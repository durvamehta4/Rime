# Track 2 brief (Inter IIT Tech Meet 15.0 — Rime problem statement)

## Task
Build a **speech captioner** and a **voice generator** for **Hindi and Tamil** that improve each other in a loop
(round 0 = baseline, then >=1 more round; fewer rounds is better).
Each round: (1) captioner describes the speech pool -> expands training set; (2) generator trains to speak from
text + description; (3) generator makes speech targeting captioner weak areas -> trains next captioner.
Final submitted models must run on their own: open models only, no closed API, no human in the loop.
- Captioner: one audio file (<=30 s) -> English free-text description.
- Generator: text + description -> audio at >=24 kHz. 10 samples per description at eval.
- One unified model (like UALM) is allowed.

## Data / models
- Vaani (IISc/ARTPARK, CC-BY-4.0) Hindi ~14,900 h and Tamil ~850 h, spontaneous image-prompted phone speech,
  16 kHz, partial transcripts + metadata (speaker, gender, state/district...). Any other public dataset allowed.
- Suggested round 0: Qwen3-Omni-30B-A3B-Captioner (understanding), Qwen3-TTS-12Hz-1.7B-CustomVoice (generation).
- Team also has locally: indic-parler-tts, Qwen3-8B, Qwen3-TTS-Tokenizer-12Hz, whisper-large-v3.
- Hardware: 4x NVIDIA L4 (24 GB each, Ada, FP8 capable, PCIe, no NVLink).

## Descriptions (what the captioner must write / generator must follow)
Free English text, what a careful listener hears, with times and numbers, not tag lists. Three axes:
- The voice: Speaker, Source (modal/breathy/creaky/strained/falsetto), Morphology (how phrases start/end),
  Pitch (semitones, Hz), Timing (ms), Event (laugh at 3.2-3.9 s etc).
- The recording: Channel (phone/mic/codec/bandwidth), Space (room/reverb), Other sounds, Coupling
  (how the voice changes in response to environment, e.g. Lombard effect).
- The intent: Addressee, Subtext, Change.
Descriptions can be fantastical (Fugatto-style). Clip <=30 s; description cut at 300 words before grading.

## Scoring (results = 20 of 100 points; other 80 judged on framing, novelty/depth, rigour, reproducibility, presentation)
- Description rubric (10 pts): Rime writes a private rubric per clip: weighted true items (global + timed, timed items
  count if placed within span +-250 ms) and a few FALSE items. Score = (weight of true items stated - weight of items
  contradicted or false items asserted) / total true weight, floored at 0. Hedging between alternatives does not count.
  A fixed grader LLM checks. => precision matters; hallucination is penalised.
- Generation instruction relevance (5): 3 listeners check each statement of the description against the audio.
- Naturalness CMOS vs other teams (2).
- Speaker diversity (2): 10 samples per description, count distinct speakers (fixed speaker-verification model, standard
  threshold) among samples that pass relevance checks; points = 2 x mean count / 10.
- Intelligibility (1): CER of AI4Bharat IndicConformer vs native-script text.
- Must report per-round scores + compute, Pareto frontier of score vs model size/compute, bootstrap CIs,
  controlled comparisons/ablations, a manifest of the source + labeler of every training example.

## Mid-term deliverables
report.pdf (<=6 pages: problem framing & prior work, baselines & eval setup, early results + failure analysis + revised plan),
results.csv, test_set.zip (per language 30 recorded clips for the captioner + 30 descriptions with text for the generator),
round0.zip (code, settings, checkpoint hashes).

## Suggested ideas in the PS
Target captioner weak areas; use captioner as judge/reward for generator (+ strong text LLM); make labels for free by
controlled transforms of clean speech (convolve RIR, add noise at chosen SNR, pitch shift known amount, splice a laugh
at known time); build instruction data from templates + LLM rewrites + known transforms (Fugatto). Only write what can be
confirmed in the audio (calm != low pitch; shouting != anger).
Background reading given: Fugatto (ICLR'25), UALM (ICLR'26), Audio Flamingo 3 (NeurIPS'25), MMAU (ICLR'25), MMAU-Pro (AAAI'26).
