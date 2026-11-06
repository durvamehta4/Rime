"""Validate and package the Track-2 contributed test set (mid-term, 5 points).

Expected source layout (one per language, lang in {hi, ta}):
  testset_src/<lang>/clips/<clip_id>.wav                 30 clips, <=30 s, mono, >=16 kHz, >=16-bit
  testset_src/<lang>/clips.csv     clip_id,speaker_id,notes   (notes: what was staged; kept in answers/ only)
  testset_src/<lang>/descriptions.csv  desc_id,text,description  (30 rows, text in native script, <=300 words)
Output zip layout (confirm with organisers on Discord; easy to change here):
  <lang>/captioner/inputs/<clip_id>.wav
  <lang>/captioner/answers/clip_metadata.csv
  <lang>/generator/inputs/descriptions.csv
Consent forms are NEVER packaged (PS: keep them, show on request).

  python -m rimet2.testset.package --src testset_src --out test_set.zip --team TEAMID
"""
from __future__ import annotations

import argparse
import csv
import re
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path

import soundfile as sf

from .lint_descriptions import lint

ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")
SCRIPT = {"hi": ("DEVANAGARI",), "ta": ("TAMIL",)}


def script_share(text: str, lang: str) -> float:
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0.0
    ok = sum(any(s in unicodedata.name(c, "") for s in SCRIPT[lang]) for c in letters)
    return ok / len(letters)


def check_lang(src: Path, lang: str, n_expected: int = 30) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    d = src / lang
    clips = sorted((d / "clips").glob("*.wav"))
    if len(clips) != n_expected:
        errors.append(f"[{lang}] expected {n_expected} clips, found {len(clips)}")
    meta = {r["clip_id"]: r for r in csv.DictReader(open(d / "clips.csv", encoding="utf-8"))} \
        if (d / "clips.csv").exists() else {}
    if not meta:
        errors.append(f"[{lang}] clips.csv missing or empty")
    spk = Counter()
    for p in clips:
        cid = p.stem
        if not ID_RE.match(cid):
            errors.append(f"[{lang}] bad clip id {cid!r} (ASCII letters/digits . _ - only)")
        info = sf.info(str(p))
        if info.channels != 1:
            errors.append(f"[{lang}] {cid}: not mono")
        if info.samplerate < 16000:
            errors.append(f"[{lang}] {cid}: sample rate {info.samplerate} < 16 kHz")
        if info.subtype not in ("PCM_16", "PCM_24", "PCM_32", "FLOAT", "DOUBLE"):
            errors.append(f"[{lang}] {cid}: subtype {info.subtype} not >=16-bit PCM")
        if info.duration > 30.0:
            errors.append(f"[{lang}] {cid}: {info.duration:.1f} s > 30 s")
        if info.duration < 2.0:
            warns.append(f"[{lang}] {cid}: very short ({info.duration:.1f} s)")
        if cid not in meta:
            errors.append(f"[{lang}] {cid}: missing in clips.csv")
        else:
            spk[meta[cid]["speaker_id"]] += 1
    for s, c in spk.items():
        if c > 5:
            errors.append(f"[{lang}] speaker {s} has {c} clips (max 5)")
    if len(spk) < 6:
        errors.append(f"[{lang}] only {len(spk)} speakers; need >= 6 (aim for 10+)")
    descs = list(csv.DictReader(open(d / "descriptions.csv", encoding="utf-8"))) if (d / "descriptions.csv").exists() \
        else []
    if len(descs) != n_expected:
        errors.append(f"[{lang}] expected {n_expected} descriptions, found {len(descs)}")
    for r in descs:
        if not ID_RE.match(r["desc_id"]):
            errors.append(f"[{lang}] bad desc id {r['desc_id']!r}")
        n = len(r["description"].split())
        if n > 300:
            errors.append(f"[{lang}] {r['desc_id']}: description has {n} words (>300)")
        sh = script_share(r["text"], lang)
        if sh < 0.7:
            warns.append(f"[{lang}] {r['desc_id']}: text only {sh:.0%} native script (English words in Latin are ok)")
        for w in lint(r["description"]):
            warns.append(f"[{lang}] {r['desc_id']}: {w}")
    return errors, warns


def package(src: Path, out: Path, langs=("hi", "ta")) -> None:
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for lang in langs:
            d = src / lang
            for p in sorted((d / "clips").glob("*.wav")):
                z.write(p, f"{lang}/captioner/inputs/{p.name}")
            z.write(d / "clips.csv", f"{lang}/captioner/answers/clip_metadata.csv")
            z.write(d / "descriptions.csv", f"{lang}/generator/inputs/descriptions.csv")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", default="test_set.zip")
    ap.add_argument("--langs", default="hi,ta")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args(argv)
    src = Path(a.src)
    all_err, all_warn = [], []
    for lang in a.langs.split(","):
        e, w = check_lang(src, lang)
        all_err += e
        all_warn += w
    for w in all_warn:
        print("WARN ", w)
    for e in all_err:
        print("ERROR", e)
    if all_err and not a.force:
        raise SystemExit(f"{len(all_err)} errors; fix them (or --force)")
    package(src, Path(a.out), a.langs.split(","))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
