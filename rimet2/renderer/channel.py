"""Channel simulation: band-limiting, real codecs via ffmpeg, clipping, packet loss. Labels are re-measured after.

Codecs available in a stock ffmpeg: G.711 mu-law/A-law, GSM 06.10 (libgsm), Opus (libopus), G.722, MP3, AAC.
AMR-NB needs an ffmpeg built with libopencore-amrnb (optional).
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from scipy.signal import butter, sosfiltfilt

from rimet2.common.audio import load, resample, save

CODECS = {
    # name: (ffmpeg encoder args, codec sample rate, container ext)
    "g711": (["-c:a", "pcm_mulaw"], 8000, "wav"),
    "gsm": (["-c:a", "libgsm"], 8000, "gsm"),
    "g722": (["-c:a", "g722"], 16000, "wav"),
    "opus_8k": (["-c:a", "libopus", "-b:a", "8k", "-application", "voip"], 16000, "ogg"),
    "opus_16k": (["-c:a", "libopus", "-b:a", "16k", "-application", "voip"], 16000, "ogg"),
    "mp3_32k": (["-c:a", "libmp3lame", "-b:a", "32k"], 16000, "mp3"),
    "amr_nb": (["-c:a", "libopencore_amrnb", "-b:a", "12.2k"], 8000, "amr"),
}

CHANNEL_PRESETS = {
    "phone_narrowband": {"band": (300, 3400), "codec": "gsm"},
    "landline": {"band": (300, 3400), "codec": "g711"},
    "voip": {"band": (80, 7000), "codec": "opus_16k"},
    "voip_poor": {"band": (100, 4000), "codec": "opus_8k", "packet_loss": 0.03},
    "laptop": {"band": (150, 9000), "codec": ""},
    "clean": {"band": None, "codec": ""},
}


def bandpass(x: np.ndarray, sr: int, lo: float, hi: float, order: int = 6) -> np.ndarray:
    hi = min(hi, sr / 2 * 0.98)
    sos = butter(order, [lo, hi], btype="band", fs=sr, output="sos")
    return sosfiltfilt(sos, x.astype(np.float64)).astype(np.float32)


def ffmpeg_codec(x: np.ndarray, sr: int, codec: str) -> np.ndarray:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg not found")
    args, csr, ext = CODECS[codec]
    with tempfile.TemporaryDirectory() as d:
        src, enc, dec = Path(d, "in.wav"), Path(d, f"enc.{ext}"), Path(d, "out.wav")
        save(src, resample(x, sr, csr), csr)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-ar", str(csr), "-ac", "1", *args,
                        str(enc)], check=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(enc), "-ar", str(sr), "-ac", "1", str(dec)],
                       check=True)
        y, _ = load(dec, sr=sr)
    y = y[:len(x)] if len(y) >= len(x) else np.pad(y, (0, len(x) - len(y)))
    return y.astype(np.float32)


def soft_clip(x: np.ndarray, drive_db: float) -> np.ndarray:
    """Drive into a hard limiter at 1.0 (peak-normalised first). drive_db=0 => no clipping."""
    x = x / (np.max(np.abs(x)) + 1e-9)
    y = np.clip(x * 10 ** (drive_db / 20), -1.0, 1.0)
    return (y / 10 ** (drive_db / 20) * 0.9).astype(np.float32) if drive_db > 0 else x.astype(np.float32)


def packet_loss(x: np.ndarray, sr: int, rate: float, rng: np.random.Generator, frame_ms: int = 20):
    y = x.copy()
    n = int(frame_ms * sr / 1000)
    lost = []
    for s in range(0, len(x) - n, n):
        if rng.random() < rate:
            y[s:s + n] = 0
            lost.append(round(s / sr, 3))
    return y, lost


def apply_channel(x: np.ndarray, sr: int, preset: str = "clean", codec: str | None = None, clip_drive_db: float = 0.0,
                  loss: float | None = None, rng: np.random.Generator | None = None) -> tuple[np.ndarray, dict]:
    rng = rng or np.random.default_rng(0)
    p = CHANNEL_PRESETS.get(preset, CHANNEL_PRESETS["clean"])
    info = {"channel_preset": preset}
    y = x
    if p.get("band"):
        y = bandpass(y, sr, *p["band"])
        info["band_hz"] = list(p["band"])
    cod = codec if codec is not None else p.get("codec", "")
    if cod:
        y = ffmpeg_codec(y, sr, cod)
        info["codec"] = cod
    if clip_drive_db > 0:
        y = soft_clip(y, clip_drive_db)
        info["clip_drive_db"] = clip_drive_db
    lr = p.get("packet_loss", 0.0) if loss is None else loss
    if lr > 0:
        y, lost = packet_loss(y, sr, lr, rng)
        info["packet_loss_rate"] = lr
        info["lost_frames_s"] = lost
    return y.astype(np.float32), info
