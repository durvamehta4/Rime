"""Room impulse responses. Labels (RT60, C50) are always MEASURED from the RIR actually used, never the request.

Sources (licences recorded in data_manifest): OpenSLR-28 real RIRs (Apache-2.0), BUT ReverbDB (CC-BY-4.0),
MIT IR survey (CC-BY-4.0), pyroomacoustics shoebox simulation (MIT). Fallback: Polack exponential-noise model.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

from rimet2.common.audio import load
from rimet2.evidence.dsp import c50_from_rir, rt60_from_rir

SPACE_PRESETS = {  # (rt60 range s, drr-ish direct gain) -> what a listener would call it
    "dry": (0.05, 0.15),
    "small_room": (0.2, 0.4),
    "bathroom": (0.6, 1.0),
    "medium_room": (0.4, 0.7),
    "large_hall": (1.2, 2.5),
}


def polack_rir(rt60: float, sr: int, rng: np.random.Generator, direct_db: float = 0.0, length_s: float | None = None
               ) -> np.ndarray:
    """Exponentially decaying Gaussian noise tail + direct impulse. Decay constant gives exactly -60 dB at rt60."""
    L = int(sr * (length_s or max(0.3, 1.2 * rt60)))
    t = np.arange(L) / sr
    tail = rng.standard_normal(L) * np.exp(-6.907755 * t / rt60)  # ln(1000)=6.9078 -> amplitude -60 dB at rt60
    pre = int(0.0025 * sr)
    tail[:pre] = 0
    rir = tail * 0.3
    rir[0] = 10 ** (direct_db / 20)
    return (rir / np.max(np.abs(rir))).astype(np.float32)


def shoebox_rir(rt60: float, room_dim=(4.0, 3.5, 2.8), sr: int = 24000, rng: np.random.Generator | None = None
                ) -> np.ndarray:
    import pyroomacoustics as pra

    rng = rng or np.random.default_rng()
    e_abs, max_order = pra.inverse_sabine(rt60, room_dim)
    room = pra.ShoeBox(room_dim, fs=sr, materials=pra.Material(e_abs), max_order=min(max_order, 30))
    src = [rng.uniform(0.5, d - 0.5) for d in room_dim]
    mic = [rng.uniform(0.5, d - 0.5) for d in room_dim]
    room.add_source(src)
    room.add_microphone(mic)
    room.compute_rir()
    rir = np.asarray(room.rir[0][0], dtype=np.float32)
    return rir / np.max(np.abs(rir))


class RIRBank:
    """Directory of real RIR wavs; measures RT60/C50 once and samples by target RT60."""

    def __init__(self, root: str | Path | None, sr: int = 24000):
        self.items = []
        self.sr = sr
        if root and Path(root).exists():
            for p in sorted(Path(root).rglob("*.wav")):
                try:
                    r, _ = load(p, sr=sr)
                    self.items.append((str(p), r, rt60_from_rir(r, sr)))
                except Exception:
                    continue

    def sample(self, rt60: float, rng: np.random.Generator, tol: float = 0.15):
        cands = [it for it in self.items if abs(it[2] - rt60) <= tol * max(rt60, 0.3)]
        if not cands:
            return None
        return cands[rng.integers(len(cands))]


def apply_rir(x: np.ndarray, rir: np.ndarray) -> np.ndarray:
    y = fftconvolve(x, rir)[:len(x)]
    # keep active level comparable to dry input
    g = np.sqrt((np.mean(x ** 2) + 1e-12) / (np.mean(y ** 2) + 1e-12))
    return (y * g).astype(np.float32)


def make_rir(space: str, sr: int, rng: np.random.Generator, rt60: float | None = None, bank: RIRBank | None = None):
    lo, hi = SPACE_PRESETS.get(space, SPACE_PRESETS["small_room"])
    target = rt60 if rt60 is not None else float(rng.uniform(lo, hi))
    src = "polack"
    rir = None
    if bank is not None:
        hit = bank.sample(target, rng)
        if hit is not None:
            src, rir = hit[0], hit[1]
    if rir is None:
        rir = polack_rir(target, sr, rng)
    return rir, {"rir_source": src, "rt60_s": rt60_from_rir(rir, sr), "c50_db": c50_from_rir(rir, sr)}
