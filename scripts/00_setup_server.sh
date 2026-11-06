#!/usr/bin/env bash
# One-time setup on the GPU server. Run from the repo root:  bash scripts/00_setup_server.sh
# Needs: HF token with access to gated repos (ai4bharat/indic-conformer-600m-multilingual, pyannote/brouhaha).
set -euo pipefail
MODELS=${MODELS:-$HOME/Vaani/models}

python -m pip install -e . && python -m pip install -r requirements-server.txt
python -m pytest -q tests/   # CPU unit tests must pass first

dl() { huggingface-cli download "$1" --local-dir "$MODELS/$(basename "$1")" ${2:-}; }
# generator backbones (CustomVoice + Tokenizer already present)
dl Qwen/Qwen3-TTS-12Hz-1.7B-Base
dl Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign
# eval / evidence models
dl ai4bharat/indic-conformer-600m-multilingual     # intelligibility judge (gated)
dl microsoft/wavlm-base-plus-sv                    # speaker diversity (threshold 0.86)
dl audeering/wav2vec2-large-robust-24-ft-age-gender  # CC-BY-NC-SA: research use only
# grader LLM (stronger than the 8B planner; FP8 fits 2 x L4)
dl Qwen/Qwen3-30B-A3B-Instruct-2507-FP8
echo "Brouhaha: accept terms at https://huggingface.co/pyannote/brouhaha then it downloads on first use."
echo "Optional data: ai4bharat/indicvoices_r (hi, ta), ai4bharat/Rasa, OpenSLR-28 RIRs, MUSAN / FSD50K (CC0/CC-BY subset)."
