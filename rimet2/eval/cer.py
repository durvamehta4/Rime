"""Intelligibility: CER of AI4Bharat IndicConformer vs native-script text (PS Track 2, 1 point = 1 - CER floored).

Model: ai4bharat/indic-conformer-600m-multilingual (gated, MIT; trust_remote_code). Feed 16 kHz mono.
We fix ONE decoder ("rnnt" default) for all reporting and also log "ctc" as a robustness check.
"""
from __future__ import annotations

from functools import lru_cache

import numpy as np

from rimet2.common.audio import load
from rimet2.common.textnorm import normalize_for_cer


def edit_distance(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb))
        prev = cur
    return prev[-1]


def cer(ref: str, hyp: str, lang: str) -> float:
    r, h = normalize_for_cer(ref, lang), normalize_for_cer(hyp, lang)
    return edit_distance(r, h) / max(1, len(r))


def corpus_cer(pairs: list[tuple[str, str]], lang: str) -> float:
    errs = tot = 0
    for ref, hyp in pairs:
        r, h = normalize_for_cer(ref, lang), normalize_for_cer(hyp, lang)
        errs += edit_distance(r, h)
        tot += max(1, len(r))
    return errs / max(1, tot)


def points(mean_cer: float) -> float:
    return max(0.0, 1.0 - mean_cer)


class IndicConformerASR:
    def __init__(self, model_id: str = "ai4bharat/indic-conformer-600m-multilingual", device: str = "cuda",
                 decoder: str = "rnnt"):
        from transformers import AutoModel  # lazy

        self.model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
        try:
            self.model = self.model.to(device)
        except Exception:
            pass
        self.decoder = decoder

    def __call__(self, wav: np.ndarray | str, lang: str, decoder: str | None = None) -> str:
        import torch

        if isinstance(wav, str):
            wav, _ = load(wav, sr=16000)
        x = torch.from_numpy(np.asarray(wav, dtype=np.float32)).unsqueeze(0)
        with torch.inference_mode():
            return str(self.model(x, lang, decoder or self.decoder)).strip()


@lru_cache(maxsize=1)
def get_asr(decoder: str = "rnnt") -> IndicConformerASR:
    return IndicConformerASR(decoder=decoder)
