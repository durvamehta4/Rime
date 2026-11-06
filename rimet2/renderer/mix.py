"""Timed mixing: background bed at a target SNR (set on ACTIVE speech) and events at exact times/levels.

Labels report ACHIEVED values (measured on the actual signals), not requested ones.
"""
from __future__ import annotations

import numpy as np

from rimet2.evidence.dsp import active_mask, energy_vad


def active_power(x: np.ndarray, sr: int, segs=None) -> float:
    segs = energy_vad(x, sr) if segs is None else segs
    m = active_mask(x, sr, segs)
    v = x[m] if m.any() else x
    return float(np.mean(v.astype(np.float64) ** 2) + 1e-12)


def fit_len(n: np.ndarray, L: int, rng: np.random.Generator) -> np.ndarray:
    if len(n) >= L:
        s = int(rng.integers(0, len(n) - L + 1))
        return n[s:s + L]
    reps = int(np.ceil(L / len(n)))
    return np.tile(n, reps)[:L]


def add_bed(speech: np.ndarray, sr: int, noise: np.ndarray, snr_db: float, rng: np.random.Generator, segs=None
            ) -> tuple[np.ndarray, dict]:
    n = fit_len(noise, len(speech), rng).astype(np.float64)
    ps = active_power(speech, sr, segs)
    pn = float(np.mean(n ** 2) + 1e-12)
    g = np.sqrt(ps / (pn * 10 ** (snr_db / 10)))
    nb = n * g
    achieved = 10 * np.log10(ps / (np.mean(nb ** 2) + 1e-12))
    return (speech + nb).astype(np.float32), {"bed_snr_db": round(float(achieved), 2)}


def place_event(y: np.ndarray, sr: int, ev: np.ndarray, t0: float, level_db_rel_speech: float, ref_power: float,
                fade_ms: float = 10.0, t1: float | None = None) -> tuple[np.ndarray, dict]:
    s = int(round(t0 * sr))
    if t1 is not None:
        ev = ev[:max(1, int(round((t1 - t0) * sr)))]
    e = ev.astype(np.float64)[: max(0, len(y) - s)]
    if len(e) == 0:
        return y, {}
    f = min(int(fade_ms * sr / 1000), len(e) // 2)
    if f > 0:
        ramp = np.linspace(0, 1, f)
        e[:f] *= ramp
        e[-f:] *= ramp[::-1]
    pe = float(np.mean(e ** 2) + 1e-12)
    g = np.sqrt(ref_power * 10 ** (level_db_rel_speech / 10) / pe)
    out = y.astype(np.float64).copy()
    out[s:s + len(e)] += e * g
    return out.astype(np.float32), {"t0": round(s / sr, 3), "t1": round((s + len(e)) / sr, 3),
                                    "level_db_rel_speech": level_db_rel_speech}
