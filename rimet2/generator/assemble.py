"""Assemble per-segment voice audio into one timeline that honours requested times, pauses and inline events.

Timing control is by construction: silences are inserted exactly; a segment that overruns its slot is
time-compressed with WSOLA (pitch-preserving) by at most 15 %; vocal events are spliced from a same-language
event library (or rendered inline by the voice model when it supports tags).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np

from rimet2.evidence.dsp import energy_vad
from rimet2.scene.schema import RenderPlan, Segment


def trim(x: np.ndarray, sr: int, pad: float = 0.03) -> np.ndarray:
    segs = energy_vad(x, sr, margin_db=10)
    if not segs:
        return x
    a = max(0, int((segs[0][0] - pad) * sr))
    b = min(len(x), int((segs[-1][1] + pad) * sr))
    return x[a:b]


def wsola(x: np.ndarray, rate: float, sr: int, frame_ms: float = 30.0, tol_ms: float = 10.0) -> np.ndarray:
    """Waveform-similarity overlap-add time-scale modification. rate>1 => faster/shorter."""
    if abs(rate - 1.0) < 1e-3 or len(x) < sr * 0.1:
        return x.astype(np.float32)
    N = int(frame_ms * sr / 1000) // 2 * 2
    Hs = N // 2
    Ha = int(round(Hs * rate))
    tol = int(tol_ms * sr / 1000)
    win = np.hanning(N)
    out_len = int(len(x) / rate) + N
    y = np.zeros(out_len)
    wsum = np.zeros(out_len)
    xp = np.pad(x.astype(np.float64), (tol, N + tol))
    prev = None
    k, a_pos = 0, 0
    while a_pos + N < len(x) and k * Hs + N < out_len:
        c = a_pos + tol
        if prev is None:
            best = c
        else:
            seg = xp[c - tol:c + tol + N]
            corr = np.correlate(seg, prev, mode="valid")
            best = c - tol + int(np.argmax(corr))
        frame = xp[best:best + N]
        y[k * Hs:k * Hs + N] += frame * win
        wsum[k * Hs:k * Hs + N] += win
        prev = xp[best + Hs:best + Hs + N]
        if len(prev) < N:
            break
        k += 1
        a_pos += Ha
    y = y / np.maximum(wsum, 1e-3)
    return y[:int(len(x) / rate)].astype(np.float32)


@dataclass
class Timeline:
    audio: np.ndarray
    sr: int
    spans: list[dict] = field(default_factory=list)  # [{"kind":"speech"|"event"|"pause","t0","t1","text"|"label"}]


def assemble(plan: RenderPlan, synth: Callable[[Segment], tuple[np.ndarray, int]], sr: int = 24000,
             event_lib: Callable[[str], np.ndarray | None] | None = None, max_compress: float = 1.15,
             lead_in: float = 0.15) -> Timeline:
    out = [np.zeros(int(lead_in * sr), np.float32)]
    cur = lead_in
    spans = []
    for seg in plan.segments:
        if seg.t0 is not None and seg.t0 > cur:
            gap = seg.t0 - cur
            out.append(np.zeros(int(round(gap * sr)), np.float32))
            spans.append({"kind": "pause", "t0": round(cur, 3), "t1": round(seg.t0, 3)})
            cur = seg.t0
        if seg.text.strip():
            w, wsr = synth(seg)
            if wsr != sr:
                from rimet2.common.audio import resample
                w = resample(w, wsr, sr)
            w = trim(w, sr)
            if seg.t0 is not None and seg.t1 is not None:
                slot = seg.t1 - max(seg.t0, cur)
                dur = len(w) / sr
                if slot > 0 and dur > slot:
                    w = wsola(w, min(max_compress, dur / slot), sr)
            out.append(w)
            spans.append({"kind": "speech", "t0": round(cur, 3), "t1": round(cur + len(w) / sr, 3), "text": seg.text})
            cur += len(w) / sr
        for ev in seg.events_inline:
            e = event_lib(ev) if event_lib else None
            if e is None:
                continue
            gap = np.zeros(int(0.08 * sr), np.float32)
            out += [gap, e.astype(np.float32)]
            spans.append({"kind": "event", "label": ev.strip("[]"), "t0": round(cur + 0.08, 3),
                          "t1": round(cur + 0.08 + len(e) / sr, 3)})
            cur += 0.08 + len(e) / sr
        if seg.pause_after_ms:
            p = seg.pause_after_ms / 1000
            out.append(np.zeros(int(round(p * sr)), np.float32))
            spans.append({"kind": "pause", "t0": round(cur, 3), "t1": round(cur + p, 3)})
            cur += p
    if plan.target_duration_s and cur < plan.target_duration_s:
        out.append(np.zeros(int((plan.target_duration_s - cur) * sr), np.float32))
    out.append(np.zeros(int(0.15 * sr), np.float32))
    return Timeline(np.concatenate(out), sr, spans)
