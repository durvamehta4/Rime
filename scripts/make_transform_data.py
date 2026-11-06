"""Round step 3: weak-area-targeted, known-by-construction captioner training data (+ manifest rows).

  python scripts/make_transform_data.py --clean data/wav/hi_clean --lang hi --n 3000 \
      --breakdown runs/r0/type_scores_hi.json --out runs/r1/synth_hi --round 1 --foley data/foley.csv
--clean : directory of CLEAN real clips (high SNR, wideband, dry; select with data/wav/*/dsp.csv)
--breakdown : {"item_type": F_k} from scripts/eval_captions.py (per-type scores on held-out REAL dev audio)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from rimet2.common.audio import load, save, sha256_file
from rimet2.common.manifest import ManifestRow, ManifestWriter
from rimet2.evidence.run import scene_from_audio
from rimet2.renderer.render import EcologyRenderer, FoleyLibrary
from rimet2.renderer.rir import RIRBank
from rimet2.scene.verbalize import verbalize
from rimet2.train.targeted import allocate, transform_example


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clean", required=True)
    ap.add_argument("--lang", default="hi")
    ap.add_argument("--n", type=int, default=2000)
    ap.add_argument("--breakdown", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--round", type=int, default=1)
    ap.add_argument("--foley", default="")
    ap.add_argument("--beds", default="")
    ap.add_argument("--rirs", default="")
    ap.add_argument("--seed", type=int, default=1234)
    a = ap.parse_args()
    sr = 24000
    rng = np.random.default_rng(a.seed)
    clips = sorted(Path(a.clean).glob("*.wav"))
    foley = FoleyLibrary.from_csv(a.foley, sr)
    R = EcologyRenderer(sr, foley, FoleyLibrary.from_csv(a.beds, sr), RIRBank(a.rirs, sr) if a.rirs else None)
    labels = sorted({r["label"] for r in foley.rows}) or None
    F = json.load(open(a.breakdown)) if a.breakdown else {t: 0.5 for t in ("Channel", "Space", "Other sounds",
                                                                           "Coupling", "Event")}
    eco_F = {t: f for t, f in F.items() if t in ("Channel", "Space", "Other sounds", "Coupling", "Event")}
    plan = allocate(eco_F, a.n)
    print("budget per focus type:", plan)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    mw = ManifestWriter(out / "manifest.csv")
    k = 0
    for focus, n in plan.items():
        for _ in range(n):
            src = clips[int(rng.integers(len(clips)))]
            x, _ = load(src, sr=sr)
            base, _ = scene_from_audio(str(src), a.lang, neural=True)
            y, sc, log = transform_example(x, sr, base, R, rng, focus=focus, event_labels=labels, seed=a.seed + k)
            p = out / f"{a.lang}_r{a.round}_{k:06d}.wav"
            save(p, y, sr)
            desc = verbalize(sc, tau=0.0)
            with open(out / "scenes.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({"example_id": p.stem, "scene": json.loads(sc.to_json()), "description": desc},
                                   ensure_ascii=False, default=float) + "\n")
            mw.write(ManifestRow(p.stem, "captioner", a.round, "train", a.lang, str(p), sha256_file(p),
                                 round(len(y) / sr, 3), "transform", src.stem, "derived: see source licence",
                                 description=desc, description_labeler="evidence_v1(verified)+construction",
                                 transform_chain=json.dumps(log, default=float), verified_claims=len(sc.claims),
                                 notes=f"focus={focus}"))
            k += 1
    mw.close()
    print(k, "examples ->", out)


if __name__ == "__main__":
    main()
