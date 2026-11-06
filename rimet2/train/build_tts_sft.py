"""Build generator SFT data (language adaptation + instruction following) from manifests.

Output JSONL rows in the official Qwen3-TTS finetuning format {"audio", "text", "ref_audio"} plus our extra
fields {"instruct", "lang", "speaker_id", "example_id"}. `ref_audio` is ANOTHER clip of the same speaker
(multi-speaker cloning objective). `instruct` is the DRY voice-axis description (ecology is the renderer's job)
built only from verified claims.

  python -m rimet2.train.build_tts_sft --manifest runs/r1/manifest.csv --out runs/r1/tts_sft.jsonl
"""
from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict

from rimet2.common.manifest import read_manifest
from rimet2.scene.schema import SceneScore
from rimet2.scene.verbalize import verbalize

VOICE_TYPES = {"Speaker", "Source", "Morphology", "Pitch", "Timing", "Event"}


def dry_instruct(scene_json: str) -> str:
    s = SceneScore.from_json(scene_json)
    s.claims = [c for c in s.claims if c.item_type in VOICE_TYPES and c.verified]
    for c in s.claims:
        c.p = 1.0
    txt = verbalize(s, tau=0.0)
    return txt.split("\n\n", 1)[1] if "\n\n" in txt else ""


def build(rows: list[dict], scenes: dict[str, str], seed: int = 0, min_dur: float = 1.5, max_dur: float = 20.0):
    rng = random.Random(seed)
    by_spk = defaultdict(list)
    for r in rows:
        if r["model"] not in ("generator", "both") or not r["text"]:
            continue
        if not (min_dur <= float(r["duration_s"]) <= max_dur):
            continue
        by_spk[(r["lang"], r["speaker_id"])].append(r)
    out = []
    for (_, spk), rs in by_spk.items():
        for r in rs:
            others = [o for o in rs if o["example_id"] != r["example_id"]]
            ref = rng.choice(others)["audio_path"] if others else r["audio_path"]
            out.append({"audio": r["audio_path"], "text": r["text"], "ref_audio": ref,
                        "instruct": dry_instruct(scenes[r["example_id"]]) if r["example_id"] in scenes else "",
                        "lang": r["lang"], "speaker_id": spk, "example_id": r["example_id"]})
    rng.shuffle(out)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--scenes", default="", help="jsonl {example_id, scene}")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    scenes = {}
    if a.scenes:
        for line in open(a.scenes, encoding="utf-8"):
            d = json.loads(line)
            scenes[d["example_id"]] = json.dumps(d["scene"], ensure_ascii=False)
    rows = build(read_manifest(a.manifest), scenes)
    with open(a.out, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(len(rows), "rows ->", a.out)


if __name__ == "__main__":
    main()
