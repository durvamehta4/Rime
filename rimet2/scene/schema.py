"""Scene Score: the shared, claim-level representation between captioner and generator.

A description is a list of atomic Claims. Each claim lives on one PS axis/item type (Appendix F3), optionally has a
time span, a confidence p (captioner side), a provenance `source`, and an optional machine-readable `value`
(e.g. {"f0_median_hz": 185}). Verbalisation turns claims into prose; parsing turns prose into claims + a RenderPlan.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any, Optional

AXES = {
    "Speaker": "voice", "Source": "voice", "Morphology": "voice", "Pitch": "voice", "Timing": "voice", "Event": "voice",
    "Channel": "recording", "Space": "recording", "Other sounds": "recording", "Coupling": "recording",
    "Addressee": "intent", "Subtext": "intent", "Change": "intent",
}
ITEM_TYPES = list(AXES)

# Prior hardness weights per item type (Rime weights items by difficulty; tune from DevReal annotations).
DEFAULT_TYPE_WEIGHT = {
    "Speaker": 1.0, "Source": 2.0, "Morphology": 2.5, "Pitch": 2.0, "Timing": 2.0, "Event": 2.0,
    "Channel": 1.5, "Space": 1.5, "Other sounds": 1.5, "Coupling": 3.0,
    "Addressee": 2.0, "Subtext": 3.0, "Change": 3.0,
}

# Source reliability tiers (used by the Verified Loop filter).
VERIFIED_SOURCES = {"construction", "measurement", "metadata", "human"}


@dataclass
class Claim:
    text: str
    item_type: str
    p: float = 1.0
    t0: Optional[float] = None
    t1: Optional[float] = None
    source: str = "model"  # construction | measurement | metadata | human | omni | llm | model
    value: dict = field(default_factory=dict)
    agree: int = 1  # number of independent sources agreeing

    def __post_init__(self):
        if self.item_type not in AXES:
            raise ValueError(f"unknown item_type {self.item_type!r}")
        if (self.t0 is None) != (self.t1 is None):
            raise ValueError("t0 and t1 must both be set or both None")
        if self.t0 is not None and self.t1 < self.t0:
            raise ValueError("t1 < t0")
        self.p = float(min(max(self.p, 0.0), 1.0))

    @property
    def axis(self) -> str:
        return AXES[self.item_type]

    @property
    def timed(self) -> bool:
        return self.t0 is not None

    @property
    def verified(self) -> bool:
        return self.source in VERIFIED_SOURCES or self.agree >= 2

    def weight(self, table: dict | None = None) -> float:
        return (table or DEFAULT_TYPE_WEIGHT)[self.item_type]


@dataclass
class SceneScore:
    lang: str
    duration_s: float
    claims: list[Claim] = field(default_factory=list)
    transcript: str = ""
    meta: dict = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=1)

    @classmethod
    def from_json(cls, s: str | dict) -> "SceneScore":
        d = json.loads(s) if isinstance(s, str) else s
        claims = [Claim(**c) for c in d.get("claims", [])]
        return cls(lang=d["lang"], duration_s=float(d["duration_s"]), claims=claims,
                   transcript=d.get("transcript", ""), meta=d.get("meta", {}))

    def by_type(self, item_type: str) -> list[Claim]:
        return [c for c in self.claims if c.item_type == item_type]

    def verified_only(self) -> "SceneScore":
        return SceneScore(self.lang, self.duration_s, [c for c in self.claims if c.verified], self.transcript,
                          dict(self.meta))


# ---------------- generator-side plan ----------------
@dataclass
class Segment:
    text: str  # native-script words to say in this segment ("" for pure non-verbal)
    t0: Optional[float] = None  # requested start (s); None = as soon as previous ends
    t1: Optional[float] = None
    style: str = ""  # voice-side instruction for this segment (pace, phonation, loudness, emotion...)
    pause_after_ms: int = 0
    events_inline: list[str] = field(default_factory=list)  # e.g. ["[laugh]"] appended after the words


@dataclass
class EnvEvent:
    label: str  # free text, e.g. "pressure cooker whistle"
    t0: float
    t1: float
    level_db_rel_speech: float = -10.0
    query: str = ""  # retrieval query for the Foley library


@dataclass
class Ecology:
    channel: str = "clean"  # clean | phone_narrowband | voip | laptop | ...
    codec: str = ""  # g711 | gsm | opus | g722 | ""
    clipping: float = 0.0  # 0..1 severity
    space: str = "dry"  # dry | small_room | medium_room | large_hall | bathroom | outdoor
    rt60_s: Optional[float] = None
    background: str = ""  # stationary bed description
    snr_db: Optional[float] = None
    events: list[EnvEvent] = field(default_factory=list)


@dataclass
class RenderPlan:
    lang: str
    speaker: dict = field(default_factory=dict)  # gender, age_band, region, f0_hz, timbre
    global_style: str = ""
    segments: list[Segment] = field(default_factory=list)
    ecology: Ecology = field(default_factory=Ecology)
    coupling: list[dict] = field(default_factory=list)  # [{"t0":7.0,"effect":"louder_brighter","gain_db":6}]
    target_duration_s: Optional[float] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=1)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "RenderPlan":
        eco = d.get("ecology", {}) or {}
        eco_events = [EnvEvent(**e) for e in eco.get("events", [])]
        eco = Ecology(**{**{k: v for k, v in eco.items() if k != "events"}, "events": eco_events})
        segs = [Segment(**s) for s in d.get("segments", [])]
        return cls(lang=d.get("lang", "hi"), speaker=d.get("speaker", {}) or {}, global_style=d.get("global_style", ""),
                   segments=segs, ecology=eco, coupling=d.get("coupling", []) or [],
                   target_duration_s=d.get("target_duration_s"))
