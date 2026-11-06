"""Voice-quality cues (heuristic, medium confidence). Literature: Kane/Drugman creak detection, CPP, HNR.

- creak: speech frames with very low / irregular F0 (YIN period < 75 Hz or high aperiodicity at low energy)
- breathiness (relative to the same speaker): lower HNR and higher spectral tilt than the speaker's own median
These are used only for claims gated by calibration; never alone for strong statements.
"""
from __future__ import annotations

import numpy as np

from .dsp import frame_db


def creak_spans(t: np.ndarray, f0: np.ndarray, ap: np.ndarray, x: np.ndarray, sr: int, segs,
                f0_max: float = 75.0, min_dur: float = 0.08) -> list[tuple[float, float]]:
    db, tdb = frame_db(x, sr, win=0.04, hop=0.01)
    db_i = np.interp(t, tdb, db)
    in_speech = np.zeros_like(t, bool)
    for a, b in segs:
        in_speech |= (t >= a) & (t <= b)
    loud = db_i > np.percentile(db_i, 30)
    cre = in_speech & loud & np.isfinite(f0) & (f0 < f0_max)
    spans, start = [], None
    for i, v in enumerate(cre):
        if v and start is None:
            start = t[i]
        if (not v or i == len(cre) - 1) and start is not None:
            end = t[i]
            if end - start >= min_dur:
                spans.append((round(float(start), 2), round(float(end), 2)))
            start = None
    return spans


def hnr_db(x: np.ndarray, sr: int, f0_hz: float) -> float:
    """Autocorrelation HNR at the lag of the given F0 (Boersma-style approximation)."""
    if not np.isfinite(f0_hz) or f0_hz <= 0:
        return float("nan")
    lag = int(round(sr / f0_hz))
    x = x - x.mean()
    if len(x) <= lag + 10:
        return float("nan")
    r0 = np.dot(x, x)
    r = np.dot(x[:-lag], x[lag:]) / (r0 + 1e-12)
    r = min(max(r, 1e-6), 0.999999)
    return float(10 * np.log10(r / (1 - r)))
