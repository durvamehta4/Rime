#!/usr/bin/env bash
# Generator language adaptation (Hindi + Tamil) of Qwen3-TTS-12Hz-1.7B-Base with the OFFICIAL fine-tuning code.
# Status: VERIFY ON SERVER. The official script is documented as single-speaker SFT with JSONL fields
# {audio, text, ref_audio}; our rows carry a per-row same-speaker ref_audio, which is how we get multi-speaker
# adaptation through it. Instruction (`instruct`) conditioning on Base is NOT in the official script: that is the
# post-mid-term extension (train/build_tts_sft.py already writes the field).
#   bash scripts/qwen3tts_language_adapt.sh runs/r1/tts_sft.jsonl ckpt/qwen3tts_hi_ta_r1
set -euo pipefail
DATA=${1:?jsonl}; OUT=${2:?outdir}
MODELS=${MODELS:-$HOME/Vaani/models}
[ -d third_party/Qwen3-TTS ] || git clone --depth 1 https://github.com/QwenLM/Qwen3-TTS third_party/Qwen3-TTS
ls third_party/Qwen3-TTS/finetuning/
echo ">>> Read third_party/Qwen3-TTS/finetuning/README* and adjust the flags below to match the script's CLI."
# Official example settings (from the research notes): lr 2e-6, batch 32. On 4xL4 use grad accumulation.
python - <<'PY'
from rimet2.common.ledger import gpu_job
import subprocess, os, sys
cmd = os.environ.get("SFT_CMD")
if not cmd:
    sys.exit("Set SFT_CMD to the exact official command (e.g. torchrun --nproc_per_node 4 "
             "third_party/Qwen3-TTS/finetuning/sft_12hz.py ...) after reading its README.")
with gpu_job("generator/qwen3tts_language_adapt", n_gpus=4):
    subprocess.run(cmd, shell=True, check=True)
PY
