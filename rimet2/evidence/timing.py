"""Timing: speech segments, pauses, breath groups, speaking rate (syllable nuclei via energy-envelope peaks)."""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.signal import butter, find_peaks, sosfiltfilt

from .dsp import energy_vad


@dataclass
class TimingStats:
    speech_segments: list[tuple[float, float]]
    pauses: list[tuple[float, float]]  # (start, end) of silences >= min_pause inside the speech span
    speech_time_s: float
    syllables: int
    rate_syl_s: float
    onset_s: float
    offset_s: float
    nuclei_t: list[float] = field(default_factory=list)


def syllable_nuclei(x: np.ndarray, sr: int, segs, min_dist: float = 0.09, prom_db: float = 2.0) -> list[float]:
    """De Jong & Wempe-style nuclei: peaks of the 2-6 kHz-free intensity envelope inside speech segments."""
    sos = butter(4, [250, min(3000, sr / 2 - 100)], btype="band", fs=sr, output="sos")
    y = sosfiltfilt(sos, x.astype(np.float64))
    hop = int(0.01 * sr)
    win = int(0.04 * sr)
    n = max(1, 1 + (len(y) - win) // hop)
    env = np.array([np.sqrt(np.mean(y[i * hop:i * hop + win] ** 2) + 1e-12) for i in range(n)])
    env_db = 20 * np.log10(env + 1e-9)
    t = (np.arange(n) * hop + win / 2) / sr
    peaks, _ = find_peaks(env_db, distance=max(1, int(min_dist / 0.01)), prominence=prom_db)
    floor = np.percentile(env_db, 20)
    out = []
    for p in peaks:
        if env_db[p] < floor + 6:
            continue
        if any(a <= t[p] <= b for a, b in segs):
            out.append(float(t[p]))
    return out


def timing(x: np.ndarray, sr: int, segs: list[tuple[float, float]] | None = None, min_pause: float = 0.2) -> TimingStats:
    segs = energy_vad(x, sr) if segs is None else segs
    if not segs:
        return TimingStats([], [], 0.0, 0, 0.0, 0.0, 0.0)
    pauses = [(a[1], b[0]) for a, b in zip(segs[:-1], segs[1:]) if b[0] - a[1] >= min_pause]
    sp = float(sum(b - a for a, b in segs))
    nuc = syllable_nuclei(x, sr, segs)
    return TimingStats(segs, pauses, sp, len(nuc), len(nuc) / sp if sp > 0 else 0.0, segs[0][0], segs[-1][1], nuc)


def isochrony(nuclei: list[float]) -> float | None:
    """Coefficient of variation of inter-nucleus intervals (low => near-isochronous rhythm)."""
    if len(nuclei) < 5:
        return None
    d = np.diff(nuclei)
    return float(np.std(d) / (np.mean(d) + 1e-9))
