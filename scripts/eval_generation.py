"""Score generator outputs on the automatic measures (PS Track 2 generation part, internal proxies).

  python scripts/eval_generation.py --gens runs/r0/gen_round0_hi/generations.jsonl --items data/gen_items_hi.csv \
      [--relevance --captions runs/r0/gencap_hi.jsonl] --round 0 --results results.csv

- intelligibility: IndicConformer CER vs the native-script text (points = 1 - CER)
- diversity: distinct speakers among the 10 samples (WavLM-SV 0.86; ECAPA 0.25 with --ecapa), counted over samples
  that pass the relevance proxy when --relevance is given (as in the PS), else over all samples (upper bound)
- relevance proxy (optional): atomic statements checked by evidence + captioner-as-judge
- naturalness proxy: UTMOSv2 (relative only)
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from rimet2.common.audio import load
from rimet2.common.bootstrap import bootstrap_ci
from rimet2.eval import results
from rimet2.eval.cer import IndicConformerASR, cer
from rimet2.eval.diversity import THRESHOLDS, count_distinct, diversity_points, get_sv
from rimet2.eval.naturalness import utmos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gens", required=True)
    ap.add_argument("--items", required=True)
    ap.add_argument("--round", default="0")
    ap.add_argument("--results", default="results.csv")
    ap.add_argument("--relevance", action="store_true")
    ap.add_argument("--captions", default="", help="jsonl {path, description} from our captioner on the outputs")
    ap.add_argument("--rel-threshold", type=float, default=0.5, help="share of statements met to 'pass'")
    ap.add_argument("--ecapa", action="store_true")
    ap.add_argument("--utmos", action="store_true")
    ap.add_argument("--seed", type=int, default=20261104)
    ap.add_argument("--device", default="cuda")
    a = ap.parse_args()
    items = {r["item_id"]: r for r in csv.DictReader(open(a.items, encoding="utf-8"))}
    gens = defaultdict(list)
    system = None
    for l in open(a.gens, encoding="utf-8"):
        d = json.loads(l)
        gens[d["item_id"]].append(d)
        system = d.get("system", Path(a.gens).parent.name)
    asr = IndicConformerASR(device=a.device)
    svs = {"wavlm": get_sv("wavlm", a.device)}
    if a.ecapa:
        svs["ecapa"] = get_sv("ecapa", a.device)
    caps = {}
    if a.relevance:
        from rimet2.common.llm import openai_chat
        from rimet2.eval.gen_relevance import relevance
        from rimet2.evidence.run import scene_from_audio
        llm = openai_chat()
        for l in open(a.captions, encoding="utf-8"):
            d = json.loads(l)
            caps[d["path"]] = d["description"]
    per_item = {}
    lang = None
    for iid, gs in gens.items():
        it = items[iid]
        lang = it["lang"]
        wavs, cers, rel, ut = [], [], [], []
        for g in sorted(gs, key=lambda g: g["k"]):
            x, _ = load(g["path"], sr=16000)
            wavs.append(x)
            cers.append(cer(it["text"], asr(x, lang), lang))
            if a.relevance:
                sc, _ = scene_from_audio(g["path"], lang, neural=True)
                share, _ = relevance(llm, it["description"], sc.claims, caps.get(g["path"], ""))
                rel.append(share)
            if a.utmos:
                ut.append(utmos(g["path"]))
        passed = [i for i in range(len(wavs)) if not a.relevance or rel[i] >= a.rel_threshold]
        div = {}
        for name, sv in svs.items():
            emb = sv.embed([wavs[i] for i in passed]) if passed else np.zeros((0, 1))
            div[name] = count_distinct(emb, THRESHOLDS[name]) if passed else 0
        per_item[iid] = {"cer": float(np.mean(cers)), "rel": float(np.mean(rel)) if rel else None, **{
            f"div_{k}": v for k, v in div.items()}, "utmos": float(np.nanmean([u for u in ut if u is not None]))
            if ut else None}
    ids = sorted(per_item)
    rows = []

    def add(measure, key, transform=lambda v: v):
        vals = [per_item[i][key] for i in ids if per_item[i][key] is not None]
        if not vals:
            return
        pt, lo, hi = bootstrap_ci([i for i in ids if per_item[i][key] is not None],
                                  lambda xs: float(np.mean([per_item[i][key] for i in xs])), a.seed,
                                  f"gen/{system}/{measure}")
        print(f"{system:<10} {measure:<22} {pt:.3f} [{lo:.3f}, {hi:.3f}]  -> points {transform(pt):.3f}")
        rows.append({"round": a.round, "model": "generator", "system": system, "lang": lang, "measure": measure,
                     "value": f"{pt:.4f}", "ci_low": f"{lo:.4f}", "ci_high": f"{hi:.4f}", "n_items": len(vals)})

    add("cer_indicconformer", "cer", lambda v: max(0.0, 1 - v))
    for name in svs:
        add(f"distinct_speakers_{name}", f"div_{name}", lambda v: diversity_points([v]))
    add("relevance_proxy", "rel", lambda v: 5 * v)
    add("utmos_proxy", "utmos")
    results.append(a.results, rows)


if __name__ == "__main__":
    main()
