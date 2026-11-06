"""Captioner CLI: audio (<=30 s) -> English description.

Modes (all comparable on the same dev set = the controlled comparison for the captioner):
  raw       round 0: first Omni sample verbatim
  evidence  evidence toolkit only (measurement claims, verbalised)
  fused     evidence + K Omni samples -> claims -> self-consistency -> fusion -> calibration -> tau -> verbalise

  python -m rimet2.captioner.cli --list clips.txt --lang hi --mode fused --k 5 --out runs/r1/captions.jsonl
clips.txt: one path per line, or "clip_id<TAB>path<TAB>lang".
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rimet2.common.ledger import gpu_job
from rimet2.common.llm import openai_chat
from rimet2.evidence.run import scene_from_audio
from rimet2.scene.verbalize import verbalize

from .calibrate import IsotonicCalibrator
from .claims import self_consistency, split_caption
from .fuse import fuse


def read_list(path: str, default_lang: str) -> list[tuple[str, str, str]]:
    rows = []
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) == 1:
            rows.append((Path(parts[0]).stem, parts[0], default_lang))
        else:
            rows.append((parts[0], parts[1], parts[2] if len(parts) > 2 else default_lang))
    return rows


def describe(clip_path: str, lang: str, omni_texts: list[str] | None, mode: str, llm=None, calibrator=None,
             tau: float = 0.5, neural: bool = True, device: str = "cuda", pitch_backend: str = "yin") -> dict:
    if mode == "raw":
        return {"description": (omni_texts or [""])[0], "scene": None}
    scene, ev = scene_from_audio(clip_path, lang, neural=neural, device=device, pitch_backend=pitch_backend)
    if mode == "evidence":
        fused = scene
    else:
        samples = [split_caption(llm, t) for t in (omni_texts or [])]
        model_claims = self_consistency(samples) if samples else []
        fused = fuse(scene.claims, model_claims, lang, scene.duration_s, calibrator=calibrator)
    return {"description": verbalize(fused, tau=tau), "scene": json.loads(fused.to_json())}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", required=True)
    ap.add_argument("--lang", default="hi")
    ap.add_argument("--mode", choices=["raw", "evidence", "fused"], default="fused")
    ap.add_argument("--k", type=int, default=5, help="Omni samples per clip (self-consistency)")
    ap.add_argument("--omni-backend", default="vllm")
    ap.add_argument("--omni-cache", default="", help="jsonl of {clip_id, omni:[...]} to reuse captions")
    ap.add_argument("--calibrator", default="")
    ap.add_argument("--tau", type=float, default=0.5)
    ap.add_argument("--no-neural", action="store_true")
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--pitch-backend", default="yin")
    ap.add_argument("--out", required=True)
    ap.add_argument("--round", default="")
    a = ap.parse_args(argv)

    rows = read_list(a.list, a.lang)
    cache = {}
    if a.omni_cache and Path(a.omni_cache).exists():
        for line in open(a.omni_cache, encoding="utf-8"):
            d = json.loads(line)
            cache[d["clip_id"]] = d["omni"]
    need = [r for r in rows if r[0] not in cache] if a.mode != "evidence" else []
    if need:
        from .omni_raw import get_captioner
        with gpu_job(f"captioner/omni_{a.mode}", round_=a.round):
            cap = get_captioner(a.omni_backend)
            # always draw k seeded samples so raw (uses sample 0) and fused (uses all k) share one cache
            texts = cap.caption([r[1] for r in need], n=a.k)
        Path(a.omni_cache or a.out + ".omni.jsonl").parent.mkdir(parents=True, exist_ok=True)
        with open(a.omni_cache or a.out + ".omni.jsonl", "a", encoding="utf-8") as f:
            for r, t in zip(need, texts):
                cache[r[0]] = t
                f.write(json.dumps({"clip_id": r[0], "omni": t}, ensure_ascii=False) + "\n")
        del cap
    llm = openai_chat() if a.mode == "fused" else None
    cal = IsotonicCalibrator.load(a.calibrator) if a.calibrator else None
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with gpu_job(f"captioner/{a.mode}_post", round_=a.round), open(a.out, "w", encoding="utf-8") as f:
        for cid, path, lang in rows:
            res = describe(path, lang, cache.get(cid), a.mode, llm, cal, a.tau, not a.no_neural, a.device,
                           a.pitch_backend)
            f.write(json.dumps({"clip_id": cid, "lang": lang, "mode": a.mode, **res}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
