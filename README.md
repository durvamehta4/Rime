# rime-t2 — Verified captioner ⇄ generator loop for Hindi & Tamil (Inter IIT 15.0, Rime Track 2)

**Lead idea (Verified Loop).** Only claims that are *measured* by non-learned tools, *known by construction*
(controlled transforms / rendering), or *agreed by independent sources* enter the loop's training data.
Real data anchors every round and synthetic data stays ≤ 25 %.
The Track-2 rubric subtracts weight for false statements, so a loop must not amplify hallucination;
this is what lets each round improve rather than collapse.

```
CAPTIONER  audio ─► evidence toolkit (pitch, VAD/timing, bandwidth/clipping, SNR/C50, SED, creak, ASR)
                 └► Qwen3-Omni-Captioner × K samples ─► atomic claims ─► self-consistency
                    ─► fusion (drop conflicts with measurements, boost agreements) ─► calibration
                    ─► keep claim iff p̂ > τ ─► 300-word knapsack ─► prose
GENERATOR  (text, prose) ─► planner (Qwen3-8B → timed RenderPlan) ─► speaker prior (diverse voices)
                    ─► voice model (Qwen3-TTS Base/VoiceDesign → language-adapted) ─► timeline assembly
                    ─► ecology renderer (room, timed sounds at set SNR, channel codecs) ─► 24 kHz wav
LOOP       captioner labels pool (verified claims only) ─► generator SFT/DPO ─► weak-area synthetic data
                    (exact labels) ─► captioner LoRA/DPO ─► report per-round scores + GPU-hours
```

## Layout
| Path | What |
|---|---|
| `rimet2/scene` | Scene Score: claims (item type, span, p, source, value), RenderPlan, verbaliser (τ + knapsack) |
| `rimet2/evidence` | DSP measurements + optional neural analysers → claims |
| `rimet2/captioner` | Omni wrappers, claim splitting, self-consistency, fusion, calibration, CLI |
| `rimet2/generator` | round-0 CustomVoice, planner, speaker prior, voice backends, assembly, CLI |
| `rimet2/renderer` | RIR, timed mixing, channel codecs (ffmpeg), splicing, exact labels |
| `rimet2/eval` | PS rubric formula, LLM grader, CER (IndicConformer), diversity, relevance proxy, results.csv |
| `rimet2/train` | weak-area allocation, transform data, DPO pairs, TTS SFT data, LoRA for Qwen3-8B |
| `rimet2/data` | Vaani indexer (no audio decode), speaker-disjoint splits, export, tag parsing |
| `rimet2/testset` | contributed test-set validator/packager, description linter, coverage matrix |
| `rimet2/common` | audio I/O, Appendix-A bootstrap, manifest, GPU-hour ledger, Indic text normalisation, LLM client |
| `scripts/` | server entry points (setup, index, round 0, evaluations, codec ceiling, speaker bank, transforms) |
| `docs/` | **MIDTERM_RUNBOOK.md** (start here), annotation guide, report skeleton, literature map, consent |
| `research/` | 248-entry literature notes behind every design decision |

## Quick start
```bash
python -m venv .venv && . .venv/bin/activate && pip install -e . pytest && pytest -q   # CPU, ~10 s
```
On the GPU server: `bash scripts/00_setup_server.sh`, then follow `docs/MIDTERM_RUNBOOK.md`.

## What is tested where
- **CPU-tested here (37 tests):** rubric formula, PS Appendix-A bootstrap (worked example reproduced), grader
  parsing, CER normaliser, diversity counting, verbaliser budget/order, all DSP measurements on synthetic speech,
  renderer label exactness (RT60, SNR, event times, narrowband after codec), splicing, assembly timing + WSOLA,
  speaker-prior distinctness, fusion rules, calibration, Vaani indexer on a synthetic parquet, test-set packager,
  end-to-end factored generation with a mock TTS.
- **Verify on the server (needs GPUs/weights):** Omni captioner (vLLM/HF), Qwen3-TTS / Indic-Parler wrappers,
  IndicConformer, WavLM/ECAPA, Brouhaha, PANNs, age/gender, Qwen3-TTS fine-tuning launcher.
