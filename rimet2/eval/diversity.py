"""Speaker diversity (PS: 10 samples per description; count distinct speakers among samples that pass relevance,
using a fixed SV model at its standard threshold; points = 2 * mean_count / 10).

The PS does not name the SV model, so we report two: WavLM-base-plus-sv (cosine 0.86, model-card threshold) and
SpeechBrain ECAPA (cosine 0.25). "Distinct speakers" = connected components of the same-speaker graph.
"""
from __future__ import annotations

from functools import lru_cache

import numpy as np

THRESHOLDS = {"wavlm": 0.86, "ecapa": 0.25}


def cosine_matrix(emb: np.ndarray) -> np.ndarray:
    e = emb / (np.linalg.norm(emb, axis=1, keepdims=True) + 1e-9)
    return e @ e.T


def count_distinct(emb: np.ndarray, threshold: float) -> int:
    """Number of connected components where an edge means cos >= threshold (same speaker)."""
    n = len(emb)
    if n == 0:
        return 0
    sim = cosine_matrix(emb)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(n):
        for j in range(i + 1, n):
            if sim[i, j] >= threshold:
                parent[find(i)] = find(j)
    return len({find(i) for i in range(n)})


def diversity_points(counts: list[int]) -> float:
    return 2.0 * (sum(counts) / len(counts)) / 10.0 if counts else 0.0


class WavLMSV:
    def __init__(self, model_id: str = "microsoft/wavlm-base-plus-sv", device: str = "cpu"):
        from transformers import AutoFeatureExtractor, WavLMForXVector

        self.fe = AutoFeatureExtractor.from_pretrained(model_id)
        self.model = WavLMForXVector.from_pretrained(model_id).to(device).eval()
        self.device = device

    def embed(self, wavs16k: list[np.ndarray]) -> np.ndarray:
        import torch

        out = []
        for w in wavs16k:
            inp = self.fe([w], sampling_rate=16000, return_tensors="pt", padding=True).to(self.device)
            with torch.inference_mode():
                out.append(self.model(**inp).embeddings[0].cpu().numpy())
        return np.stack(out)


class EcapaSV:
    def __init__(self, source: str = "speechbrain/spkrec-ecapa-voxceleb", device: str = "cpu"):
        from speechbrain.inference.speaker import EncoderClassifier

        self.model = EncoderClassifier.from_hparams(source=source, run_opts={"device": device})

    def embed(self, wavs16k: list[np.ndarray]) -> np.ndarray:
        import torch

        out = []
        for w in wavs16k:
            with torch.inference_mode():
                out.append(self.model.encode_batch(torch.from_numpy(w).unsqueeze(0)).squeeze().cpu().numpy())
        return np.stack(out)


@lru_cache(maxsize=2)
def get_sv(name: str = "wavlm", device: str = "cpu"):
    return WavLMSV(device=device) if name == "wavlm" else EcapaSV(device=device)
