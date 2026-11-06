"""Training-example manifest. The PS requires one manifest recording the source and labeler of every example.

Every row is one (audio, text, description) training example for either model.
"""
from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path
from typing import Iterable

COLUMNS = [
    "example_id", "model", "round", "split", "lang", "audio_path", "audio_sha256", "duration_s",
    "source_dataset", "source_id", "licence", "speaker_id",
    "text", "text_labeler", "description", "description_labeler",
    "transform_chain", "verified_claims", "dropped_claims", "notes",
]


@dataclass
class ManifestRow:
    example_id: str
    model: str  # "captioner" | "generator" | "both"
    round: int
    split: str  # train | dev | test
    lang: str  # hi | ta
    audio_path: str
    audio_sha256: str
    duration_s: float
    source_dataset: str  # vaani | indicvoices_r | rasa | synthetic_g{r} | transform
    source_id: str
    licence: str
    speaker_id: str = ""
    text: str = ""
    text_labeler: str = ""  # vaani_transcript | indicconformer@conf | human
    description: str = ""
    description_labeler: str = ""  # e.g. "evidence_v1+omni_r0+fuser_r1" | "construction" | "human"
    transform_chain: str = "[]"  # JSON list of applied transforms with parameters
    verified_claims: int = 0
    dropped_claims: int = 0
    notes: str = ""


class ManifestWriter:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        new = not self.path.exists()
        self._f = open(self.path, "a", newline="", encoding="utf-8")
        self._w = csv.DictWriter(self._f, fieldnames=COLUMNS)
        if new:
            self._w.writeheader()

    def write(self, row: ManifestRow) -> None:
        d = asdict(row)
        if not isinstance(d["transform_chain"], str):
            d["transform_chain"] = json.dumps(d["transform_chain"], ensure_ascii=False)
        self._w.writerow(d)

    def write_many(self, rows: Iterable[ManifestRow]) -> None:
        for r in rows:
            self.write(r)

    def close(self) -> None:
        self._f.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


def read_manifest(path: str | Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


assert [f.name for f in fields(ManifestRow)] == COLUMNS
