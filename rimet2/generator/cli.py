"""Generator CLI: (text, description) -> 10 x 24 kHz wavs.

Systems (controlled comparison on identical items):
  round0     Qwen3-TTS CustomVoice, description as instruct (official round 0)
  parler     Indic-Parler-TTS, description as-is (reference row)
  design     Qwen3-TTS VoiceDesign, description as instruct (reference row)
  factored   planner -> speaker prior (Base clone) or VoiceDesign -> assemble -> ecology renderer (ours)

  python -m rimet2.generator.cli --items items.csv --system factored --out runs/r1/gen --n 10
items.csv columns: item_id,lang,text,description
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from rimet2.common.audio import resample, save
from rimet2.common.ledger import gpu_job
from rimet2.renderer.render import EcologyRenderer, FoleyLibrary
from rimet2.renderer.rir import RIRBank

OUT_SR = 24000


def run_factored(item, n, tts, llm, bank, renderer, base_seed, event_lib=None):
    from .assemble import assemble
    from .planner import plan as make_plan
    from .planner import voice_instruct

    p = make_plan(item["text"], item["description"], item["lang"], llm)
    sp = p.speaker or {}
    voices = bank.sample(n, seed=base_seed, lang=item["lang"], gender=sp.get("gender"), f0_hz=sp.get("f0_hz"),
                         age_band=sp.get("age_band"), region=sp.get("region")) if bank is not None else []
    outs = []
    for i in range(n):
        seed = base_seed + i
        if voices:
            v = voices[i % len(voices)]
            prompt = tts.clone_prompt(v.ref_path, v.ref_text or None)
            synth = lambda seg, prompt=prompt, seed=seed: tts.clone(seg.text, None, seed=seed, prompt=prompt)
            who = v.speaker_id
        else:  # no bank yet: VoiceDesign per sample (diversity from sampling only)
            synth = lambda seg, seed=seed: tts.design(seg.text, voice_instruct(p, seg), seed=seed)
            who = f"design_seed{seed}"
        tl = assemble(p, synth, OUT_SR, event_lib=event_lib)
        y, claims, log = renderer.render(tl.audio, p.ecology, p.coupling, seed=seed)
        outs.append((y, OUT_SR, {"voice": who, "seed": seed, "plan": json.loads(p.to_json()), "timeline": tl.spans,
                                 "render_log": log, "constructed_claims": [c.__dict__ for c in claims]}))
    return outs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", required=True)
    ap.add_argument("--system", choices=["round0", "parler", "design", "factored"], default="factored")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=1234)
    ap.add_argument("--qwen-customvoice", default="models/Qwen3-TTS-12Hz-1.7B-CustomVoice")
    ap.add_argument("--qwen-design", default="models/Qwen3-TTS-12Hz-1.7B-VoiceDesign")
    ap.add_argument("--qwen-base", default="models/Qwen3-TTS-12Hz-1.7B-Base")
    ap.add_argument("--parler", default="models/indic-parler-tts")
    ap.add_argument("--bank", default="", help="speaker bank prefix: <prefix>.jsonl + <prefix>.npy")
    ap.add_argument("--foley", default="", help="foley CSV (path,label,licence)")
    ap.add_argument("--beds", default="", help="noise-bed CSV (path,label,licence)")
    ap.add_argument("--rirs", default="", help="directory of real RIR wavs")
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--device", default="cuda:0")
    ap.add_argument("--round", default="")
    a = ap.parse_args(argv)

    items = list(csv.DictReader(open(a.items, encoding="utf-8")))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    with gpu_job(f"generator/{a.system}", round_=a.round, n_gpus=1):
        if a.system == "round0":
            from . import round0
            from .voices import Qwen3TTS
            tts = Qwen3TTS(a.qwen_customvoice, a.device)
            gen = lambda it: round0.generate(tts, it["text"], it["description"], a.n, a.seed)
        elif a.system == "parler":
            from .voices import IndicParler
            tts = IndicParler(a.parler, a.device)
            gen = lambda it: [(*tts.design(it["text"], it["description"], seed=a.seed + i), {"seed": a.seed + i})
                              for i in range(a.n)]
        elif a.system == "design":
            from .voices import Qwen3TTS
            tts = Qwen3TTS(a.qwen_design, a.device)
            gen = lambda it: [(*tts.design(it["text"], " ".join(it["description"].split()[:300]), seed=a.seed + i),
                               {"seed": a.seed + i}) for i in range(a.n)]
        else:
            from rimet2.common.llm import openai_chat
            from .speaker_prior import SpeakerBank
            from .voices import Qwen3TTS
            bank = SpeakerBank.load(a.bank + ".jsonl", a.bank + ".npy") if a.bank else None
            tts = Qwen3TTS(a.qwen_base if bank else a.qwen_design, a.device)
            llm = None if a.no_llm else openai_chat()
            R = EcologyRenderer(OUT_SR, FoleyLibrary.from_csv(a.foley, OUT_SR), FoleyLibrary.from_csv(a.beds, OUT_SR),
                                RIRBank(a.rirs, OUT_SR) if a.rirs else None)
            gen = lambda it: run_factored(it, a.n, tts, llm, bank, R, a.seed)
        meta = open(out / "generations.jsonl", "a", encoding="utf-8")
        for it in items:
            for k, (w, sr, info) in enumerate(gen(it)):
                if sr < OUT_SR:
                    w, sr = resample(w, sr, OUT_SR), OUT_SR
                p = out / it["item_id"] / f"{k:02d}.wav"
                save(p, np.asarray(w, np.float32), sr)
                meta.write(json.dumps({"item_id": it["item_id"], "k": k, "path": str(p), "system": a.system, **info},
                                      ensure_ascii=False, default=float) + "\n")
        meta.close()


if __name__ == "__main__":
    main()
