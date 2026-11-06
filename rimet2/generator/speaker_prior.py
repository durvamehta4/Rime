r"""Attribute-conditioned speaker prior for speaker diversity.

Bank: one row per real speaker (IndicVoices-R, Vaani clean subset, Rasa) with a clean reference clip, its text,
attributes (gender, age_band, region, lang, f0_median) and an SV embedding (WavLM-SV; also ECAPA if available).
Selection for one description: filter by the described attributes, then farthest-point sampling

    z_{k+1} = argmax_{z in Z_a} min_{j<=k} (1 - cos(z, z_j))

keeping only candidates whose cosine to every chosen voice is < theta (0.86 WavLM default) when possible.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


@dataclass
class Voice:
    speaker_id: str
    ref_path: str
    ref_text: str
    lang: str
    gender: str | None = None
    age_band: str | None = None
    region: str | None = None
    f0_median: float | None = None
    emb: np.ndarray | None = field(default=None, repr=False)


class SpeakerBank:
    def __init__(self, voices: list[Voice]):
        self.voices = voices
        self.E = np.stack([v.emb / (np.linalg.norm(v.emb) + 1e-9) for v in voices]) if voices else np.zeros((0, 1))

    @classmethod
    def load(cls, jsonl: str | Path, emb_npy: str | Path) -> "SpeakerBank":
        E = np.load(emb_npy)
        vs = []
        for i, line in enumerate(open(jsonl, encoding="utf-8")):
            d = json.loads(line)
            vs.append(Voice(**{k: d.get(k) for k in ("speaker_id", "ref_path", "ref_text", "lang", "gender",
                                                     "age_band", "region", "f0_median")}, emb=E[i]))
        return cls(vs)

    def save(self, jsonl: str | Path, emb_npy: str | Path) -> None:
        with open(jsonl, "w", encoding="utf-8") as f:
            for v in self.voices:
                f.write(json.dumps({k: getattr(v, k) for k in ("speaker_id", "ref_path", "ref_text", "lang", "gender",
                                                              "age_band", "region", "f0_median")},
                                   ensure_ascii=False) + "\n")
        np.save(emb_npy, np.stack([v.emb for v in self.voices]))

    def candidates(self, lang: str | None = None, gender: str | None = None, f0_hz: float | None = None,
                   age_band: str | None = None, region: str | None = None, f0_tol_st: float = 3.0) -> np.ndarray:
        idx = []
        for i, v in enumerate(self.voices):
            if lang and v.lang and v.lang != lang:
                continue
            if gender and v.gender and v.gender != gender:
                continue
            if f0_hz and v.f0_median and abs(12 * np.log2(v.f0_median / f0_hz)) > f0_tol_st:
                continue
            if age_band and v.age_band and v.age_band != age_band:
                continue
            if region and v.region and region.lower() not in v.region.lower():
                continue
            idx.append(i)
        return np.array(idx, dtype=int)

    def sample(self, n: int, seed: int = 0, theta: float = 0.86, relax: bool = True, **attrs) -> list[Voice]:
        rng = np.random.default_rng(seed)
        cand = self.candidates(**attrs)
        if len(cand) < n and relax:  # relax the softest constraints first
            for drop in ("region", "age_band", "f0_hz"):
                attrs.pop(drop, None)
                cand = self.candidates(**attrs)
                if len(cand) >= n:
                    break
        if len(cand) == 0:
            return []
        chosen = [int(cand[rng.integers(len(cand))])]
        while len(chosen) < min(n, len(cand)):
            S = self.E[cand] @ self.E[chosen].T  # (cand, chosen)
            maxsim = S.max(axis=1)
            maxsim[np.isin(cand, chosen)] = np.inf
            ok = maxsim < theta
            pick = np.where(ok)[0] if ok.any() else np.arange(len(cand))
            j = pick[np.argmin(maxsim[pick])]
            chosen.append(int(cand[j]))
        return [self.voices[i] for i in chosen]


def mix_voice(a: np.ndarray, b: np.ndarray, alpha: float) -> np.ndarray:
    """Interpolate two speaker embeddings into a voice that does not exist (if the backend accepts embeddings)."""
    z = alpha * a / np.linalg.norm(a) + (1 - alpha) * b / np.linalg.norm(b)
    return z / np.linalg.norm(z)
