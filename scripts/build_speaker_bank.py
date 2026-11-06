"""Build the speaker bank for the speaker prior (diversity) from a metadata CSV of clean clips.

Input CSV columns: speaker_id,path,text,lang,gender[,age_band,region]  (e.g. IndicVoices-R exported rows, or the
cleanest Vaani clip per speaker by DSP SNR). One reference per speaker: the longest clip within 4-12 s.
  python scripts/build_speaker_bank.py --meta data/ivr_hi_ta.csv --out data/bank
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from rimet2.common.audio import load
from rimet2.eval.diversity import get_sv
from rimet2.evidence import pitch
from rimet2.generator.speaker_prior import SpeakerBank, Voice


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--device", default="cuda")
    a = ap.parse_args()
    df = pd.read_csv(a.meta)
    sv = get_sv("wavlm", a.device)
    voices = []
    for spk, g in df.groupby("speaker_id"):
        best = None
        for _, r in g.iterrows():
            x, sr = load(r["path"], sr=16000)
            d = len(x) / sr
            if 4 <= d <= 12 and (best is None or d > best[1]):
                best = (r, d, x)
        if best is None:
            continue
        r, _, x = best
        st = pitch.stats(pitch.yin(x, 16000)[1])
        voices.append(Voice(str(spk), r["path"], str(r.get("text", "") or ""), r["lang"], r.get("gender"),
                            r.get("age_band"), r.get("region"), st.median_hz if st else None,
                            sv.embed([x])[0]))
    bank = SpeakerBank(voices)
    bank.save(a.out + ".jsonl", a.out + ".npy")
    print(len(voices), "speakers ->", a.out)


if __name__ == "__main__":
    main()
