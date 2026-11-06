"""Voice backends (GPU server). All return (float32 mono wav, sr).

Qwen3-TTS (pip: qwen-tts, Apache-2.0). Official language list has no Hindi/Tamil: we pass language="Auto"
until our language-adapted checkpoint exists. Variants:
  CustomVoice : 9 preset speakers + instruct          (round 0)
  VoiceDesign : instruct (natural-language voice)     (voice from description)
  Base        : clone from ref audio (+ref text) or x-vector only (speaker prior -> diversity)
Indic-Parler-TTS (Apache-2.0): description-conditioned, speaks Hindi/Tamil natively (fallback / reference row).
"""
from __future__ import annotations

from functools import lru_cache

import numpy as np

from rimet2.common.audio import resample

CUSTOMVOICE_SPEAKERS = {"female": ["Vivian", "Serena", "Ono_Anna", "Sohee"],
                        "male": ["Uncle_Fu", "Dylan", "Eric", "Ryan", "Aiden"]}


@lru_cache(maxsize=4)
def _qwen(path: str, device: str = "cuda:0"):
    import torch
    from qwen_tts import Qwen3TTSModel

    try:
        return Qwen3TTSModel.from_pretrained(path, device_map=device, dtype=torch.bfloat16,
                                             attn_implementation="flash_attention_2")
    except Exception:
        return Qwen3TTSModel.from_pretrained(path, device_map=device, dtype=torch.bfloat16)


def _first(wavs, sr):
    w = wavs[0]
    w = w.detach().cpu().numpy() if hasattr(w, "detach") else np.asarray(w)
    return w.astype(np.float32).reshape(-1), int(sr)


class Qwen3TTS:
    def __init__(self, path: str, device: str = "cuda:0", language: str = "Auto"):
        self.m = _qwen(path, device)
        self.language = language

    def custom(self, text: str, speaker: str, instruct: str = "", seed: int = 0, **gen):
        import torch
        torch.manual_seed(seed)
        return _first(*self.m.generate_custom_voice(text=text, language=self.language, speaker=speaker,
                                                     instruct=instruct, **gen))

    def design(self, text: str, instruct: str, seed: int = 0, **gen):
        import torch
        torch.manual_seed(seed)
        return _first(*self.m.generate_voice_design(text=text, language=self.language, instruct=instruct, **gen))

    def clone(self, text: str, ref_audio, ref_text: str | None = None, seed: int = 0, prompt=None, **gen):
        """ref_audio: path or (np.ndarray, sr). If ref_text is None we use x-vector-only mode."""
        import torch
        torch.manual_seed(seed)
        if prompt is None:
            prompt = self.m.create_voice_clone_prompt(ref_audio=ref_audio, ref_text=ref_text,
                                                      x_vector_only_mode=ref_text is None)
        return _first(*self.m.generate_voice_clone(text=text, language=self.language, voice_clone_prompt=prompt,
                                                   **gen))

    def clone_prompt(self, ref_audio, ref_text: str | None = None):
        return self.m.create_voice_clone_prompt(ref_audio=ref_audio, ref_text=ref_text,
                                                x_vector_only_mode=ref_text is None)


@lru_cache(maxsize=1)
def _parler(path: str, device: str = "cuda:0"):
    from parler_tts import ParlerTTSForConditionalGeneration
    from transformers import AutoTokenizer

    model = ParlerTTSForConditionalGeneration.from_pretrained(path).to(device)
    tok = AutoTokenizer.from_pretrained(path)
    desc_tok = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)
    return model, tok, desc_tok


class IndicParler:
    def __init__(self, path: str = "models/indic-parler-tts", device: str = "cuda:0"):
        self.model, self.tok, self.desc_tok = _parler(path, device)
        self.device = device

    def design(self, text: str, instruct: str, seed: int = 0, out_sr: int = 24000):
        import torch
        torch.manual_seed(seed)
        d = self.desc_tok(instruct, return_tensors="pt").to(self.device)
        p = self.tok(text, return_tensors="pt").to(self.device)
        with torch.inference_mode():
            g = self.model.generate(input_ids=d.input_ids, attention_mask=d.attention_mask,
                                    prompt_input_ids=p.input_ids, prompt_attention_mask=p.attention_mask)
        w = g.cpu().numpy().squeeze().astype(np.float32)
        sr = self.model.config.sampling_rate
        return resample(w, sr, out_sr), out_sr
