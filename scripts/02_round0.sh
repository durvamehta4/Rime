#!/usr/bin/env bash
# E1 + E4 + E5: round-0 runs and the first controlled comparisons on identical dev items.
#   bash scripts/02_round0.sh hi
# Pre-reqs: scripts/01_index_and_dev.sh; data/gen_items_<lang>.csv (item_id,lang,text,description) = our own dev
# descriptions (NOT the contributed test set). Optional: data/foley.csv, data/beds.csv, data/rirs/.
set -euo pipefail
lang=${1:-hi}
R=runs/r0; mkdir -p $R
export RIMET2_LEDGER=runs/compute_ledger.csv
MODELS=${MODELS:-$HOME/Vaani/models}

# ---- Stage A (all 4 GPUs): Omni captioner, 5 seeded samples per clip, cached. Round 0 = sample 0 verbatim. ----
RIMET2_OMNI=$MODELS/Qwen3-Omni-30B-A3B-Captioner python -m rimet2.captioner.cli --list data/${lang}_dev.list \
  --lang $lang --mode raw --k 5 --omni-cache $R/omni_${lang}.jsonl --out $R/cap_raw_${lang}.jsonl --round 0

# ---- Stage B: start the planner/fuser LLM on GPU 0 in another shell:  GPUS=0 bash scripts/serve_llm.sh planner
until curl -s localhost:8000/v1/models >/dev/null; do echo "waiting for LLM on :8000"; sleep 20; done
CUDA_VISIBLE_DEVICES=1 python -m rimet2.captioner.cli --list data/${lang}_dev.list --lang $lang --mode evidence \
  --out $R/cap_evidence_${lang}.jsonl --round 0 --device cuda:0
CUDA_VISIBLE_DEVICES=1 python -m rimet2.captioner.cli --list data/${lang}_dev.list --lang $lang --mode fused \
  --k 5 --omni-cache $R/omni_${lang}.jsonl --out $R/cap_fused_${lang}.jsonl --round 0 --device cuda:0

# ---- Stage C: generator round 0 + reference rows (one GPU each) ----
G="--items data/gen_items_${lang}.csv --round 0 --device cuda:0"
CUDA_VISIBLE_DEVICES=1 python -m rimet2.generator.cli $G --system round0 --out $R/gen_round0_${lang} \
  --qwen-customvoice $MODELS/Qwen3-TTS-12Hz-1.7B-CustomVoice &
CUDA_VISIBLE_DEVICES=2 python -m rimet2.generator.cli $G --system parler --out $R/gen_parler_${lang} \
  --parler $MODELS/indic-parler-tts &
CUDA_VISIBLE_DEVICES=3 python -m rimet2.generator.cli $G --system design --out $R/gen_design_${lang} \
  --qwen-design $MODELS/Qwen3-TTS-12Hz-1.7B-VoiceDesign &
wait
# early round-1 slice: factored system (planner + VoiceDesign + renderer), no speaker bank yet
CUDA_VISIBLE_DEVICES=1 python -m rimet2.generator.cli $G --system factored --out $R/gen_factored_${lang} \
  --qwen-design $MODELS/Qwen3-TTS-12Hz-1.7B-VoiceDesign --foley data/foley.csv --beds data/beds.csv --rirs data/rirs

echo "Score: python scripts/eval_captions.py --rubric data/rubric_${lang}.csv --captions $R/cap_*_${lang}.jsonl"
echo "       python scripts/eval_generation.py --gens $R/gen_*_${lang}/generations.jsonl --items data/gen_items_${lang}.csv"
