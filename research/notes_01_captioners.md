# Notes 01 — Speech/audio captioners and audio-language models (captioner side)

Cluster owner: lit-review agent, compiled 2026-11-04. Goal: inform the Track 2 captioner (Hindi/Tamil clip, up to 30 s -> English description, graded by a private rubric that penalises false items, timed items +-250 ms).

Method: every arXiv ID below was checked against the arXiv API (title match). Details come from the arXiv HTML/abstract pages, Hugging Face model cards/API, and ms-swift example scripts. Venues I could not confirm are marked [venue unverified]. Numbers are copied from the papers; where a paper contradicts itself, I say so. "Read depth" says how much I read: full = HTML method and results; abs = abstract/metadata only.

---

## A. Open audio-language models and captioners

### Qwen3-Omni Technical Report (arXiv 2025) — arXiv:2509.17765 (+ HF card Qwen/Qwen3-Omni-30B-A3B-Captioner)
- Read depth: full (first 100k characters) + model card + HF API.
- **Key idea:** Thinker–Talker MoE omni model. The Thinker is a 30B-A3B MoE. The audio encoder (AuT, about 0.6B, trained on 20M hours of supervised audio) downsamples 8x to **12.5 Hz, about 80 ms per audio token**. The **Captioner** is the Instruct model fine-tuned "on a large-scale dataset of detailed audio descriptions" to give a general-purpose, "low-hallucination" captioner.
- **Data/training recipe:** Pre-training has three stages: (S1) encoder alignment with the LLM frozen; (S2) about 2T tokens (audio 0.77T); (S3) long context, 8k -> 32k. Thinker post-training is SFT, then strong-to-weak distillation (off-policy, then on-policy against Qwen3-32B or 235B-A22B), then **GSPO RL with rule-based and LLM-judge rewards**. The paper gives no Captioner data recipe; its appendix has only qualitative cases.
- **Key numbers:** MMAU 77.5 (Instruct); MMSU 69.0; VoiceBench 85.5; LibriSpeech 1.22/2.48 WER. **No quantitative Captioner evaluation is reported.**
- **Captioner card:** audio-only input, **no text prompt accepted**, single turn, **recommended 30 s or less**. "Excessively long audio clips may diminish detail perception." vLLM settings: temp 0.6, top_p 0.95, top_k 20, max_model_len 32768. HF safetensors total is 31.7B params (thinker only). Licence: Apache-2.0 (card `license_name: apache-2.0`). Community AWQ-4bit/8bit and GGUF quantisations exist (cyankiwi/..., mradermacher/...).
- **Languages:** speech-input languages listed: ar, de, en, es, fr, id, it, ja, ko, ms, nl, pt, ru, th, tr, **ur**, vi, yue, zh. **Hindi and Tamil are not listed.** Urdu is close to spoken Hindi; Tamil has no near neighbour in the list.
- **Takeaway for Track 2:** This is the natural round-0 captioner and a good LoRA base, because its paralinguistic and scene coverage is broad. Three cautions follow. (a) It cannot be prompted, so to inject DSP evidence or a rubric style we must fine-tune it or post-edit its output with a text LLM (Qwen3-8B). (b) Expect weak Tamil content and intent understanding; take transcripts from IndicConformer or Whisper rather than from the captioner. (c) An 80 ms token grid is fine for the +-250 ms tolerance.

### Qwen-Audio (arXiv 2023) — arXiv:2311.07919
- Read depth: full.
- **Key idea:** Whisper-large-v2 encoder (640M) plus Qwen-7B, trained on 30+ tasks in 8 languages. **Hierarchical tags** (task, language, timestamps / no-timestamps) avoid one-to-many interference. **SRWT:** word-level start and end time tokens interleaved with the transcript. Encoder frames are about 40 ms.
- **Key numbers:** SRWT ablation: AISHELL-1 test 1.71 -> 1.29 WER; ClothoAQA 0.5648 -> 0.5795; MusicAVQA 0.7027 -> 0.7211. Clotho captioning CIDEr 0.441.
- **Open weights + licence:** Qwen/Qwen-Audio on HF (no licence tag in the API; Qwen licence [unverified]).
- **Takeaway:** Training with explicit timestamp targets also *improves* grounding-based QA, not just timing. Add timestamped auxiliary targets (word times, event spans) to our captioner SFT even if the final caption uses only some of them.

### Qwen2-Audio Technical Report (arXiv 2024) — arXiv:2407.10759
- Read depth: full.
- **Key idea:** Hierarchical tags replaced by natural-language prompts. Whisper-large-v3 encoder (128 mel, 40 ms per frame) plus Qwen-7B, 8.2B total. Two modes: voice chat and audio analysis.
- **Data/training recipe:** Pre-training, then SFT, then **DPO on human-annotated preference pairs "to optimise factuality"**.
- **Key numbers:** AIR-Bench chat speech/sound/music/mixed = 7.18/6.99/6.79/6.77. VocalSound 0.9392. MELD 0.553 (not SOTA).
- **Open weights + licence:** Qwen2-Audio-7B-Instruct, Apache-2.0.
- **Takeaway:** DPO on factual vs non-factual responses is the standard post-SFT step for factuality. We can build DPO pairs automatically: a caption with a known transform label (correct) vs. the same caption with a corrupted attribute (rejected).

### Qwen2.5-Omni Technical Report (arXiv 2025) — arXiv:2503.20215
- Read depth: full.
- **Key idea:** Thinker–Talker architecture. **TMRoPE** gives absolute time position IDs, with **one temporal ID = 40 ms**. Audio is in 2 s blocks for streaming. Encoder initialised from Whisper-large-v3.
- **Data/training recipe:** Three pre-training stages (encoders only; then 300B audio tokens + 800B image/video + 100B video-audio; then 32k long context).
- **Key numbers:** MMAU 65.60 (speech 59.76); MELD 0.570; VocalSound 0.939; LibriSpeech 1.8/3.4.
- **Open weights + licence:** 7B is Apache-2.0 (card license_name); the 3B is under a different "other" licence [unverified which].
- **Takeaway:** Absolute-time RoPE means the model has an internal clock. A 7B fallback base for cheap LoRA ablations (Omni-Captioner, TVPara and ASTP all fine-tune it).

### SALMONN (ICLR 2024) — arXiv:2310.13289
- Read depth: full.
- **Key idea:** Whisper (speech) plus BEATs (audio) dual encoder, a window-level Q-Former (window 17 frames, about 0.33 s, giving 88 tokens per 30 s), and Vicuna-13B with LoRA (r=8, scale 4.0). Only about 33M params are trained.
- **Data/training recipe:** Three stages: pre-training (960 h LibriSpeech, 1000 h GigaSpeech, 2800 h WavCaps); instruction tuning (about 4,400 h, 2.3M samples, 12 tasks); **activation tuning** (12 stories, 12 steps).
- **Key numbers:** "Task over-fitting": the model collapses to ASR or caption-like outputs. Halving the LoRA scale to 2.0 restores instruction following. After activation tuning, story-following rate goes 0.00 -> 1.00 with ASR WER unchanged at 2.1.
- **Open weights + licence:** tsinghua-ee/SALMONN, Apache-2.0.
- **Takeaway:** If we LoRA-tune a captioner on templated captions, it can over-fit to the template. Mitigations: diverse phrasings (LLM rewrites), and tuning the LoRA scale at inference as a cheap knob between "rubric-style factual" and "fluent" output.

### Listen, Think, and Understand — LTU (ICLR 2024 [venue unverified]) — arXiv:2305.10790
- Read depth: full (first 100k characters).
- **Key idea:** OpenAQA-5M (1.9M closed-ended + 3.7M open-ended QA). GPT-3.5 generates open-ended QA **from metadata only** (events, acoustic features, captions, timestamps), never hearing the audio.
- **Data/training recipe:** A 4-stage **perception-to-understanding curriculum**: projection only -> encoder + LoRA on classification/description -> all closed-ended -> plus open-ended. LLaMA-7B frozen, LoRA r=8 on Q/K.
- **Key numbers:** Without the curriculum, classification falls 50.3 -> 23.0. About **6.5% "it cannot be determined from the audio" answers** raise the refusal rate on unanswerable questions from 51.9% to 69.3% at no cost to closed-ended accuracy (50.0 -> 50.3). Humans judged 79.3% of answers fully correct.
- **Takeaway:** (1) Train perception (closed-form attribute targets) before free-form captions. (2) Include "not determinable / not present" supervision so the model learns to omit, which is what the rubric's false-item penalty rewards. (3) The metadata-to-LLM-to-text recipe is exactly our "controlled transforms -> template -> LLM rewrite" plan.

### Joint Audio and Speech Understanding — LTU-AS (ASRU 2023 [venue unverified]) — arXiv:2309.14405
- Read depth: full.
- **Key idea:** All 32 Whisper encoder layers feed a TLTR (time- and layer-wise transformer) for paralinguistics, **plus the Whisper transcript as text input**, into LLaMA-7B with LoRA. Speed, pitch and energy are computed with Whisper timestamps and librosa to build the GPT training data.
- **Data/training recipe:** Open-ASQA, 9.6M QA (Table 2; the intro says 6.9M open-ended, which is inconsistent). Three-stage curriculum. About 80 h on 4x A6000.
- **Key numbers:** IEMOCAP 65.2; VoxCeleb2 gender F1 90.8, age MAE 7.3. Training data: 1.089M clips.
- **Takeaway:** Two ideas to copy cheaply: (a) **DSP-measured prosody (rate, pitch, energy) as label source** for LLM-written training captions; (b) feeding an external transcript as text gives content grounding. For Hindi/Tamil, pass an IndicConformer transcript to the text-LLM rewriter rather than trusting the captioner's ASR.

### Audio Flamingo 2 (ICML 2025 [venue unverified]) — arXiv:2503.03983
- Read depth: full (first 100k characters).
- **Key idea:** AF-CLAP, trained on 8M pairs with **composition-aware hard negatives** (temporal and attribute swaps). Uses a 3B LLM (Qwen2.5-3B). AudioSkills dataset: 4.2M QA. LongAudio dataset: 263k QA.
- **Key numbers:** MMAU sound 65.1, music 72.9. The paper states that "data quality often surpasses ... scaling compute."
- **Weights/licence:** HF nvidia/audio-flamingo-2 (0.5B, 1.5B, 3B variants); licence not stated in paper; NVIDIA non-commercial [unverified].
- **Takeaway:** Attribute- and order-swapped negatives are the right way to build a contrastive or DPO signal for "who/what happened when". Use swapped-time and swapped-attribute negatives for our DPO pairs.

### Audio Flamingo 3 (NeurIPS 2025) — arXiv:2507.08128
- Read depth: full (first 100k characters).
- **Key idea:** AF-Whisper encoder (Whisper-v3 further trained on 13.2M audio-caption pairs, 50 Hz then pool x2) plus Qwen2.5-7B. Fully open data: AudioSkills-XL 8M, LongAudio-XL about 1M+, AF-Think 250k, AF-Chat 75k.
- **Data/training recipe:** Five stages: adaptor only -> encoder + adaptor -> full (up to 2.5 min) -> **LoRA** for long context and thinking (up to 10 min) -> chat and voice.
- **Key numbers:** MMAU test 72.42 (73.16 with Think); MMAR 58.5; MMSU 61.4; AudioCaps CIDEr 0.70; CMM hallucination 86.5 (the text says 86.7).
- **Weights/licence:** research-only (NVIDIA OneWay Noncommercial on HF).
- **Takeaway:** The curriculum order (align -> encoder -> full -> LoRA extensions) is a proven template. Usable as a second "opinion" model for ensemble or verification only if the research licence is acceptable for the competition (check the rules). Note that its high instruction-following scores did *not* translate to grounded style captions (see StyleInstructCaps, where its meta-score is 3.88).

### Audio Flamingo Next (arXiv 2026) — arXiv:2604.10905 (+ HF nvidia/audio-flamingo-next-captioner-hf)
- Read depth: full.
- **Key idea:** Successor to AF3. Qwen2.5-7B with 128k context. **Rotary Time Embeddings (RoTE)**: positions are absolute timestamps. **Temporal Audio CoT** ties reasoning steps to times. Three releases: Instruct, Think, **Captioner**.
- **Data/training recipe:** About 108M samples, about 1M hours. Pre-training (LLM frozen), mid-training (up to 30 min audio) producing the Captioner, then GRPO post-training producing Instruct. The Captioner's long-audio data comes from about 200k videos, with four annotation types per 10 s segment merged by an LLM.
- **Key numbers (Captioner):** MMAU 75.76 (speech 72.13); MMAR 63.0; MMSU 63.3. CMM hallucination 87.0 (Instruct).
- **Weights/licence:** NVIDIA OneWay **Noncommercial**, research only. English card; "low-resource languages underrepresented". No Hindi or Tamil mentioned.
- **Takeaway:** This is the strongest open captioner on reasoning benchmarks, but it is non-commercial and has no Indic coverage. If allowed, use it as a teacher or verifier in label fusion, not as the submission base. RoTE and segment-wise (10 s) annotation merged by an LLM is a good pattern for our 30 s clips: annotate 0–10, 10–20 and 20–30 s windows separately, then merge.

### Kimi-Audio Technical Report (arXiv 2025) — arXiv:2504.18425
- Read depth: full.
- **Key idea:** 12.5 Hz discrete semantic tokens **plus** continuous Whisper features, with LLM initialised from Qwen2.5-7B. About 13M hours of pre-training audio.
- **Data/training recipe:** Large data pipeline: BSRNN enhancement, PyAnnote diarization with merging heuristics, Whisper/Paraformer ASR, about 200k h/day. SFT on about 300k h, including 5,200 h in-house AAC/AQA.
- **Key numbers:** MMAU sound 73.27, speech 60.66; VocalSound 94.85; MELD 59.13.
- **Weights/licence:** moonshotai/Kimi-Audio-7B-Instruct, MIT (HF tag).
- **Takeaway:** The data pipeline (enhancement, diarization, segment merging up to 27 s) is a good template for cleaning the Vaani pool into 30 s units. A permissive-licence 7B alternative with strong emotion and vocal-sound recognition, useful as an ensemble member.

### Step-Audio 2 Technical Report (arXiv 2025) — arXiv:2507.16632
- Read depth: full.
- **Key idea:** End-to-end LALM with a frozen 25 Hz encoder, adaptor to 12.5 Hz, and interleaved text and audio tokens. RL focuses on paralinguistic perception. Retrieval (RAG) over a voice library.
- **Data/training recipe:** 1.356T tokens of continued pre-training; SFT on 4B tokens; then **PPO (concise-reasoning reward) -> PPO (learned RM) -> GRPO for 400 iterations "to improve audio perception"**.
- **Key numbers:** **StepEval-Audio-Paralinguistic** (550 clips, 11 dimensions including pitch, rhythm, speed, timbre, scenario, event, vocal): Step-Audio 2 **83.09**, mini 80.00, vs GPT-4o Audio 43.45, Kimi-Audio 49.64, Qwen-Omni 44.18. MMAU 78.0 (mini 73.2).
- **Weights/licence:** stepfun-ai/Step-Audio-2-mini, Apache-2.0 (8.3B; Qwen2-Audio encoder plus Qwen2.5-7B).
- **Takeaway:** This is the best *reported* open paralinguistic perception, especially Step-Audio-2-mini, which is cheap to LoRA on one L4 pair. Its benchmark dimensions (pitch, rhythm, speed, timbre, scenario, event, vocal) line up with our rubric axes. Worth a round-0 bake-off against the Qwen3-Omni Captioner on our 30-clip test set. GRPO with verifiable perception rewards is the RL recipe to copy.

### GAMA (EMNLP 2024 [venue unverified]) — arXiv:2406.11768
- Read depth: full (first 100k characters).
- **Key idea:** Multiple audio feature streams (Audio Q-Former, multi-layer aggregator over AST layers 4 and 8, and **soft prompts built from AST event tags**). CompA-R instruction data is built by GPT-4 from vision and audio tags **plus AudioSet-Strong event timestamps**, with human filtering of hallucinated items.
- **Key numbers:** Removing the event-tag soft prompt drops CompA-R-test from 4.0/4.3 to 3.8/3.8 and dense captioning from 4.2 to 4.0.
- **Takeaway:** Feeding detector outputs (event tags) as extra input measurably helps. This is evidence for a **tool-augmented captioner**: give the model a text "evidence sheet" (SED events with times, F0 statistics, SNR) during SFT and inference.

### UALM: Unified Audio Language Model (ICLR 2026 per brief) — arXiv:2510.12000
- Read depth: full.
- **Key idea:** One Qwen2.5-7B for understanding (AF3 encoder input) and generation (X-codec, 50 Hz x 8 RVQ, delay pattern), plus a 48 kHz enhancement VAE. **UALM-Reason** does *self-reflection*: it generates audio, captions what it actually produced, critiques the caption against the plan, and regenerates.
- **Data/training recipe:** UALM-Gen 1.5B was trained on about 30M samples (about 80k h); DPO from 250k prompts x 10 samples (about 50k pairs). Unified: 660k steps on 128 A100s. Reason: two rounds of SFT + DPO (750k SFT + about 60k DPO; then 850k SFT + 20k DPO).
- **Key numbers:** MMAU 74.1; MMAR 55.2. Self-reflection subjective 3.82 -> 4.04 (+-0.10 CI). There is no objective metric for the loop.
- **Weights/licence:** Not stated in paper (repo NVIDIA/audio-intelligence) [unverified].
- **Takeaway:** This validates our loop shape: captioner-as-critic of generated audio, then DPO. Its compute is far beyond 4x L4, so copy the *protocol* (10 samples per prompt -> rank with captioner/judge -> DPO pairs), not the model.

### Omni-Captioner (arXiv 2025) — arXiv:2510.12720
- Read depth: full.
- **Key idea:** **Omni-Detective**, an agentic pipeline in which a detective LLM repeatedly queries independent "observer" tools (MLLM, ASR, OCR) for up to 10 rounds to verify details before writing. The captioner is trained on the result. **Removing text prompts from the input improved descriptive performance.**
- **Data/training recipe:** About 55k audio-only VGGSound samples -> Audio-Captioner-7B (Qwen2.5-Omni-7B; full fine-tune, LR 5e-6, 2 epochs, **8 h on 8x A100**).
- **Key numbers:** Audio-Captioner-7B gets MMAU 70.0 and MMAR 59.8 (best open at the time), used as captioner plus LLM. **Detail and hallucination co-grow with caption length** (Gemini analysis). Omni-Cloze benchmark (cloze with a "Not Given" option to separate omission from hallucination) correlates with human Elo at r=0.91.
- **Weights/licence:** "all open-source" (GitHub); licence not stated [unverified].
- **Takeaway:** This is the most directly reusable recipe. (1) Build training captions with a *verify-before-write* agent (Qwen3-8B as detective; the Qwen3-Omni Captioner, IndicConformer, DSP tools and SED as observers). (2) A small high-quality set (about 55k) is enough for a large gain. (3) Because length raises hallucination, **cap caption length and only write verified items**, given that the rubric subtracts false items. (4) Use an Omni-Cloze-like "Not Given" eval internally.

### MOSS-Audio Technical Report (arXiv 2026) — arXiv:2606.01802 (+ HF card)
- Read depth: abstract + model card.
- **Key idea:** 12.5 Hz encoder with **DeepStack** multi-layer injection and **time markers inserted into the audio token stream**. Event-preserving annotation pipeline with separate speech, music and sound branches merged into one caption.
- **Key numbers (HF card):** speech captioning LLM-judge average **3.7252** for MOSS-Audio-8B-Instruct vs Qwen3-Omni-30B-A3B-Instruct 3.5986. Timestamp-ASR AAS on LibriSpeech 131.61 vs Qwen3-Omni 646.95 (lower is better). In StyleInstructCaps (below), its meta-score of 6.32 is the best untuned open model.
- **Weights/licence:** OpenMOSS-Team/MOSS-Audio-8B-Instruct, **Apache-2.0**, about 9B params (Qwen3-8B backbone). English and Chinese only.
- **Takeaway:** This is a strong, small, permissive alternative captioner base with native timestamp skill. It is cheap to LoRA on 2x L4 and fits the Pareto-frontier story (8B vs 30B). Include it in the round-0 bake-off.

### TAC: Timestamped Audio Captioning (arXiv 2026) — arXiv:2602.15766
- Read depth: full (first 100k characters).
- **Key idea:** Captions per event with `<|t|>`-style atomic time tokens, e.g. `[sfx] A dog barks ... from <|0.50|>s to <|2.30|>s`. Trained on **synthetic mixtures with known onsets** (about 150k mixtures, about 1.2k h). Ground truth comes from RMS activity detection, not metadata.
- **Data/training recipe:** Qwen2-Audio frozen plus **LoRA r=128, alpha=256 on all linear layers**. Timestamp-token loss is up-weighted (**lambda_time = 5.0**). 5k iterations on 8x A100.
- **Key numbers (TACOS):** EvtF1 0.50 / SegF1 0.71 / **Hal% 4.9** vs Qwen3-Omni 0.37 / 0.66 / 7.3 and AF3 0.27 / 0.55 / 11.6. Pretraining halves hallucination (8.8 -> 4.9%). Hallucination is measured as FLAM confidence < 0.25. The LLM judge correlates with humans at Spearman 0.81.
- **Weights/licence:** no release commitment.
- **Takeaway:** This is the best evidence that **synthetic mixing with known times plus timestamp-token loss up-weighting** fixes timing in a cheap LoRA. Adopt it directly for the brief's "splice a laugh at known time" idea. Use RMS/VAD-derived spans (not nominal splice times) as truth. Use an audio-text model confidence filter (FLAM or CLAP) to prune hallucinated events.

### TAC2: Timestamped Audio Captioning as composable functions (arXiv 2026) — arXiv:2610.36568
- Read depth: full (first 100k characters).
- **Key idea:** **Backbone = Qwen3-Omni-30B(-A3B) Captioner**. Weak teachers (TAC-style SED, diarizer, the Qwen3-Omni captioner, wav2vec2 forced alignment) are fused by **time-registered IoU matching** with an attribute "authority map" (the most reliable teacher wins per attribute). TAC2-S adds expressive speech attributes by distilling LoRA specialists.
- **Data/training recipe:** Stage 1: **rank-512 attention-only LoRA**, about 2M in-the-wild clips of up to 30 s, 10k steps, LR 1.6e-3. Stage 2: specialists (stress/intonation from A560E + torchcrepe; emotion from IEMOCAP, RAVDESS, MELD; voice profile; CREPE F0 + RMS), each trained on fewer than 10k examples. These are hot-loaded as TAC2-E to re-annotate, then **Qwen3-Next-80B rewrites** the overview for consistency, and the result is distilled into one LoRA (2k steps).
- **Key numbers:** Probing shows paralinguistic attributes are **linearly decodable from the frozen backbone (AUC 0.89–0.99) but the model fails to verbalise them**. MMSU perception: TAC2-S **77.8 vs Qwen3-Omni-Captioner 63.5**. Pitch-comparison 63.0 -> 75.9 with multi-pass. Pitch and loudness are **relative within clip, with no Hz and no speaking rate**.
- **Weights/licence:** weights release not stated. The corpus is proprietary, but the IoU-fusion code is provided.
- **Takeaway:** This is the closest prior art to our captioner. It proves that **attention-only LoRA on the Qwen3-Omni Captioner works** (and sidesteps MoE expert-LoRA issues). It shows that teacher fusion plus specialist distillation beats the base model on perception. It also leaves a gap we can fill: **absolute Hz, semitones and ms rate numbers**, which the brief's rubric asks for.

### Towards Fine-grained Temporal Perception: Post-Training LALMs with Audio-Side Time Prompt (arXiv 2026) — arXiv:2604.13715
- Read depth: full.
- **Key idea:** Adds 750 timestamp tokens (`<0.04>` ... 30 s, 0.04 s stride) **interleaved with the 25 Hz audio tokens** at their positions. Embeddings are initialised from the mean of the number-string subword embeddings and kept frozen.
- **Data/training recipe:** Qwen2-Audio and Qwen2.5-Omni-7B, **LoRA r=8, alpha=32**. SFT for 3 epochs, then **GRPO** (10.2k samples, group 4) with an event-F1 reward plus mIoU or METEOR auxiliary rewards.
- **Key numbers (Qwen2.5-Omni):** SED event F1 13.7 (zero-shot) -> 48.9 (SFT) -> 57.6 (RL). Grounding mIoU 69.9 -> 74.4. Dense-caption event F1 35.2 -> 40.7. Random timestamp-embedding initialisation costs 2.9 F1.
- **Takeaway:** Timing is learnable with a tiny LoRA plus a verifiable RL reward. The rubric's +-250 ms tolerance window can be turned directly into a GRPO reward (fraction of timed claims inside the span) for round 2+.

### SECap: Speech Emotion Captioning (AAAI 2024 [venue unverified]) — arXiv:2312.10381
- Read depth: full.
- **Key idea:** HuBERT -> Q-Former -> frozen LLaMA. **Speech–transcription mutual-information minimisation** keeps content out of the emotion features, plus a speech–caption contrastive loss.
- **Key numbers:** Adding the raw transcript *lowers* caption quality (SIM1 71.95 -> 69.24). The ablation shows both losses help (67.29 -> 71.95). MOS 3.77 vs human captions 3.85. Internal Chinese EMOSpeech, 41.6 h.
- **Takeaway:** Lexical content leaks into paralinguistic judgments, the "calm != low pitch" trap in the brief. Keep transcript-driven intent ("Subtext") separate from acoustic claims, and generate acoustic claims only from acoustic evidence.

---

## B. Speech-style caption datasets and pipelines

### ParaSpeechCaps (arXiv 2025 [venue unverified]) — arXiv:2503.04713
- Read depth: full (first 100k characters).
- **Key idea:** 59 style tags (28 rich intrinsic, 23 rich situational, 8 basic). PSC-Base is about 282 h of human labels; PSC-Scaled is about 2,427 h auto-labelled (the HTML renders these numbers garbled).
- **Data/training recipe:** Intrinsic tags propagate to Emilia speakers with VoxSim speaker cosine of at least 0.8. Situational tags come from a DVA-arousal filter, then text-embedding match, then a Gemini rating (keep only 5/5). **Basic tags are DSP-binned**: pitch uses gender-dependent thresholds (male low < 115.7 Hz, female low < 141.6 Hz); speed slow < 11.5, fast > 19.1 phonemes/s; SNR bins from 17.1 to 75 dB. Mistral-7B writes the prompts.
- **Key numbers:** Parler-TTS-mini fine-tuned: intrinsic tag recall 69.5%, situational 75.4%.
- **Licence:** annotations released; audio under source licences. The derived Parler checkpoint is CC-BY-NC-SA-4.0 (HF).
- **Takeaway:** Ready-made thresholds to translate measured F0 and rate into words. **But the rubric wants numbers**, so state both: "low-pitched (median F0 about 105 Hz)". Precision-oriented filtering (keep only top-confidence situational labels) is the right posture for the rubric's false-item penalty.

### SpeechCraft (ACM MM 2024 [venue unverified]) — arXiv:2408.13608
- Read depth: full.
- **Key idea:** About 2.2M clips, EN+ZH (about 2,380 h per Table 4). Attribute recognisers (signal processing for pitch, energy, speed; wav2vec2 for age and gender; emotion2vec) feed a fine-tuned LLaMA-2 that writes descriptions. **Word-level emphasis** comes from regenerating speech with FastSpeech2 and scaled prosody predictors.
- **Key numbers:** Emphasis detection 85–89% on regenerated data but only **66.9% word / 41.6% sentence on real speech**. Retrained SECap user score 3.79 vs 3.58.
- **Takeaway:** (1) The synthetic-to-real gap is large for fine prosody, so mix real labelled data with synthetic transforms. (2) The "re-synthesise with known prosody edits" idea fits our generator loop: the generator can make emphasis- or pitch-controlled variants with known ground truth for the next captioner round.

### CapSpeech (arXiv 2025 [venue unverified]) — arXiv:2506.02863
- Read depth: full.
- **Key idea:** More than 10M machine-annotated and about 0.36M human-annotated speech–caption pairs. Includes **sound-effect insertion at known positions** (forced-alignment word gaps of at least 0.3 s; SNR -3 to 6 dB; 394 event types) and background layering.
- **Data/training recipe:** Clips of 3–18 s; drop WER > 25% and Squim SNR < 20 dB. Continuous values are binned into keywords, then Mistral writes captions. A human check found **95.5% per-tag correctness**.
- **Licence:** **CC BY-NC 4.0**.
- **Takeaway:** This is a concrete recipe for the "splice event at known time" augmentation: insert at forced-aligned word gaps, choose the SNR range, simulate 5x. Its 95.5% tag correctness gives a realistic precision target for our auto-labels. The licence is NC, so reuse the *method*, not the data, unless the rules allow it.

### AudioSetCaps (arXiv 2024 [venue unverified]) — arXiv:2411.18953
- Read depth: full.
- **Key idea:** Prompt-chained LALM content extraction (Qwen-Audio-Chat) -> Mistral-7B caption -> **CLAP-based refinement**: regenerate if the caption scores below the label on audio similarity. 1.9M AudioSet captions (6M total).
- **Key numbers:** Removing refinement lowers retrieval R@1 39.7 -> 38.7 (T2A). The paper gives a qualitative example of removing absent speech and music claims.
- **Takeaway:** Cheap automatic hallucination filter: score each sentence of a candidate caption with CLAP or FLAM against the audio, and drop or regenerate low-scoring sentences. This is weak for paralinguistics, but OK for "Other sounds" and "Space".

### Factor-Conditioned Speaking-Style Captioning (Interspeech 2024 [venue unverified]) — arXiv:2406.18910
- Read depth: full.
- **Key idea:** Predict a fixed-format factor string first (gender, pitch, volume, speed), then the free caption. **Greedy-then-sampling**: greedy decoding for the factors, sampling for the prose.
- **Key numbers:** Factor accuracy 96.5% (GtS) vs StyleCap 76.8%. Diversity improves (distinct-2 0.051 -> 0.070).
- **Takeaway:** Use a two-part captioner output: a hidden, deterministic structured "facts" block (attribute: value, times) decoded greedily, then a free-text rendering. Strip the block before submission. This gives precision plus fluency, and makes the facts machine-checkable for the loop.

### TVPara (arXiv 2026) — arXiv:2610.19678
- Read depth: full.
- **Key idea:** A paralinguistic caption corpus in complex acoustic scenes (19 English TV series; 492 h single-utterance, 213 h multi-utterance). SALMONN pre-annotates, GPT-4o-mini polishes, and **humans correct**. After 50 h, the pre-annotator is re-fine-tuned and the correction rate drops from about 38% to about 17%.
- **Data/training recipe:** SALMONN and Qwen2.5-Omni-7B: frozen encoder, trained adapter, **LoRA r=8, alpha=32**, 10 epochs, LR 3e-6. The judge is GPT-5-mini (text-only, per attribute 0–4).
- **Key numbers:** +31.26% average relative gain. Gains are larger on clips with background sound (32.4% vs 19.9%). SALMONN volume correlation goes 0.03 -> 0.85, but **Qwen2.5-Omni volume stayed at about 0.03 even after fine-tuning**, which the authors attribute to its small adapter.
- **Takeaway:** (1) Iterated pre-annotate -> correct -> re-train cuts label error quickly. This is our round structure, with automatic verification standing in for humans. (2) Some attributes (loudness) may be **unlearnable through LoRA on the LLM alone if the adapter/encoder discards them**. So supply level, SNR and F0 as measured numbers (evidence sheet) rather than hoping the model learns them.

### StyleInstructCaps — A Benchmark for Controllable Speaking-Style Captioning (AACL 2026) — arXiv:2610.33036
- Read depth: full (first 100k characters).
- **Key idea:** 2.7k h on top of ParaSpeechCaps, with 6 caption types per utterance. The judge panel (Qwen3-32B, Gemma-4-31B, GPT-OSS-20B) scores metadata groundedness (1–10) and hallucination (0–10 plus severity).
- **Key numbers (meta-score):** Qwen3-Omni 5.75; AF3 3.88; Qwen2-Audio 3.62; MOSS-Audio 6.32; SALMONN 4.68 -> **7.35 after multi-task SSC SFT**. Hallucination column: Qwen3-Omni 3.86, AF3 6.43, Qwen2-Audio 7.00 (the scale direction is not certain from my read [unverified]; it appears higher = more hallucination). The judge panel agrees with the human majority on 85.9% of pairs (kappa 0.717).
- **Takeaway:** **Instruction-following does not equal grounded style perception.** Modest, instruction-diverse SSC SFT lifts even an old model above all untuned ones. An open-LLM judge panel is a credible, reproducible proxy for the Rime grader; use it for our internal eval and CIs.

---

## C. Benchmarks and evidence about listening vs. guessing

### MMAU (ICLR 2025) — arXiv:2410.19168
- Read depth: full (first 100k characters).
- **Key idea:** 10k MCQ, 27 skills, speech/sound/music. Test-mini has 1k items.
- **Key numbers:** Gemini Pro 1.5 52.97, Qwen2-Audio 52.50, humans 82.23 (test-mini). **Perceptual errors dominate: 55% (Qwen2-Audio) and 64% (Gemini)** of analysed errors.
- **Takeaway:** The bottleneck is perception, not reasoning. Invest in perception supervision (DSP and SED labels), not CoT.

### MMAU-Pro (AAAI 2026) — arXiv:2508.13992
- Read depth: full.
- **Key idea:** 5,305 items, 49 skills, including voice prosody, spatial, multi-audio, open-ended, and clips up to 10 min.
- **Key numbers:** Gemini 2.5 Flash 59.2, Qwen2.5-Omni-7B 52.2, AF3 51.7. With noise replacing audio: Qwen2.5-Omni 52.2 -> 30.6, but **AF3 only 51.7 -> 47.2**, i.e. it relies heavily on priors. Indian music is the hardest culture (39.4%).
- **Takeaway:** Use the "replace audio with noise" ablation as a standard check of our captioner. Captions that barely change under noise are prior-driven and will accumulate false items.

### MMAR (arXiv 2025 [venue unverified]) — arXiv:2505.13032
- Read depth: full (first 100k characters).
- **Key idea:** 1,000 items with Signal / Perception / Semantic / Cultural layers and CoT rationales.
- **Key numbers:** Best open is Qwen2.5-Omni-7B at 56.7; Gemini 2.0 Flash 65.6. **The Signal layer is worst** despite having the highest chance rate. Noise input: Qwen2.5-Omni 56.7 -> 36.3.
- **Takeaway:** Low-level signal properties (pitch, channel, reverb, bandwidth) are what LALMs are worst at, and exactly what our rubric's Voice and Recording axes ask for. Compute them with DSP rather than asking the LALM.

### AIR-Bench (ACL 2024 [venue unverified]) — arXiv:2402.07729
- Read depth: full.
- **Key idea:** 19k single-choice questions plus 2k open-ended chat items. **The GPT-4 judge sees meta-information, not audio**, and scores twice with swapped order to cancel position bias.
- **Key numbers:** Judge-human agreement 98.2% (foundation); pairwise consistency > 70% (chat).
- **Takeaway:** For our LLM-judge eval: score with references or metadata, swap positions, average. This mimics a text-only grader such as Rime's fixed grader LLM.

### Do Audio LLMs Really LISTEN, or Just Transcribe? (arXiv 2025) — arXiv:2510.10444
- Read depth: full.
- **Key idea:** LISTEN benchmark (7,939 items) with conflicting lexical vs acoustic emotion cues.
- **Key numbers:** Qwen3-Omni-30B paralinguistic-only (nonverbal) 21.0% vs 10% chance. Qwen2.5-Omni drops from 34.0% (audio) to 19.8% when text is added on neutral-text items. There is a strong "neutral" default.
- **Takeaway:** Do not let the captioner assert emotion or intent labels from words alone. For Hindi and Tamil, the model barely understands the words anyway, so emotion claims will default to neutral or be guessed. Prefer acoustic descriptors (F0 range, rate, intensity) plus cautious intent statements.

---

## D. Hallucination mitigation

### Can Large Audio-Language Models Truly Hear? (MATCH) (arXiv 2024 [venue unverified]) — arXiv:2410.16130
- Read depth: full.
- **Key idea:** Hallucination tasks for object existence, temporal order and attribute. **MATCH:** describe the audio first, then answer in a second turn.
- **Key numbers:** Qwen2-Audio object-existence F1 20.5 -> 63.8 with MATCH.
- **Takeaway:** Two-pass inference helps. Pass 1: dense description. Pass 2: targeted yes/no verification questions per candidate claim ("Is there a laugh between 3 and 4 s?"). Keep only claims that survive.

### Audio-Aware Decoding (AAD) (arXiv 2025) — arXiv:2506.07233
- Read depth: full.
- **Key idea:** Contrastive decoding: logits(audio) x (1+alpha) - alpha x logits(silence), plus a "focus on the audio" prefix.
- **Key numbers:** Object-hallucination F1 +0.046 to +0.428 (SALMONN-7B random split 0.233 -> 0.737 at alpha=1). Clotho-AQA also improves. Cost: about +60% inference time (+19% when parallelised).
- **Takeaway:** This is a training-free knob for the captioner, but it is tested only on yes/no QA. Use it in the verification pass (yes/no), not for long free captions.

### TAD: Token-Adaptive Contrastive Decoding (arXiv 2026) — arXiv:2609.07286
- Read depth: abstract only.
- **Key idea:** Applies the audio-vs-silence contrast only at decision-critical (first or affirmative) tokens, with confidence gating.
- **Key numbers:** +0.059 to +0.117 F1 over AAD (Qwen2) on AudioCaps-Hallucination.
- **Takeaway:** If using contrastive decoding in yes/no verification, gate it on the answer token only.

### BRACE: Benchmark for Robust Audio Caption Quality Evaluation (arXiv 2025) — arXiv:2512.10403
- Read depth: full (first 100k characters).
- **Key idea:** Caption-quality and hallucination-detection (noun-swap) benchmark for reference-free metrics.
- **Key numbers:** Best CLAP-based score on BRACE-Main is 70.01 F1. Hallucination detection: best CLAP 88.26, GPT-4o-audio 96.37, best open LALM (Qwen-Audio-Chat) 77.25. LALM judges show position bias.
- **Takeaway:** CLAP-style filters catch gross object swaps (about 88%) but not fine errors. Do not rely on CLAP for paralinguistic verification; use DSP measurements and targeted QA instead.

---

## E. Caption evaluation metrics

### FENSE / "Can Audio Captions Be Evaluated with Image Caption Metrics?" (ICASSP 2022 [venue unverified]) — arXiv:2110.04684
- Read depth: full.
- **Key idea:** Sentence-BERT similarity with a fluency-error penalty. Built the AudioCaps-Eval (1,671 pairs) and Clotho-Eval (1,750 pairs) human-preference sets.
- **Key numbers:** FENSE 85.3/75.7 vs CIDEr 71.0/63.2 pairwise accuracy. N-gram metrics can be gamed by padding.
- **Takeaway:** Not suitable for rubric-style grading. Use it only as a tie-breaker.

### CLAIR-A (arXiv 2024 [venue unverified]) — arXiv:2409.12962
- Read depth: full.
- **Key idea:** An LLM gives a 0–100 score plus a reason against the references, with FENSE as tie-breaker (epsilon 0.25).
- **Key numbers:** Clotho-Eval pair accuracy 79.7 vs FENSE 75.7. Its explanations are rated better (3.81 vs FENSE baseline).
- **Takeaway:** Our internal metric should be a **rubric-replica LLM judge** (Qwen3-8B or a larger open LLM), not CLAIR-A's holistic 0–100. Use item-level true/false checks with weights, same as Rime. Keep CLAIR-A-style "reason" outputs for failure analysis in the report.

---

## F. Indian-language resources relevant to the captioner

### VAANI: Capturing the language landscape for an inclusive digital India (arXiv 2026) — arXiv:2603.28714
- Read depth: abstract.
- **Key numbers:** 31,255 h speech, 2,043 h transcribed (about 6.5%), 105 languages, 165 districts. Image-prompted spontaneous speech. CC BY 4.0 (paper page).
- **Takeaway:** Most of the pool is untranscribed. Use IndicConformer or Whisper for transcripts and keep transcript confidence as a feature.

### VAANI Noise Event Dataset (arXiv 2026) — arXiv:2609.02474
- Read depth: full.
- **Key idea:** **Timestamped background-noise events on real Vaani speech**: 72,756 segments, 122.17 h, 106,892 events, 7 classes (non-speech human, animal, traffic, baby/child, music, alarm, appliance). Freelancer annotation with internal re-timestamping (a verified tier of 21.85 h) and a 10% audit.
- **Key numbers:** **Hindi 83.9 h / 47,080 segments; Tamil not mentioned.** No baselines. Dataset licence and release are not stated [unverified].
- **Takeaway:** This is the single most valuable in-domain supervision for the "Other sounds" axis with times. (1) Train or evaluate an SED or timestamp head on it. (2) Measure the round-0 captioner's event precision and recall on real Vaani audio. (3) Use its class prior to choose which events to splice synthetically for Tamil.

### Vaani Benchmark V1.0 (Hindi) (arXiv 2026) — arXiv:2606.21408
- Read depth: abstract.
- **Key idea:** Hindi spontaneous speech from 102 districts, each clip with 3 independent transcriptions. Multi-reference ASR evaluation shows that single-reference evaluation overstates errors.
- **Takeaway:** For the intelligibility metric and transcript-dependent claims, expect orthographic variation. Use multi-reference or normalised CER internally.

### Rasa: Expressive TTS for Indian languages (arXiv 2024 [venue unverified]) — arXiv:2407.14056
- Read depth: full.
- **Key idea:** Studio expressive speech (6 Ekman emotions plus neutral) for Assamese, Bengali and **Tamil** (Tamil expressive about 18.7 h, total 28.2 h).
- **Key numbers:** 1 h neutral + 0.5 h per emotion gives "Fair" MUSHRA (Tamil 57.30); 10 h + 3 h gives 68.66.
- **Licence:** released "for research and commercial purposes" (specific licence not named [unverified]).
- **Takeaway:** This is a source of *acted* Tamil emotion with known labels for captioner calibration (emotion and voice quality). It is studio-clean, so augment it with phone-channel simulation to match Vaani.

### Indic Parler-TTS (HF model card, ai4bharat/indic-parler-tts) — no arXiv paper
- Read depth: model card.
- **Key facts:** Apache-2.0 (gated). Hindi (107 h) and Tamil (52.25 h) training subsets. Descriptions control gender, rate, pitch, noise, reverberation ("close/distant"), expressivity, and emotion (Tamil yes, Hindi no). 69 named speakers.
- **Takeaway:** Its description vocabulary is a ready controllable-generation space. Generated samples with *known* description attributes can seed round-0 captioner SFT for Hindi and Tamil phonetics.

### IndicContextEval (arXiv 2026) — arXiv:2606.19157
- Read depth: search snippet only [details unverified].
- **Key facts:** 8 Indic languages (includes Hindi, **not Tamil**), 56 h, evaluates context use in audio LLMs.
- **Takeaway:** This confirms the gap: there is no public Hindi+Tamil paralinguistic captioning benchmark. Our test_set.zip is itself a contribution.

---

## G. Cheap fine-tuning of the Qwen3-Omni MoE (engineering evidence, not a paper)

### ms-swift Qwen3-Omni example scripts (modelscope/ms-swift, `examples/models/qwen3_omni/*.sh`, `examples/megatron/multimodal/omni/moe.sh`)
- **Facts (from script headers):** LoRA r=8, alpha=32, `target_modules all-linear`, `freeze_vit true`, `freeze_aligner true`, gradient checkpointing, max_length 4096. Memory: **2 x 48 GiB** with plain transformers device_map (batch 1, packing); 2 x 60 GiB with ZeRO-3; **2 x 50 GiB with Megatron expert-parallel 2** (`moe_grouped_gemm`, `moe_aux_loss_coeff 1e-3`).
- **Takeaway for 4x L4 (4 x 24 GB = 96 GB, PCIe):** BF16 LoRA of the 31.7B Captioner is *borderline* (about 64 GB of weights). Options:
  - (a) Attention-only LoRA as in TAC2, with the encoder frozen and short sequences: 30 s is about 375 audio tokens at 12.5 Hz, plus at most 600 text tokens.
  - (b) QLoRA on a 4-bit base: community AWQ checkpoints exist for inference, and bnb-4bit training on fused MoE experts is untested [unverified].
  - (c) Do ablations on 7–9B bases (Step-Audio-2-mini, MOSS-Audio-8B, Qwen2.5-Omni-7B), which fit LoRA on one L4 pair.
  - (d) Inference: the FP8 (Ada supports it) or AWQ Captioner with vLLM TP=4 for bulk labelling of the pool.

---

## Synthesis

**Papers read: 43 arXiv papers** (38 at method + results depth; 5 at abstract, card or snippet depth: TAD, MOSS-Audio, VAANI, Vaani Benchmark, IndicContextEval) plus HF model cards (Qwen3-Omni Captioner, AF-Next Captioner, MOSS-Audio, Indic Parler-TTS) and the ms-swift scripts.

### Top 8 actionable design takeaways
1. **Base model:** start from the Qwen3-Omni-30B-A3B-Captioner (Apache-2.0, recommended 30 s or less, no text prompt). Adapt it with **attention-only LoRA** (TAC2: r=512, about 2M clips, 10k steps; it beat the base on MMSU perception, 77.8 vs 63.5). Run a round-0 bake-off against Step-Audio-2-mini (paralinguistic 80.0, Apache-2.0) and MOSS-Audio-8B (speech-caption judge score 3.73 vs 3.60 for Qwen3-Omni, Apache-2.0) as cheap Pareto points.
2. **Numbers from DSP, not from the LALM:** LALMs are worst at the Signal layer (MMAR) and do not verbalise attributes they encode (TAC2 probing). Compute F0 (Hz and semitones), rate, pauses (ms), SNR, bandwidth and reverb with tools, and feed them as an "evidence sheet" (GAMA soft-prompt gains; LTU-AS DSP-built labels). ParaSpeechCaps thresholds turn the numbers into words.
3. **Timestamps:** synthetic splices with known RMS-derived spans, a 5x up-weighted timestamp-token loss (TAC), and audio-side time tokens with GRPO on event F1 (ASTP: SED event F1 48.9 -> 57.6). Qwen3-Omni's 80 ms frames are fine-grained enough for the +-250 ms window.
4. **Verify before writing:** use an Omni-Detective-style agent (Qwen3-8B querying the captioner, ASR, SED and DSP tools), then a MATCH-style yes/no check per claim, optionally with AAD/TAD contrastive decoding. Keep only claims that pass.
5. **Short, precise captions:** detail and hallucination grow together with length (Omni-Captioner). The rubric subtracts false items, so write only verified items and never hedge.
6. **Structured-then-prose output:** decode a hidden facts block greedily, then sample the prose (FCC: 96.5% factor accuracy). This makes captions machine-checkable for the loop and for DPO pairs (correct vs attribute- or time-swapped captions, as in AF2 negatives and Qwen2-Audio DPO).
7. **Curriculum plus abstention:** train perception targets before free captions (LTU: 50.3 vs 23.0 without the curriculum). Add about 5–10% "not determinable" or absent-event targets (refusal rate 51.9% -> 69.3%).
8. **In-domain Indic supervision:** Vaani Noise Events (Hindi 83.9 h, timestamped, 7 classes), Rasa Tamil emotions, and Indic-Parler generations with known descriptions. Use an open-LLM judge panel that replicates the rubric (StyleInstructCaps: 85.9% agreement with humans) for internal scores and bootstrap CIs.

### 3 biggest risks
1. **Prior-driven hallucination in a language the model does not know.** Qwen3-Omni lists no Hindi or Tamil speech input; LALMs "transcribe rather than listen" (LISTEN) and default to "neutral". Run noise-input ablations (MMAU-Pro) to catch false emotion and intent claims.
2. **Compute.** LoRA on the 31.7B MoE needs 2x48–60 GiB in reference scripts. 4x L4 over PCIe without NVLink is tight, and QLoRA on fused experts is unproven. Bulk labelling of thousands of hours also competes for the same GPUs.
3. **Loop confirmation bias and licences.** A captioner trained on its own or the generator's outputs can reinforce its own errors unless labels come from independent tools or transforms. AF3, AF-Next and CapSpeech are non-commercial or research-only, so their licences need a rules check before use.
