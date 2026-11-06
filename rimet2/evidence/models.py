"""Optional neural analysers (lazy imports; run on the GPU server). Each returns plain python data.

Install names (see requirements-server.txt): silero-vad, pyannote.audio (brouhaha, gated HF), panns-inference,
transformers (audeering age/gender, CC-BY-NC-SA: research only), funasr (emotion2vec+).
Every wrapper fails soft: returns None if the dependency/weights are missing, so the pipeline still runs on DSP.
"""
from __future__ import annotations

import logging
from functools import lru_cache

import numpy as np

from rimet2.common.audio import resample

log = logging.getLogger(__name__)


# ---------------- Silero VAD ----------------
@lru_cache(maxsize=1)
def _silero():
    from silero_vad import get_speech_timestamps, load_silero_vad

    return load_silero_vad(), get_speech_timestamps


def silero_segments(x: np.ndarray, sr: int) -> list[tuple[float, float]] | None:
    try:
        import torch

        model, gst = _silero()
        x16 = resample(x, sr, 16000)
        ts = gst(torch.from_numpy(x16), model, sampling_rate=16000, return_seconds=True)
        return [(float(d["start"]), float(d["end"])) for d in ts]
    except Exception as e:
        log.debug("silero unavailable: %s", e)
        return None


# ---------------- Brouhaha: frame-level VAD, SNR, C50 ----------------
@lru_cache(maxsize=1)
def _brouhaha(device: str = "cuda"):
    import torch
    from pyannote.audio import Inference, Model

    m = Model.from_pretrained("pyannote/brouhaha")
    return Inference(m, device=torch.device(device))


def brouhaha(x: np.ndarray, sr: int, device: str = "cuda") -> dict | None:
    """Returns {'snr_db': median over speech frames, 'c50_db': median over speech frames, 'speech_frac': ...}."""
    try:
        import torch

        inf = _brouhaha(device)
        x16 = resample(x, sr, 16000)
        out = inf({"waveform": torch.from_numpy(x16)[None], "sample_rate": 16000})
        arr = np.array([v for _, v in out])  # (frames, 3): vad, snr, c50
        sp = arr[:, 0] > 0.5
        if sp.sum() == 0:
            return {"snr_db": None, "c50_db": None, "speech_frac": 0.0}
        return {"snr_db": float(np.median(arr[sp, 1])), "c50_db": float(np.median(arr[sp, 2])),
                "speech_frac": float(sp.mean())}
    except Exception as e:
        log.debug("brouhaha unavailable: %s", e)
        return None


# ---------------- PANNs sound event detection (AudioSet, framewise) ----------------
@lru_cache(maxsize=1)
def _panns(device: str = "cuda"):
    from panns_inference import SoundEventDetection, labels

    return SoundEventDetection(checkpoint_path=None, device=device), labels


SPEECH_LIKE = {"Speech", "Male speech, man speaking", "Female speech, woman speaking", "Child speech, kid speaking",
               "Conversation", "Narration, monologue", "Speech synthesizer", "Inside, small room",
               "Inside, large room or hall", "Silence"}
VOCAL_EVENTS = {"Laughter", "Giggle", "Chuckle, chortle", "Belly laugh", "Cough", "Sneeze", "Sigh", "Breathing",
                "Gasp", "Throat clearing", "Crying, sobbing", "Whispering", "Shout", "Yell", "Screaming", "Humming",
                "Singing", "Whistling", "Sniff"}


def sed_events(x: np.ndarray, sr: int, thr: float = 0.3, min_dur: float = 0.15, device: str = "cuda",
               top_k: int = 8) -> list[dict] | None:
    """Timed AudioSet events (excluding generic speech). PANNs runs at 32 kHz, ~10 ms frames."""
    try:
        sed, labels = _panns(device)
        x32 = resample(x, sr, 32000)
        fw = sed.inference(x32[None, :])[0]  # (frames, 527)
        hop = len(x32) / 32000 / fw.shape[0]
        events = []
        for k in np.argsort(-fw.max(0))[:top_k * 3]:
            lab = labels[k]
            if lab in SPEECH_LIKE:
                continue
            on = fw[:, k] > thr
            start = None
            for i, v in enumerate(np.append(on, False)):
                if v and start is None:
                    start = i
                if not v and start is not None:
                    t0, t1 = start * hop, i * hop
                    if t1 - t0 >= min_dur:
                        events.append({"label": lab, "t0": round(t0, 2), "t1": round(t1, 2),
                                       "p": float(fw[start:i, k].max()),
                                       "vocal": lab in VOCAL_EVENTS})
                    start = None
        events.sort(key=lambda e: -e["p"])
        return events[:top_k]
    except Exception as e:
        log.debug("panns unavailable: %s", e)
        return None


# ---------------- audEERING age/gender (wav2vec2-large-robust-24-ft-age-gender) ----------------
@lru_cache(maxsize=1)
def _agegender(device: str = "cuda"):
    import torch
    import torch.nn as nn
    from transformers import Wav2Vec2Processor
    from transformers.models.wav2vec2.modeling_wav2vec2 import Wav2Vec2Model, Wav2Vec2PreTrainedModel

    class ModelHead(nn.Module):
        def __init__(self, config, num_labels):
            super().__init__()
            self.dense = nn.Linear(config.hidden_size, config.hidden_size)
            self.dropout = nn.Dropout(config.final_dropout)
            self.out_proj = nn.Linear(config.hidden_size, num_labels)

        def forward(self, x):
            return self.out_proj(self.dropout(torch.tanh(self.dense(self.dropout(x)))))

    class AgeGenderModel(Wav2Vec2PreTrainedModel):
        def __init__(self, config):
            super().__init__(config)
            self.wav2vec2 = Wav2Vec2Model(config)
            self.age = ModelHead(config, 1)
            self.gender = ModelHead(config, 3)
            self.init_weights()

        def forward(self, input_values):
            h = self.wav2vec2(input_values)[0].mean(dim=1)
            return self.age(h), torch.softmax(self.gender(h), dim=1)

    name = "audeering/wav2vec2-large-robust-24-ft-age-gender"
    return Wav2Vec2Processor.from_pretrained(name), AgeGenderModel.from_pretrained(name).to(device).eval(), device


def age_gender(x: np.ndarray, sr: int, device: str = "cuda") -> dict | None:
    try:
        import torch

        proc, model, dev = _agegender(device)
        x16 = resample(x, sr, 16000)
        y = proc(x16, sampling_rate=16000)["input_values"][0]
        with torch.inference_mode():
            age, g = model(torch.from_numpy(np.asarray(y))[None].to(dev))
        g = g[0].cpu().numpy()  # female, male, child
        return {"age_years": float(age[0, 0].item() * 100), "p_female": float(g[0]), "p_male": float(g[1]),
                "p_child": float(g[2])}
    except Exception as e:
        log.debug("age/gender unavailable: %s", e)
        return None
