"""Audio I/O helpers: load, resample, save, hash. Pure numpy/scipy/soundfile so they run anywhere."""
from __future__ import annotations

import hashlib
import io
from pathlib import Path
from typing import Union

import numpy as np
import soundfile as sf
from scipy.signal import resample_poly

PathLike = Union[str, Path]


def to_mono(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float32)
    if x.ndim == 2:
        # soundfile returns (frames, channels)
        x = x.mean(axis=1)
    return x


def resample(x: np.ndarray, sr_in: int, sr_out: int) -> np.ndarray:
    """Polyphase resampling (anti-aliased). Returns float32."""
    if sr_in == sr_out:
        return np.asarray(x, dtype=np.float32)
    g = np.gcd(int(sr_in), int(sr_out))
    y = resample_poly(np.asarray(x, dtype=np.float64), sr_out // g, sr_in // g)
    return y.astype(np.float32)


def load(path_or_bytes: Union[PathLike, bytes], sr: int | None = None) -> tuple[np.ndarray, int]:
    """Load audio as mono float32. Accepts a path or raw encoded bytes (e.g. Vaani parquet `audio.bytes`)."""
    if isinstance(path_or_bytes, (bytes, bytearray)):
        x, file_sr = sf.read(io.BytesIO(path_or_bytes), dtype="float32", always_2d=False)
    else:
        x, file_sr = sf.read(str(path_or_bytes), dtype="float32", always_2d=False)
    x = to_mono(x)
    if sr is not None and sr != file_sr:
        x = resample(x, file_sr, sr)
        file_sr = sr
    return x, int(file_sr)


def save(path: PathLike, x: np.ndarray, sr: int, subtype: str = "PCM_16") -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    x = np.asarray(x, dtype=np.float32)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    if peak > 1.0:  # never hard-clip silently; normalise instead
        x = x / peak * 0.99
    sf.write(str(path), x, sr, subtype=subtype)


def sha256_file(path: PathLike, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def rms_db(x: np.ndarray, eps: float = 1e-12) -> float:
    return float(10 * np.log10(np.mean(np.square(x, dtype=np.float64)) + eps))


def duration(x: np.ndarray, sr: int) -> float:
    return len(x) / float(sr)
