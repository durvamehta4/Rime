"""F0 tracking. Default: numpy YIN (CPU, deterministic). On the server prefer PENN or torchcrepe (`backend=`).

Statistics are on voiced frames only, in Hz and semitones: st(f1, f2) = 12 * log2(f2 / f1).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def yin(x: np.ndarray, sr: int, fmin: float = 50.0, fmax: float = 600.0, hop: float = 0.01, win: float = 0.04,
        thresh: float = 0.15) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (times, f0_hz with nan for unvoiced, aperiodicity)."""
    W, H = int(win * sr), int(hop * sr)
    tau_min, tau_max = int(sr / fmax), min(int(sr / fmin), W - 1)
    if len(x) < W + tau_max:
        x = np.pad(x, (0, W + tau_max - len(x)))
    n = 1 + (len(x) - W - tau_max) // H
    f0 = np.full(n, np.nan)
    ap = np.ones(n)
    for i in range(n):
        s = i * H
        fr = x[s:s + W + tau_max].astype(np.float64)
        if np.mean(fr[:W] ** 2) < 1e-7:
            continue
        # difference function via FFT autocorrelation
        x1 = fr[:W]
        cum = np.concatenate([[0], np.cumsum(fr ** 2)])
        energy0 = cum[W] - cum[0]
        energies = cum[np.arange(tau_max + 1) + W] - cum[np.arange(tau_max + 1)]
        N = 1 << int(np.ceil(np.log2(W + tau_max + W)))
        ac = np.fft.irfft(np.fft.rfft(fr, N) * np.conj(np.fft.rfft(x1, N)), N)[:tau_max + 1]
        d = energy0 + energies - 2 * ac
        d[0] = 0
        cmnd = np.ones_like(d)
        cs = np.cumsum(d[1:])
        cmnd[1:] = d[1:] * np.arange(1, tau_max + 1) / np.maximum(cs, 1e-12)
        cand = np.where(cmnd[tau_min:] < thresh)[0]
        if len(cand) == 0:
            continue
        tau = cand[0] + tau_min
        while tau + 1 <= tau_max and cmnd[tau + 1] < cmnd[tau]:
            tau += 1
        # parabolic interpolation
        if 1 <= tau < tau_max:
            a, b, c = cmnd[tau - 1], cmnd[tau], cmnd[tau + 1]
            den = a - 2 * b + c
            shift = 0.5 * (a - c) / den if abs(den) > 1e-12 else 0.0
        else:
            shift = 0.0
        f0[i] = sr / (tau + shift)
        ap[i] = cmnd[tau]
    t = (np.arange(n) * H + W / 2) / sr
    return t, f0, ap


def track(x: np.ndarray, sr: int, backend: str = "yin", device: str = "cpu", **kw):
    if backend == "yin":
        return yin(x, sr, **kw)
    if backend == "torchcrepe":
        import torch
        import torchcrepe

        from rimet2.common.audio import resample
        x16 = resample(x, sr, 16000)
        audio = torch.from_numpy(x16).unsqueeze(0)
        f0, per = torchcrepe.predict(audio, 16000, 160, 50, 600, "full", return_periodicity=True, batch_size=512,
                                     device=device)
        f0, per = f0[0].cpu().numpy(), per[0].cpu().numpy()
        f0 = np.where(per > 0.5, f0, np.nan)
        t = np.arange(len(f0)) * 0.01
        return t, f0, 1 - per
    if backend == "penn":
        import penn
        import torch

        from rimet2.common.audio import resample
        x16 = resample(x, sr, 16000)
        f0, per = penn.from_audio(torch.from_numpy(x16)[None], 16000, hopsize=0.01, fmin=50, fmax=600,
                                  gpu=0 if device.startswith("cuda") else None)
        f0, per = f0[0].cpu().numpy(), per[0].cpu().numpy()
        f0 = np.where(per > 0.065, f0, np.nan)  # PENN recommended voicing threshold
        return np.arange(len(f0)) * 0.01, f0, 1 - per
    raise ValueError(backend)


def semitones(f1: float, f2: float) -> float:
    return float(12 * np.log2(f2 / f1))


@dataclass
class PitchStats:
    median_hz: float
    p10_hz: float
    p90_hz: float
    range_st: float  # p10..p90 span in semitones
    voiced_frac: float
    n_voiced: int


def stats(f0: np.ndarray) -> PitchStats | None:
    v = f0[np.isfinite(f0)]
    if len(v) < 10:
        return None
    p10, p50, p90 = np.percentile(v, [10, 50, 90])
    return PitchStats(float(p50), float(p10), float(p90), semitones(p10, p90), float(len(v) / len(f0)), int(len(v)))


def segment_slope_st(t: np.ndarray, f0: np.ndarray, a: float, b: float) -> float | None:
    """Pitch movement (semitones) across [a, b] from a linear fit on voiced frames (positive = rise)."""
    m = (t >= a) & (t <= b) & np.isfinite(f0)
    if m.sum() < 8:
        return None
    st = 12 * np.log2(f0[m] / np.median(f0[m]))
    k = np.polyfit(t[m], st, 1)[0]
    return float(k * (b - a))
