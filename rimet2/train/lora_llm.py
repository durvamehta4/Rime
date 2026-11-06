"""LoRA SFT for Qwen3-8B as (a) captioner fuser/editor or (b) generator planner.

Data: JSONL {"prompt": ..., "response": ...}. Loss on response tokens only. Fits one L4 (bf16 weights ~16 GB,
LoRA r=16 on attention+MLP, gradient checkpointing, seq<=2048). For 4 GPUs use `torchrun --nproc_per_node 4`.

  python -m rimet2.train.lora_llm --model models/Qwen3-8B --data runs/r1/planner_sft.jsonl --out ckpt/planner_r1
"""
from __future__ import annotations

import argparse
import json


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--epochs", type=float, default=2)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--r", type=int, default=16)
    ap.add_argument("--max-len", type=int, default=2048)
    ap.add_argument("--bsz", type=int, default=1)
    ap.add_argument("--grad-accum", type=int, default=16)
    ap.add_argument("--seed", type=int, default=1234)
    a = ap.parse_args(argv)

    import torch
    from datasets import Dataset
    from peft import LoraConfig, get_peft_model
    from transformers import (AutoModelForCausalLM, AutoTokenizer, DataCollatorForSeq2Seq, Trainer,
                              TrainingArguments)

    from rimet2.common.ledger import gpu_job

    tok = AutoTokenizer.from_pretrained(a.model)
    rows = [json.loads(l) for l in open(a.data, encoding="utf-8")]

    def enc(r):
        msgs = [{"role": "user", "content": r["prompt"]}]
        p = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        pi = tok(p, add_special_tokens=False)["input_ids"]
        ri = tok(r["response"] + tok.eos_token, add_special_tokens=False)["input_ids"]
        ids = (pi + ri)[:a.max_len]
        labels = ([-100] * len(pi) + ri)[:a.max_len]
        return {"input_ids": ids, "attention_mask": [1] * len(ids), "labels": labels}

    ds = Dataset.from_list(rows).map(enc, remove_columns=list(rows[0].keys()))
    model = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.bfloat16, attn_implementation="sdpa")
    model.gradient_checkpointing_enable()
    model.enable_input_require_grads()
    model = get_peft_model(model, LoraConfig(r=a.r, lora_alpha=2 * a.r, lora_dropout=0.05, task_type="CAUSAL_LM",
                                             target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj",
                                                             "up_proj", "down_proj"]))
    args = TrainingArguments(output_dir=a.out, per_device_train_batch_size=a.bsz, gradient_accumulation_steps=a.grad_accum,
                             num_train_epochs=a.epochs, learning_rate=a.lr, lr_scheduler_type="cosine",
                             warmup_ratio=0.03, logging_steps=10, save_strategy="epoch", bf16=True, seed=a.seed,
                             data_seed=a.seed, report_to=[])
    with gpu_job(f"train/lora_llm:{a.out}"):
        Trainer(model=model, args=args, train_dataset=ds,
                data_collator=DataCollatorForSeq2Seq(tok, padding=True, label_pad_token_id=-100)).train()
    model.save_pretrained(a.out)
    tok.save_pretrained(a.out)


if __name__ == "__main__":
    main()
