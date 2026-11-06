"""E2: can the Qwen3-TTS 12 Hz tokenizer represent Hindi/Tamil? Round-trip N clips, compare CER and SV vs original.
Decision gate for the generator backbone: if Delta-CER (resynth - original) > ~5 points absolute on clean clips,
prefer the Indic-Parler-TTS voice backend.

  python scripts/codec_ceiling.py --list data/hi_dev.list --n 200 --tokenizer models/Qwen3-TTS-Tokenizer-12Hz
List lines: clip_id<TAB>path<TAB>lang. Uses Vaani transcripts? No: compares ASR(original) vs ASR(resynth) so the
measure isolates codec damage (no reference text needed).
"""
from __future__ import annotations

import argparse
import tempfile

import numpy as np

from rimet2.common.audio import load, resample, save
from rimet2.common.ledger import gpu_job
from rimet2.eval.cer import IndicConformerASR, cer
from rimet2.eval.diversity import cosine_matrix, get_sv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", required=True)
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--tokenizer", default="models/Qwen3-TTS-Tokenizer-12Hz")
    ap.add_argument("--device", default="cuda:0")
    a = ap.parse_args()
    from qwen_tts import Qwen3TTSTokenizer

    rows = [l.split("\t") for l in open(a.list).read().splitlines()][:a.n]
    tok = Qwen3TTSTokenizer.from_pretrained(a.tokenizer, device_map=a.device)
    asr = IndicConformerASR(device=a.device.split(":")[0])
    sv = get_sv("wavlm", a.device)
    cers, sims = [], []
    with gpu_job("e2/codec_ceiling", n_gpus=1), tempfile.TemporaryDirectory() as d:
        for cid, path, lang in rows:
            x, sr = load(path, sr=24000)
            p24 = f"{d}/{cid}.wav"
            save(p24, x, 24000)
            wavs, osr = tok.decode(tok.encode(p24))
            y = np.asarray(wavs[0], dtype=np.float32).reshape(-1)
            x16, y16 = resample(x, 24000, 16000), resample(y, osr, 16000)
            h0, h1 = asr(x16, lang), asr(y16, lang)
            cers.append(cer(h0, h1, lang))  # disagreement between ASR(original) and ASR(resynth)
            e = sv.embed([x16, y16])
            sims.append(float(cosine_matrix(e)[0, 1]))
    print(f"n={len(cers)}  mean CER(orig-ASR vs resynth-ASR)={np.mean(cers):.3f}  "
          f"median={np.median(cers):.3f}  SV cos mean={np.mean(sims):.3f}  frac>=0.86={np.mean(np.array(sims) >= .86):.2f}")


if __name__ == "__main__":
    main()
