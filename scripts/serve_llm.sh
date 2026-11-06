#!/usr/bin/env bash
# OpenAI-compatible LLM servers used by the fuser/planner (Qwen3-8B) and the rubric grader (Qwen3-30B-A3B FP8).
#   bash scripts/serve_llm.sh planner   # GPU 0, port 8000
#   bash scripts/serve_llm.sh grader    # GPUs 2,3, port 8001
# Clients read RIMET2_LLM_URL / RIMET2_LLM_MODEL (see rimet2/common/llm.py).
set -euo pipefail
MODELS=${MODELS:-$HOME/Vaani/models}
case "${1:-planner}" in
  planner)
    CUDA_VISIBLE_DEVICES=${GPUS:-0} vllm serve "$MODELS/Qwen3-8B" --served-model-name Qwen3-8B \
      --port 8000 --max-model-len 8192 --gpu-memory-utilization 0.90 --seed 1234 ;;
  grader)
    CUDA_VISIBLE_DEVICES=${GPUS:-2,3} vllm serve "$MODELS/Qwen3-30B-A3B-Instruct-2507-FP8" \
      --served-model-name grader --tensor-parallel-size 2 --port 8001 --max-model-len 8192 \
      --gpu-memory-utilization 0.90 --seed 1234 ;;
esac
