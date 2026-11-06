"""Ecology renderer: dry voice + Ecology spec -> audio + EXACT labels (Claims with source="construction").

Order: coupling gain on speech -> room (RIR) -> background bed at SNR (on active speech) -> timed events
       -> channel (band/codec/clipping/loss).
Salience gate: a constructed label is emitted only if the thing is audible enough (achieved SNR / event level),
otherwise it would become a false claim for the captioner (the rubric penalises those).
"""
from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from rimet2.common.audio import load
from rimet2.evidence.dsp import energy_vad
from rimet2.scene.schema import Claim, Ecology

from . import channel as ch
from . import mix, rir

SPACE_WORDS = [  # (max rt60, phrase)
    (0.2, "A dry, close-miked sound with almost no room reverberation"),
    (0.45, "A small room: short reflections colour the voice slightly"),
    (0.8, "A reflective room with clearly audible reverberation"),
    (10.0, "A large, echoing space with a long reverberant tail"),
]
CHANNEL_WORDS = {
    "phone_narrowband": "A narrowband phone line: the voice is band-limited to about 300–3400 Hz with codec artefacts",
    "landline": "A narrowband telephone channel, band-limited to about 300–3400 Hz",
    "voip": "A voice-call channel with mild codec smoothing",
    "voip_poor": "A poor internet call: narrow bandwidth, codec smearing and brief dropouts",
    "laptop": "A laptop-style microphone with slightly thin low end",
}


@dataclass
class FoleyLibrary:
    """CSV with columns: path,label,licence[,source]. Labels are free text (e.g. 'pressure cooker whistle')."""
    rows: list[dict] = field(default_factory=list)
    sr: int = 24000

    @classmethod
    def from_csv(cls, path: str | Path | None, sr: int = 24000) -> "FoleyLibrary":
        if not path or not Path(path).exists():
            return cls([], sr)
        with open(path, newline="", encoding="utf-8") as f:
            return cls(list(csv.DictReader(f)), sr)

    def find(self, query: str, rng: np.random.Generator):
        q = set(query.lower().split())
        scored = [(len(q & set(r["label"].lower().split())), i) for i, r in enumerate(self.rows)]
        scored = [s for s in scored if s[0] > 0]
        if not scored:
            return None
        best = max(s[0] for s in scored)
        cands = [i for s, i in scored if s == best]
        r = self.rows[cands[rng.integers(len(cands))]]
        x, _ = load(r["path"], sr=self.sr)
        return x, r


def _synthetic_noise(kind: str, n: int, sr: int, rng: np.random.Generator) -> np.ndarray:
    """Fallback beds when no library is available (also used in tests): white/pink/hum."""
    if "hum" in kind or "fan" in kind:
        t = np.arange(n) / sr
        return (np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 100 * t) + 0.05 * rng.standard_normal(n)
                ).astype(np.float32)
    w = rng.standard_normal(n)
    if "pink" in kind or "rumble" in kind or "traffic" in kind:
        f = np.fft.rfft(w)
        f /= np.sqrt(np.arange(1, len(f) + 1))
        w = np.fft.irfft(f, n)
    return (w / (np.std(w) + 1e-9)).astype(np.float32)


class EcologyRenderer:
    def __init__(self, sr: int = 24000, foley: FoleyLibrary | None = None, noise_beds: FoleyLibrary | None = None,
                 rir_bank: rir.RIRBank | None = None, min_event_db: float = -12.0, min_bed_snr_for_quiet: float = 35):
        self.sr = sr
        self.foley = foley or FoleyLibrary([], sr)
        self.beds = noise_beds or FoleyLibrary([], sr)
        self.rir_bank = rir_bank
        self.min_event_db = min_event_db
        self.quiet_snr = min_bed_snr_for_quiet

    def render(self, voice: np.ndarray, eco: Ecology, coupling: list[dict] | None = None, seed: int = 0
               ) -> tuple[np.ndarray, list[Claim], dict]:
        rng = np.random.default_rng(seed)
        sr = self.sr
        y = voice.astype(np.float32).copy()
        segs = energy_vad(y, sr)
        claims: list[Claim] = []
        log: dict = {"steps": []}
        dur = len(y) / sr
        # 1) coupling: voice gets louder after an onset (Lombard-like level change only; brightness must come
        #    from the voice model's style instruction, so we only label the level change we actually applied)
        for c in coupling or []:
            g = float(c.get("gain_db", 0))
            if g:
                k = int(c["t0"] * sr)
                y[k:] *= 10 ** (g / 20)
                claims.append(Claim(f"From about {c['t0']:.1f} s the voice gets louder by roughly {g:.0f} dB in "
                                    f"response to the noise", "Coupling", p=1.0, t0=float(c["t0"]), t1=round(dur, 2),
                                    source="construction", value={"coupling_gain_db": g}))
                log["steps"].append({"coupling": c})
        ref_power = mix.active_power(y, sr, segs)
        # 2) room
        if eco.space and eco.space != "dry" or eco.rt60_s:
            r, info = rir.make_rir(eco.space or "small_room", sr, rng, eco.rt60_s, self.rir_bank)
            y = rir.apply_rir(y, r)
            log["steps"].append({"room": info})
            rt = info["rt60_s"]
            phrase = next(p for m, p in SPACE_WORDS if rt <= m)
            claims.append(Claim(phrase, "Space", p=1.0, source="construction",
                                value={"rt60_s": rt, "c50_db": info["c50_db"]}))
        elif eco.space == "dry":
            claims.append(Claim(SPACE_WORDS[0][1], "Space", p=1.0, source="construction", value={"rt60_s": 0.0}))
        # 3) background bed
        if eco.background or eco.snr_db is not None:
            snr = eco.snr_db if eco.snr_db is not None else float(rng.uniform(5, 25))
            hit = self.beds.find(eco.background, rng) if eco.background else None
            noise = hit[0] if hit else _synthetic_noise(eco.background or "pink", len(y), sr, rng)
            y, info = mix.add_bed(y, sr, noise, snr, rng, segs)
            info["bed"] = hit[1]["label"] if hit else (eco.background or "pink noise")
            log["steps"].append({"bed": info})
            a = info["bed_snr_db"]
            label = info["bed"]
            if a >= self.quiet_snr:
                claims.append(Claim("The background is quiet; the noise floor sits far below the voice",
                                    "Other sounds", p=1.0, source="construction", value={"snr_db": a}))
            elif a <= 10:
                claims.append(Claim(f"A loud, steady {label} runs throughout, only about {a:.0f} dB below the voice",
                                    "Other sounds", p=1.0, source="construction", value={"snr_db": a, "bed": label}))
            elif a <= 25:
                claims.append(Claim(f"A steady {label} is audible throughout, well below the voice",
                                    "Other sounds", p=1.0, source="construction", value={"snr_db": a, "bed": label}))
        # 4) timed events
        for e in eco.events:
            hit = self.foley.find(e.query or e.label, rng)
            if hit is None:
                log["steps"].append({"event_missing": e.label})
                continue
            y, info = mix.place_event(y, sr, hit[0], e.t0, e.level_db_rel_speech, ref_power, t1=e.t1)
            log["steps"].append({"event": {**info, "label": e.label, "file": hit[1].get("path")}})
            if info and e.level_db_rel_speech >= self.min_event_db:
                claims.append(Claim(f"{e.label[0].upper() + e.label[1:]}", "Other sounds", p=1.0, t0=info["t0"],
                                    t1=info["t1"], source="construction", value={"event": e.label.lower()}))
        # 5) channel
        preset = eco.channel or "clean"
        if preset != "clean" or eco.codec or eco.clipping > 0:
            y, info = ch.apply_channel(y, sr, preset if preset in ch.CHANNEL_PRESETS else "clean",
                                       codec=eco.codec or None, clip_drive_db=12 * eco.clipping, rng=rng)
            log["steps"].append({"channel": info})
            if preset in CHANNEL_WORDS:
                claims.append(Claim(CHANNEL_WORDS[preset], "Channel", p=1.0, source="construction",
                                    value={"channel": "narrowband" if "band_hz" in info and info["band_hz"][1] <= 4000
                                           else preset}))
            if eco.clipping > 0.3:
                claims.append(Claim("The loudest syllables are clipped, adding a harsh distortion", "Channel", p=1.0,
                                    source="construction", value={"clipping": True}))
        peak = float(np.max(np.abs(y)) + 1e-9)
        if peak > 0.99:
            y = y / peak * 0.95
        return y.astype(np.float32), claims, log


def labels_json(claims: list[Claim]) -> str:
    return json.dumps([c.__dict__ for c in claims], ensure_ascii=False)
