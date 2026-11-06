"""Synthetic speech-like signals for CPU tests (harmonic source + syllable envelope + pauses)."""
import numpy as np


def voiced(f0_start: float, f0_end: float, dur: float, sr: int, syl_rate: float = 5.0, n_harm: int = 25,
           seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    t = np.arange(int(dur * sr)) / sr
    f0 = np.geomspace(f0_start, f0_end, len(t))
    phase = 2 * np.pi * np.cumsum(f0) / sr
    x = np.zeros_like(t)
    for h in range(1, n_harm + 1):
        fh = f0 * h
        amp = np.where(fh < sr / 2 - 200, 1.0 / h, 0.0)
        x += amp * np.sin(h * phase)
    env = 0.55 + 0.45 * np.sin(2 * np.pi * syl_rate * t - np.pi / 2)  # syllable-rate envelope
    x = x * env ** 2 + 0.002 * rng.standard_normal(len(t))
    return (0.3 * x / np.max(np.abs(x))).astype(np.float32)


def utterance(sr: int = 16000, f0: float = 200.0, pause: float = 0.5, seed: int = 0) -> tuple[np.ndarray, list]:
    """1.5 s voiced, `pause` s silence, 1.5 s voiced. Returns audio and true speech spans."""
    a = voiced(f0, f0 * 1.1, 1.5, sr, seed=seed)
    b = voiced(f0 * 1.05, f0 * 0.9, 1.5, sr, seed=seed + 1)
    sil = np.zeros(int(pause * sr), np.float32) + 0.0005 * np.random.default_rng(seed).standard_normal(int(pause * sr)
                                                                                                      ).astype(np.float32)
    lead = np.zeros(int(0.2 * sr), np.float32)
    x = np.concatenate([lead, a, sil, b, lead])
    return x, [(0.2, 1.7), (1.7 + pause, 3.2 + pause)]
