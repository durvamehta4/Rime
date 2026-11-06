"""Pure-DSP measurements (numpy/scipy). Deterministic, fast, no model weights -> the backbone of verifiable claims."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.signal import stft


def frame_db(x: np.ndarray, sr: int, win: float = 0.025, hop: float = 0.010) -> tuple[np.ndarray, np.ndarray]:
    """Frame RMS in dB and frame centre times."""
    w, h = int(win * sr), int(hop * sr)
    if len(x) < w:
        x = np.pad(x, (0, w - len(x)))
    n = 1 + (len(x) - w) // h
    idx = np.arange(w)[None, :] + h * np.arange(n)[:, None]
    fr = x[idx]
    db = 10 * np.log10(np.mean(fr.astype(np.float64) ** 2, axis=1) + 1e-12)
    t = (np.arange(n) * h + w / 2) / sr
    return db, t


def energy_vad(x: np.ndarray, sr: int, margin_db: float = 12.0, min_speech: float = 0.12,
               min_gap: float = 0.15) -> list[tuple[float, float]]:
    """Energy VAD fallback (Silero is preferred when available). Threshold = noise floor + margin."""
    db, t = frame_db(x, sr)
    floor = np.percentile(db, 10)
    peak = np.percentile(db, 95)
    thr = max(floor + margin_db, peak - 35)
    on = db > thr
    segs, start = [], None
    for i, v in enumerate(on):
        if v and start is None:
            start = t[i]
        if not v and start is not None:
            segs.append([start, t[i]])
            start = None
    if start is not None:
        segs.append([start, t[-1]])
    merged = []
    for s in segs:
        if merged and s[0] - merged[-1][1] < min_gap:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return [(round(a, 3), round(b, 3)) for a, b in merged if b - a >= min_speech]


def active_mask(x: np.ndarray, sr: int, segs: list[tuple[float, float]]) -> np.ndarray:
    m = np.zeros(len(x), bool)
    for a, b in segs:
        m[int(a * sr):int(b * sr)] = True
    return m


def snr_active(x: np.ndarray, sr: int, segs: list[tuple[float, float]] | None = None) -> float:
    """Crude SNR: active-speech power vs. inactive power (noise-floor estimate). Brouhaha is the better tool."""
    segs = energy_vad(x, sr) if segs is None else segs
    m = active_mask(x, sr, segs)
    if m.all() or not m.any():
        db, _ = frame_db(x, sr)
        return float(np.percentile(db, 95) - np.percentile(db, 5))
    ps = np.mean(x[m].astype(np.float64) ** 2)
    pn = np.mean(x[~m].astype(np.float64) ** 2) + 1e-12
    return float(10 * np.log10(max(ps - pn, 1e-12) / pn))


@dataclass
class Band:
    low_hz: float
    high_hz: float
    narrowband: bool


def bandwidth(x: np.ndarray, sr: int, floor_db: float = -45.0) -> Band:
    """Effective band edges: lowest/highest frequency where long-term spectrum is within `floor_db` of its peak."""
    f, _, Z = stft(x, fs=sr, nperseg=1024, noverlap=768)
    psd = np.mean(np.abs(Z) ** 2, axis=1)
    db = 10 * np.log10(psd + 1e-20)
    db -= db.max()
    # smooth to avoid single-bin spikes
    k = 5
    db_s = np.convolve(db, np.ones(k) / k, mode="same")
    above = np.where(db_s > floor_db)[0]
    if len(above) == 0:
        return Band(0.0, sr / 2, False)
    # high edge: last bin above floor whose energy is sustained (avoid aliasing junk)
    hi = f[above[-1]]
    lo = f[above[0]]
    return Band(float(lo), float(hi), bool(hi < 4200))


def clipping_ratio(x: np.ndarray, thr: float = 0.99, run: int = 3) -> float:
    """Fraction of samples in flat runs at |x| >= thr*peak (peak normalised); a codec/loudness clipping cue."""
    a = np.abs(x)
    peak = a.max() if a.size else 0
    if peak < 1e-4:
        return 0.0
    hot = a >= thr * peak
    if hot.sum() == 0:
        return 0.0
    # count runs of consecutive hot samples of length >= run
    d = np.diff(np.concatenate([[0], hot.astype(np.int8), [0]]))
    starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
    lens = ends - starts
    return float(lens[lens >= run].sum() / len(x))


def spectral_centroid_series(x: np.ndarray, sr: int, hop: float = 0.05) -> tuple[np.ndarray, np.ndarray]:
    n = 1024
    f, t, Z = stft(x, fs=sr, nperseg=n, noverlap=n - int(hop * sr))
    mag = np.abs(Z)
    c = (f[:, None] * mag).sum(0) / (mag.sum(0) + 1e-12)
    return c, t


def level_change_db(x: np.ndarray, sr: int, t_split: float, segs: list[tuple[float, float]]) -> float | None:
    """Active-speech level after t_split minus before (dB). Used for Coupling (Lombard) claims."""
    m = active_mask(x, sr, segs)
    k = int(t_split * sr)
    a, b = x[:k][m[:k]], x[k:][m[k:]]
    if len(a) < sr * 0.3 or len(b) < sr * 0.3:
        return None
    return float(10 * np.log10(np.mean(b ** 2) + 1e-12) - 10 * np.log10(np.mean(a ** 2) + 1e-12))


def loudness_flatness(x: np.ndarray, sr: int, segs: list[tuple[float, float]]) -> float:
    """Std (dB) of 100 ms active-speech levels; small => flat loudness."""
    db, t = frame_db(x, sr, win=0.1, hop=0.05)
    keep = np.zeros_like(t, bool)
    for a, b in segs:
        keep |= (t >= a) & (t <= b)
    v = db[keep]
    return float(np.std(v)) if v.size > 2 else 0.0


def rt60_from_rir(rir: np.ndarray, sr: int) -> float:
    """Schroeder backward integration; T20 extrapolated to 60 dB (falls back to T10)."""
    e = np.cumsum(rir[::-1].astype(np.float64) ** 2)[::-1]
    edc = 10 * np.log10(e / e[0] + 1e-20)
    t = np.arange(len(rir)) / sr

    def fit(lo, hi):
        i = np.where((edc <= lo) & (edc >= hi))[0]
        if len(i) < 10:
            return None
        slope = np.polyfit(t[i], edc[i], 1)[0]
        return -60.0 / slope if slope < 0 else None

    return float(fit(-5, -25) or fit(-5, -15) or 0.0)


def c50_from_rir(rir: np.ndarray, sr: int) -> float:
    k0 = int(np.argmax(np.abs(rir)))
    k = k0 + int(0.05 * sr)
    early = np.sum(rir[:k].astype(np.float64) ** 2)
    late = np.sum(rir[k:].astype(np.float64) ** 2) + 1e-20
    return float(10 * np.log10(early / late))
