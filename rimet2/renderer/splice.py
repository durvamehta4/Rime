"""Insert a vocal event (laugh, breath, cough) INTO the speech timeline at a word gap, shifting later audio.

Audio outside the inserted region is bit-exact (SSR-Speech style), so all other labels stay valid
(timed labels after the insertion point shift by the inserted duration; we return the shift).
"""
from __future__ import annotations

import numpy as np


def find_gaps(segs: list[tuple[float, float]], min_gap: float = 0.3) -> list[tuple[float, float]]:
    return [(a[1], b[0]) for a, b in zip(segs[:-1], segs[1:]) if b[0] - a[1] >= min_gap]


def insert_at(x: np.ndarray, sr: int, ev: np.ndarray, t: float, gain: float = 1.0, fade_ms: float = 15.0
              ) -> tuple[np.ndarray, dict]:
    k = int(round(t * sr))
    e = ev.astype(np.float32).copy() * gain
    f = min(int(fade_ms * sr / 1000), len(e) // 2)
    if f > 0:
        r = np.linspace(0, 1, f, dtype=np.float32)
        e[:f] *= r
        e[-f:] *= r[::-1]
    y = np.concatenate([x[:k], e, x[k:]]).astype(np.float32)
    return y, {"t0": round(k / sr, 3), "t1": round((k + len(e)) / sr, 3), "shift_s": round(len(e) / sr, 3)}


def shift_spans(spans: list[tuple[float, float]], at: float, by: float) -> list[tuple[float, float]]:
    return [(a + by if a >= at else a, b + by if b >= at else b) for a, b in spans]
