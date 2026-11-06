# Notes 02: Description/instruction-conditioned TTS and LM-based TTS (the generator side)

Cluster owner: lit-review agent. Date: 2026-11-04.
How I checked things: arXiv IDs were confirmed by downloading each PDF from arxiv.org/pdf/<id> and reading the abstract, method and results text. Licences were checked with the Hugging Face API (`cardData.license`) or the repo LICENSE file. "[unverified]" marks anything I could not confirm from a primary source. Numbers are copied from the papers. Where I derived a number myself, it says so.

Brief constraints that matter most here:
- Hindi and Tamil.
- Output must be >= 24 kHz.
- 10 samples per description, scored for speaker diversity with a fixed SV model.
- Timed items in descriptions must be within +-250 ms.
- Open models only.
- Hardware: 4x L4 24 GB.

---

## A. Backbone candidates (focus Q1)

### Qwen3-TTS Technical Report (Qwen Team, tech report 2026) — arXiv:2601.15621
- **Key idea:**
  - Qwen3 LM backbone with a "dual-track" layout: text and acoustic tokens are concatenated along the channel axis, so speech can stream as text arrives.
  - Two tokenizers:
    - **12Hz:** 12.5 Hz, 16 codebooks of size 2048. Codebook 0 is semantic, distilled from WavLM; the other 15 are acoustic RVQ. Fully causal ConvNet decoder.
    - **25Hz:** single codebook built on Qwen2-Audio, with a block-wise DiT plus BigVGAN decoder.
  - In the 12Hz model, the backbone predicts codebook 0 and an MTP module predicts the 15 residual codebooks.
  - A speaker encoder is trained jointly with the backbone. Cloning works either from a speaker embedding (x-vector-like) or by in-context prompting with a text-speech pair.
  - Instructions are prepended in ChatML format. A "probabilistically activated thinking pattern" is used during training to improve following of complex voice descriptions.
- **Data/training recipe:**
  - More than 5M hours across 10 languages.
  - Pre-training in three stages: S1 general; S2 high-quality continued pre-training (CPT) to cut hallucination; S3 long-context, raising max length from 8,192 to 32,768 tokens.
  - Post-training: DPO on human preference pairs, then GSPO with rule-based rewards, then lightweight speaker fine-tuning.
  - The report does **not** describe how the voice-design or instruction data was collected or annotated.
- **Key numbers:**
  - Seed-TTS WER (12Hz-1.7B-Base): zh 0.77, en 1.24.
  - InstructTTSEval voice design (12Hz-1.7B-VD): ZH APS 85.2 / DSD 81.1 / RP 65.1; EN APS 82.9 / DSD 82.4 / RP 68.4.
  - Same benchmark, EN: Parler-TTS-large 64.3 / 47.2 / 31.4, VoxInstruct 54.9 / 57.0 / 39.3.
  - First-packet latency 97 ms (0.6B) and 101 ms (1.7B).
  - Tokenizer output is 24 kHz (from the HF config: `output_sample_rate: 24000`, `encode_downsample_rate: 1920`).
  - My own calculation: 16 × 11 bits × 12.5 Hz ≈ 2.2 kbps.
- **Languages:** zh, en, de, it, pt, es, ja, ko, fr, ru. **No Hindi and no Tamil.**
- **Open weights + licence:**
  - Released checkpoints: Base, VoiceDesign and CustomVoice (12Hz, 1.7B), plus Base and CustomVoice (0.6B); the 12Hz tokenizer. All Apache-2.0.
  - CustomVoice has 9 preset speakers: zh ×5, en ×2, ja ×1, ko ×1.
  - The official `finetuning/` folder supports **single-speaker SFT only**. JSONL fields are `audio`, `text`, `ref_audio`; there is no `instruct` field. Example command: `sft_12hz.py`, lr 2e-6, batch 32. Multi-speaker training is "future".
  - vLLM-Omni supports offline inference.
- **Takeaway for our Track 2 design:**
  - This is the best licence/quality/latency fit, and it outputs 24 kHz.
  - 12.5 Hz means a 30 s clip is only 375 frames, so sequences are short and training on L4s is feasible.
  - Hindi and Tamil need language-adaptive continued pre-training. We must also write our own instruction-SFT script (add `instruct` to the ChatML prefix).
  - Before committing:
    - Measure tokenizer resynthesis CER on Vaani Hindi/Tamil with IndicConformer.
    - Measure Qwen BPE token counts on Tamil script.
  - CustomVoice (the brief's round-0 suggestion) has only 9 voices. Our speaker diversity score would be capped near the number of preset voices the SV model counts as distinct (≤9 of 10 per description), and only if instructions do not collapse them. So the diversity score needs the Base model's speaker-embedding path or VoiceDesign.

### Indic Parler-TTS (AI4Bharat + HF, model card 2024) — no arXiv; huggingface.co/ai4bharat/indic-parler-tts
- **Key idea:** Parler-TTS (Mini v1 architecture) fine-tuned on Indic data. The description is free text naming gender, pitch, rate, expressivity, noise, reverb, quality and emotion. There are also "named speakers" for consistency.
- **Data/training recipe:**
  - 1,806 h of Indic and English speech: GLOBE 535 h, IndicTTS 382 h, LIMMITS 568 h, Rasa 288 h.
  - Descriptions come from the Data-Speech pipeline (binned signal features rewritten by an LLM).
- **Key numbers:**
  - 0.9B params.
  - 21 official languages, including Hindi and Tamil.
  - Named speakers: Hindi 4, Tamil 2 (69 in total).
  - 12 emotions (official in 10 languages).
  - Native-speaker score, pretrained → fine-tuned: Hindi 83.43 → 84.79; Tamil 69.68 → 75.48.
  - The card does not state the sampling rate. Parler Mini v1 uses 44.1 kHz DAC, so the Indic variant presumably does too [unverified for the Indic checkpoint; the config is gated].
- **Open weights + licence:**
  - Apache-2.0, gated with automatic approval.
  - Full training code (`parler-tts/training`, `run_parler_tts_training.py`) and a mono-speaker fine-tuning notebook.
  - Data-Speech annotation code is public.
- **Takeaway:**
  - Strongest **day-0 Hindi+Tamil description TTS**, with a complete open training stack. Use it as the round-0 baseline and fallback generator.
  - Weaknesses:
    - Descriptions are tag-like and coarse; there are no timed events.
    - Tamil quality is weaker.
    - DAC at 86 Hz × 9 codebooks gives long sequences (a 30 s clip is about 2,580 frames).
    - The voice is random given the description, with no explicit control over speaker identity. That helps diversity but hurts consistency.

### Natural language guidance of high-fidelity TTS with synthetic annotations (Lyth & King, arXiv 2024) — arXiv:2402.01912
- **Key idea:**
  - Label speaker, style and channel automatically, then train a codec LM (adapted from AudioCraft).
  - The transcript is prepended; the description goes in via cross-attention.
  - No reference audio or speaker embedding is used.
  - DAC codec: 44.1 kHz, 9 codebooks, 86 Hz.
- **Data/training recipe:**
  - Data: MLS-English (~45k h) plus LibriTTS-R (585 h).
  - Labels:
    - gender from metadata;
    - accent from a classifier;
    - pitch mean (relative to gender), pitch std, speaking rate, SNR and C50 (reverb).
  - Each continuous variable is split into **7 bins**, each with a phrase (e.g. "very fast").
  - "Very good/bad recording" is added when SNR and C50 are both in the extreme bins.
  - Stable Beluga 2 turns the keywords into sentences.
- **Key numbers:**
  - Gender accuracy 94%; accent 68%; poor control of C50.
  - MOS 3.92 vs Audiobox 2.79 vs ground truth 3.67.
  - Description relevance 3.88 vs 3.19 vs 3.62.
  - SQUIM PESQ 3.84.
  - Adding the small clean LibriTTS-R set (about 1% of data) drove the gain in fidelity.
- **Open weights + licence:** Parler-TTS Mini v1 (880M) and Large v1 (2.3B), Apache-2.0, with full data and training code.
- **Takeaway:**
  - Template recipe: binned DSP features + LLM rewrite, with a small clean subset for fidelity.
  - Reverb (C50) is hard to control from text. This argues for **rendering the recording axis by DSP after generation** rather than asking the model to learn it.

### CosyVoice 2 (Du et al., tech report 2024) — arXiv:2412.10117
- **Key idea:**
  - Supervised semantic tokenizer with FSQ, 25 Hz, inside the SenseVoice-large encoder.
  - The Qwen2.5-0.5B LLM predicts tokens; a chunk-aware causal flow-matching model converts them to mel, then a vocoder produces audio.
  - Instructions are prepended before `<|endofprompt|>`.
- **Data/training recipe:**
  - Tokenizer data: zh 110,884 h, en 99,918 h.
  - TTS data: zh 130k h, en 30k h, plus ja/ko.
  - 1,500 h of instruction data:
    - natural-language instructions (emotion, rate, dialect, role-play);
    - fine-grained **inline vocal bursts `[laughter]`, `[breath]`**;
    - span tags `<laughter>…</laughter>` and `<strong>…</strong>`.
  - Multi-speaker SFT with a `Speaker A<|endofprompt|>` prefix (`unknown` when unlabelled), lr 1e-5.
  - DPO using WER and speaker similarity (SS) to pick preferred and rejected samples.
- **Key numbers:**
  - Instruction test (zh, 290 items, 29 instruction types): CER 1.52, SS 0.804, NMOS 3.94, MOS-I 4.06.
  - Without instructions: MOS-I 2.28. So instruction control does not emerge from content text alone.
  - The tokenizer generalised zero-shot to ja/ko, but ja CER was 18.79 because of shared characters with Chinese.
- **Open weights + licence:**
  - CosyVoice2-0.5B, Apache-2.0.
  - Training recipe in `examples/libritts`.
  - GRPO recipe added Aug 2025, contributed by NVIDIA.
- **Takeaway:**
  - Inline vocal-burst tokens and span tags are the simplest proven way to place laughs and breaths in time.
  - The speaker-tag prefix plus "unknown" is a cheap way to mix speaker-labelled Vaani data with unlabelled data.

### CosyVoice 3 (Du et al., tech report 2025) — arXiv:2505.17589
- **Key idea:**
  - New tokenizer built on the MinMo voice encoder plus FSQ, trained with multi-task supervision (ASR, LID, SER, audio event detection, speaker analysis), so the tokens carry prosody, emotion and events.
  - DiffRO: Gumbel-softmax lets rewards from a Token2Text ASR model and other heads (SER, MOS, AED) be optimised directly on tokens.
  - Pronunciation inpainting and self-training for text normalisation.
- **Data/training recipe:**
  - 1M hours: 9 languages and 18 Chinese dialects, from in-the-wild sources.
  - Pipeline: diarisation and segmentation → denoising → ASR with LID (FasterWhisper) → punctuation adjustment → volume normalisation → filtering on text-length ratio.
  - 5,000 h of instruction data with more than 100 style types.
  - SFT with partial labels: "You are Speaker A. Please talk to me happily." Speaker and style prompts are randomly masked.
  - Polyglot SFT: monolingual speakers are taught other languages using an auxiliary studio-quality dataset with speaker ID and language ID given in the instruction.
- **Key numbers:**
  - Model sizes 0.5B and 1.5B.
  - Released: Fun-CosyVoice3-0.5B-2512 base plus an RL variant (Dec 2025), Apache-2.0.
  - Languages: zh, en, ja, ko, de, es, fr, it, ru. **No Indic.**
- **Takeaway:**
  - The best alternative backbone with an open training recipe, RL recipe, and `[laughter]`/`[breath]` support.
  - The supervised multi-task tokenizer is attractive because events and emotion survive tokenisation.
  - Its 25 Hz rate gives twice the frame count of Qwen 12.5 Hz, though there is only one codebook per frame.
  - The "random masking of speaker/style prompt" trick lets one model handle both description-only and speaker-specified generation.

### Spark-TTS (Wang et al., arXiv 2025) — arXiv:2503.01710
- **Key idea:**
  - BiCodec: 50 TPS semantic tokens plus **32 fixed-length global tokens** for speaker attributes.
  - Qwen2.5-0.5B LLM.
  - Chain-of-thought generation: attribute labels (gender, pitch level, speed level) → fine-grained values (pitch in Mel, syllables per second) → global tokens → semantic tokens.
  - Without labels, global tokens come from a reference, which gives zero-shot cloning.
- **Data/training recipe:**
  - VoxBox: 100k h, zh+en, from open datasets.
  - Annotations: gender, pitch, speed, age, emotion.
  - Pitch and speed are each binned into 5 levels by percentile.
  - BiCodec trained on ~3k h at 16 kHz.
- **Key numbers:** gender control accuracy 99.77% vs Parler 98.12% vs VoxInstruct 82.99%.
- **Open weights + licence:** Spark-TTS-0.5B is **CC-BY-NC-SA-4.0** (HF). Code is on GitHub.
- **Takeaway:**
  - Generating the speaker identity first (global tokens), conditioned on the description, then the content, separates "who" from "what was said".
  - Sampling the global tokens gives speaker diversity per description.
  - However, the 16 kHz codec fails our ≥24 kHz requirement, and the NC licence is a problem.

### Llasa (Ye et al., arXiv 2025) — arXiv:2502.04128
- **Key idea:**
  - Single Llama-style Transformer over a single-codebook X-codec2 (one VQ, 65,536 codes, 50 tokens/s).
  - Studies scaling of both training-time and inference-time compute.
  - Inference-time search (best-of-N, beam-like) with speech understanding models as verifiers (speaker similarity, emotion, ASR).
- **Data/training recipe:** 250k h zh+en. Models at 1B, 3B and 8B (from Llama 3.2/3.1).
- **Key numbers:** inference-time scaling shifts outputs toward the verifiers' preferences and improves emotion, timbre consistency and content accuracy (qualitative summary from the abstract).
- **Open weights + licence:** Llasa-1B/3B **CC-BY-NC-4.0**. Training and codec code are open. X-codec2 runs at 16 kHz.
- **Takeaway:**
  - Verifier-guided best-of-N is directly usable: score N candidates with our captioner, IndicConformer CER and an SV model, then keep the best.
  - This costs compute at inference time only, which suits limited L4 training budgets.
  - The backbone itself is unsuitable (16 kHz output and NC licence).

### MiniMax-Speech (MiniMax, tech report 2025) — arXiv:2505.07916
- **Key idea:**
  - AR transformer with a **learnable speaker encoder** trained jointly. It needs no transcript of the reference, so it is cross-lingual.
  - Flow-VAE decoder.
  - **Text-to-Voice (T2V):** a compact timbre-generation model maps a natural-language description plus discrete attributes (rate, gender, language, pitch in 6 bins, volume) to a **PCA-compressed 128-d timbre vector**.
  - Training uses random masking of key words in the description.
- **Data/training recipe:** 32 languages. Data sizes are not given.
- **Key numbers:** SOTA objective cloning WER/SIM claimed; #1 on TTS Arena at the time (claims, not re-checked).
- **Open weights + licence:** closed (commercial).
- **Takeaway:**
  - Best template for **speaker diversity**: learn a separate, sampleable prior p(timbre | description) in the speaker-embedding space of a cloning model.
  - With Qwen3-TTS, whose speaker encoder is jointly trained, we can fit a conditional prior (GMM or small flow) on embeddings of Vaani's many speakers, conditioned on description attributes.

### IndexTTS2 (Zhou et al., arXiv 2025) — arXiv:2506.21619
- **Key idea:**
  - AR text-to-semantic model with an optional **target token count** for exact duration control, plus free-running mode.
  - Emotion and speaker are separated with a gradient-reversal layer (GRL).
  - "Soft instruction": a fine-tuned Qwen3 maps a text description to a probability over 7 emotions, which weights a set of emotion embeddings.
  - Three-stage training.
- **Data/training recipe:**
  - 55k h (30k zh + 25k en), mostly Emilia.
  - Emotional subset: 135 h from 361 speakers.
- **Key numbers:** token-number error rate for duration control below 0.02% at the original duration and below 0.03% when scaled (Table 4).
- **Open weights + licence:** **bilibili Model Use License Agreement** (custom). Derivatives, including fine-tunes, fall under it. Not Apache.
- **Takeaway:** explicit token-count conditioning is a clean way to hit timed spans per segment. At 12.5 Hz, one frame is 80 ms, well inside the ±250 ms tolerance. We can add a duration or length token to our segment-wise generation.

### Step-Audio-EditX (StepFun, tech report 2025) — arXiv:2511.03601
- **Key idea:**
  - 3B audio LLM, initialised from a text LLM, over dual-codebook tokens (16.7 Hz linguistic with 1024 codes and 25 Hz semantic with 4096 codes, interleaved 2:3).
  - Does zero-shot TTS and **iterative editing** of emotion, style and paralinguistics, with no disentangling modules.
  - The control comes from **large-margin synthetic pairs**.
- **Data/training recipe:**
  - 200k h of high-quality speech.
  - Emotion and style triplets: voice actors record about 10 s per emotion/style; zero-shot cloning produces neutral and emotional versions of the same text; a margin scorer (1–10) keeps pairs scoring ≥6.
  - Paralinguistic quadruplets: NVSpeech audio with tags (target) versus a TTS re-synthesis of the same text with tags removed (input).
  - RL: human pairs with margin >3 on a 5-point scale, and LLM-judge pairs with margin >8 on a 10-point scale → reward model → PPO.
- **Key numbers:** beats MiniMax-2.6-hd and Doubao-Seed-TTS-2.0 on emotion editing (claim). 10 paralinguistic tag types (model card).
- **Open weights + licence:** code and model on GitHub/HF. The repo LICENSE is Apache-2.0; the HF card has no licence field [check weights licence before use].
- **Takeaway:**
  - The "edit" formulation (input = clean TTS audio, output = audio with a laugh or breath at a position) is a strong way to **insert events at exact times** after generation.
  - The large-margin pair recipe matches our captioner-as-judge loop: keep only pairs with clear differences.

### F5-TTS (Chen et al., arXiv 2024; venue [unverified]) — arXiv:2410.06885
- **Key idea:**
  - Non-autoregressive flow matching (DiT).
  - Text is a character sequence padded with filler tokens to the mel length and refined by ConvNeXt V2. No duration model and no phoneme alignment.
  - Trained on text-guided **speech infilling**.
  - "Sway sampling" of flow steps at inference.
- **Data/training recipe:** Emilia, about 95k h zh+en.
- **Key numbers:** RTF 0.15.
- **Open weights + licence:** F5-TTS weights **CC-BY-NC-4.0**, inherited from Emilia. Code is MIT.
- **Takeaway:**
  - The infilling objective lets us regenerate or insert a span at an exact time in a clip.
  - Total length is chosen by the user, so global duration is set directly.

### IndicF5 (AI4Bharat, model card 2025) — no arXiv; huggingface.co/ai4bharat/IndicF5
- **Key idea:** F5-TTS-style model for 11 Indic languages, including Hindi and Tamil. **Reference audio plus its transcript are required.**
- **Data/training recipe:** about 1,417 h from Rasa, IndicTTS, LIMMITS and IndicVoices-R.
- **Key numbers:** 24 kHz output.
- **Open weights + licence:** **MIT** (HF), gated with auto-approval. No fine-tuning instructions on the card. The card now points to a newer model, "Indic-Speak" (22 languages) [not examined].
- **Takeaway:**
  - A permissively licensed Hindi/Tamil **renderer for "design-then-clone"**: a designed or sampled reference voice goes in, Hindi/Tamil speech in that voice comes out.
  - It also offers infilling for timed edits.
  - A strong fallback if adapting Qwen3-TTS to Hindi/Tamil fails.

### MaskGCT (Wang et al., ICLR 2025) — arXiv:2409.00750
- **Key idea:**
  - Fully non-autoregressive, two-stage masked generative model: text → semantic tokens (from an SSL model), then semantic → acoustic tokens.
  - Total length is specified at inference; no explicit alignment.
- **Data/training recipe:** 100k h of in-the-wild speech (Emilia).
- **Key numbers:** claims SOTA zero-shot quality, similarity and intelligibility at the time.
- **Open weights + licence:** amphion/MaskGCT, **CC-BY-NC-4.0**.
- **Takeaway:** setting the length directly gives duration control for segment-wise rendering. Not usable as our final model because of the NC licence.

### Seed-TTS (ByteDance, tech report 2024) — arXiv:2406.02430
- **Key idea:**
  - AR LM plus a diffusion stage; there is also a fully DiT variant.
  - **Self-distillation for timbre separation:** perturb the speaker in the diffusion stage to make pairs with the same content and prosody but different timbre, then retrain so timbre comes only from the timbre reference.
  - RL (REINFORCE/DPO-style) with WER, SIM and SER rewards.
  - Instruction fine-tuning for emotion.
- **Data/training recipe:** large in-house data. No weights released.
- **Key numbers:** emotion control accuracy improves with instruction fine-tuning versus speaker SFT alone (Table 4, qualitative here).
- **Open weights + licence:** closed. The seed-tts-eval test sets are public.
- **Takeaway:**
  - Synthetic "same prosody, different timbre" pairs are a cheap way to separate speaker from style.
  - That separation is what lets 10 samples of one description vary in speaker while holding the described style fixed.
  - RL with ASR, SV and SER rewards fits our loop.

### VoiceCraft (Peng et al., ACL 2024) — arXiv:2403.16973
- **Key idea:**
  - Token-infilling neural-codec LM (Encodec RVQ).
  - "Causal masking + delayed stacking" rearrangement allows generation inside an existing sequence.
  - Does both speech editing and zero-shot TTS on in-the-wild data; introduces the RealEdit benchmark.
- **Data/training recipe:** GigaSpeech [size per paper; not re-checked].
- **Key numbers:** edited speech is nearly indistinguishable from unedited in human tests (abstract).
- **Open weights + licence:** weights released [licence unverified; HF API returned none].
- **Takeaway:**
  - Mid-utterance infilling is the codec-LM way to put a laugh or a style change at a timestamp.
  - IndicVoices-R showed VoiceCraft can be fine-tuned to Indian languages (see below).

### UniAudio (Yang et al., ICML 2024) — arXiv:2310.00704
- **Key idea:**
  - One LLM for 11 audio-generation tasks (TTS, VC, instructed TTS, sound, music, singing…).
  - Each task is a source-target token sequence.
  - A multi-scale transformer handles long RVQ sequences.
- **Data/training recipe:** 165k h of audio; 1B params.
- **Key numbers:** SOTA or competitive on most of the 11 tasks (abstract).
- **Open weights + licence:** code and demo released [weights licence unverified].
- **Takeaway:**
  - Supports the "one unified model" option the brief allows (captioner and generator in one network, like UALM).
  - But multi-task training at this scale is out of reach on 4× L4. Prefer two models plus a shared LLM.

### Audiobox (Vyas et al., Meta, arXiv 2023) — arXiv:2312.15821
- **Key idea:**
  - Flow-matching unified model for speech and sound.
  - Conditions on transcript, masked audio context (infilling), a **description** and an optional **voice prompt**.
  - The voice prompt is chosen *adversarially*: same speaker, but differing in emotion, environment or rate, and RIR- and noise-augmented. It therefore transfers only vocal timbre, while the description sets emotion and acoustics.
  - Introduces Joint-CLAP for description–audio relevance.
- **Data/training recipe:**
  - Over 160k h of speech, 20k h of music, 6k h of sound.
  - Automatic speech captions:
    - classifier/metadata tags (age 4 classes, gender, quality 3, pitch 3, rate 3, open-vocabulary accent, emotion and environment);
    - LLaMA2-7B writes captions using a **style bank of writing personas**;
    - random RIR plus tagged background noise is applied and the caption is updated to match (quality set to "low" when noise is added).
  - 500 h of human-written captions; annotators were filtered on gold samples plus LLM rating.
- **Key numbers:**
  - Zero-shot TTS similarity 0.745 on LibriSpeech; FAD 0.77 on AudioCaps.
  - Bespoke solvers are more than 25× faster.
- **Open weights + licence:** model not openly released [unverified]. Watermarking was evaluated.
- **Takeaway:** the closest published recipe to our needs.
  - (i) "augment, then rewrite the caption" gives free, verified labels for the recording axis.
  - (ii) Adversarial voice-prompt selection separates timbre from style.
  - (iii) The persona style bank gives free-form caption diversity.

### Fugatto 1 (Valle et al., NVIDIA, ICLR 2025) — OpenReview B2Fqu7Y2cd (no arXiv found)
- **Key idea:**
  - Generalist audio model (flow matching / transformer; 0.8B, 1.4B and 2.5B studied) with free-form instructions and optional audio inputs.
  - **ComposableART:** compositional classifier-free guidance that combines, interpolates or negates instructions, possibly across separately trained models. For example, speech plus a background event.
- **Data/training recipe:** five-part dataset generation.
  - (I) An LLM writes *python instruction generators* for each task.
  - (II) Absolute and relative instructions.
  - (III) Audio-understanding models write synthetic captions; for speech, predicted attributes are filled into LLM-written templates.
  - (IV) Transmutation pairs from datasets where one factor varies and others are fixed (e.g. RAVDESS emotions by the same speaker).
  - (V) **Praat/Pedalboard controlled transforms** for exact paired labels ("increase F0 variance slightly…", "add moderate reverb").
  - At least 20M rows and at least 50k h, all from open data.
- **Key numbers:** WER near ground truth on LibriSpeech in-context TTS; competitive with specialist models (Table 2).
- **Open weights + licence:** weights not released [unverified].
- **Takeaway:**
  - The brief directly cites Fugatto-style descriptions. Its recipe (LLM-generated instruction programs plus DSP transforms with known values) is our cheapest source of *exact* numeric labels: semitone shifts, reverb, SNR, codec, splice times.
  - ComposableART-style guidance can mix "speech" and "event/background" conditions at inference.

---

## B. Earlier description-conditioned TTS (lineage, data recipes)

### PromptTTS (Guo et al., ICASSP 2023) — arXiv:2211.12171
- **Key idea:** a text prompt containing style and content goes to a style encoder and a content encoder, then a speech decoder.
- **Data/training recipe:** released the PromptSpeech dataset of prompts paired with speech. Attributes include gender, pitch, speed, volume and emotion. The data uses voices from a commercial TTS plus real speech [details per paper].
- **Key numbers:** attribute accuracy is reported in the PromptTTS 2 table: gender 98.01, speed 89.66, volume 92.49, pitch 85.98, mean 91.54.
- **Open weights + licence:** dataset released; model weights [unverified].
- **Takeaway:**
  - A style encoder over a fixed attribute set saturates quickly.
  - This is also the "one-to-many" problem: the description does not fix the voice, so samples collapse to similar voices (similarity 0.77–0.80; see PromptTTS 2).

### PromptTTS 2 (Leng et al., ICLR 2024) — arXiv:2309.02285
- **Key idea:**
  - A **variation network**: diffusion over reference-speech query embeddings (fixed-length, via learnable queries), conditioned on the prompt embedding.
  - At inference, sampling the variation network gives *different voices that all satisfy the prompt*. Reference speech is used only during training.
- **Data/training recipe:**
  - MLS-English, 44k h.
  - Prompts come from an SLU-plus-LLM pipeline: SLU tags gender, pitch, speed and volume.
  - The LLM writes per-attribute keywords, then sentences with **placeholders** ("[Gender]"), then combines them, then fills the placeholders.
  - Prompts can be reused across utterances with the same labels.
- **Key numbers:**
  - Attribute accuracy mean 93.33 vs PromptTTS 91.54 and InstructTTS 91.47.
  - **WavLM-TDNN similarity among 5 samples:**
    - varying only the variation-network sample: **0.355**;
    - varying the text prompt wording: 0.775;
    - varying text content: 0.873;
    - varying the TTS backbone sample: 0.914.
  - Baselines: 0.77–0.80.
- **Open weights + licence:** code in Microsoft repo [weights unverified].
- **Takeaway:**
  - **The most direct evidence for our speaker diversity score.** An explicit, sampleable latent for "what the description leaves free" gives large voice variation (similarity 0.355) while keeping attribute accuracy.
  - Plain sampling of the TTS model does not.
  - Our version: a description-conditioned prior over speaker embeddings.

### InstructTTS (Yang et al., submitted to TASLP 2023; final venue [unverified]) — arXiv:2301.13662
- **Key idea:**
  - Natural-language style prompts are encoded with a three-stage-trained sentence encoder (self-supervised plus cross-modal metric learning).
  - Discrete diffusion over VQ acoustic tokens.
  - Mutual-information minimisation separates style from speaker and content.
- **Data/training recipe:** in-house Chinese corpus with free-form style descriptions (the paper calls it NLSpeech, per ParaSpeechCaps' related work).
- **Key numbers:** attribute accuracy mean 91.47 (as reported in PromptTTS 2).
- **Open weights + licence:** [unverified].
- **Takeaway:** contrastive alignment between description and audio embeddings (CLAP-like) is useful as a *relevance reward* and as the description encoder. MI/GRL separation is how style stays free of speaker.

### TextrolSpeech / Salle (Ji et al., ICASSP 2024) — arXiv:2308.14430
- **Key idea:** VALL-E-style codec LM conditioned on a natural-text style prompt.
- **Data/training recipe:** 236,220 pairs of speech and style prompt, each with 5 style factors (gender, pitch, speed, volume, emotion). Descriptions were written by GPT through multi-stage prompting.
- **Key numbers:** "comparable" controllable-TTS performance (abstract only).
- **Open weights + licence:** dataset public [model licence unverified].
- **Takeaway:**
  - Early proof that a plain codec LM with a prepended description works.
  - Five-factor captions are far below our rubric's richness, so our captions must cover the timed and recording axes.

### VoxInstruct (Zhou et al., ACM MM 2024) — arXiv:2408.15676
- **Key idea:**
  - One instruction mixing content and description ("say X in a sad voice…").
  - An MT5 encoder, then a LLaMA-style codec LM that first predicts **HuBERT semantic tokens** (to pull out content), then Encodec acoustic tokens, decoded with Vocos.
  - Several classifier-free guidance strategies.
  - Can combine a speech prompt with a description.
- **Data/training recipe:** zh+en mixed corpora with descriptions [hours not re-checked].
- **Key numbers:**
  - Gender accuracy 82.99% (from the Spark-TTS table).
  - InstructTTSEval EN APS/DSD/RP 54.9 / 57.0 / 39.3 (Qwen3-TTS Table 8).
- **Open weights + licence:** code and model on GitHub thuhcsi/VoxInstruct [licence unverified].
- **Takeaway:**
  - CFG on the description is a cheap way to strengthen instruction relevance; we can apply it to any AR model by dropping the description during training.
  - Mixing content and description in one string hurts accuracy compared with separate fields; keep them separate.

### EmoVoice (Yang et al., ACM MM 2025) — arXiv:2504.12867
- **Key idea:**
  - Qwen2.5-0.5B LLM outputs 50 Hz CosyVoice semantic tokens, then flow matching and a vocoder.
  - Free-style emotion descriptions.
  - "Phoneme boost" variant predicts phoneme tokens in parallel with audio tokens (CoT/CoM-style) to improve content accuracy.
- **Data/training recipe:**
  - Pre-trained on CosyVoice-synthesised data.
  - Emotional fine-tuning on **EmoVoice-DB: 40 h of English synthesised with GPT-4o-audio**, with fine-grained natural-language emotion descriptions.
  - "SOTA using only synthetic data."
- **Key numbers:** SOTA on the EmoVoice-DB test set and the Chinese Secap test set (claim).
- **Open weights + licence:** dataset, code and checkpoints on GitHub [licence unverified].
- **Takeaway:**
  - Synthetic data from a strong generator is enough to teach description control. This is exactly our round-1+ loop.
  - Our data source must be open (Qwen3-TTS / Indic-Parler / IndicF5), not a closed API, to stay rule-compliant and defensible.

### CapSpeech (Wang et al., arXiv 2025) — arXiv:2506.02863
- **Key idea:** benchmark and corpus for caption-conditioned TTS, including **CapTTS-SE (sound events in the transcript)**, accent, emotion and agent TTS.
  - Event tags are inline, e.g. `<telephone>`, `<knock>`, with `<B>…</B>` (background) and `<I>…</I>` (inserted) spans.
- **Data/training recipe:**
  - More than 10M machine-annotated and about 0.36M human-annotated caption pairs.
  - **SE simulation:**
    - LibriTTS-R plus 394 event classes from VGGSound, FSDKaggle2018 and ESC-50;
    - insertion mode (clean events) or background mode (noisy events);
    - **MFA alignment chooses insertion points between words with ≥0.3 s gap** (start, middle or end);
    - mixed at SNR −3 to 6 dB;
    - each utterance simulated 5×.
  - Models: Parler-TTS (AR) and F5-TTS (NAR) fine-tuned.
- **Key numbers:** high fidelity and intelligibility across styles (abstract).
- **Open weights + licence:** data released under **CC BY-NC 4.0** (paper).
- **Takeaway:**
  - A copyable recipe for timed non-verbal and event data with exact timestamps from alignment.
  - Do the same with Vaani: forced alignment (or IndicConformer timestamps) → splice laughs, coughs and noises at known times → captions say "laugh at 3.2–3.9 s".
  - Rebuild it ourselves rather than reuse it, because of the NC licence.

### ParaSpeechCaps (Diwan et al., arXiv 2025) — arXiv:2503.04713
- **Key idea:** rich style captions with **59 tags**: 33 intrinsic (speaker-level, e.g. guttural, nasal, shrill) and 26 situational (utterance-level, e.g. whispered, pained).
- **Data/training recipe:**
  - PSC-Base: 282 h of human (MTurk) labels on Expresso, EARS and VoxCeleb.
  - PSC-Scaled, 2,427 h, built two ways:
    - intrinsic tags are **propagated through a perceptual speaker-similarity model** to similar Emilia speakers (×9);
    - situational tags come from **dominance-valence-arousal classifier → text-embedding match of transcript to tag → Gemini audio check** (×3, 215 h).
  - Parler-TTS is fine-tuned on it.
- **Key numbers:** +7.9% consistency MOS and +15.5% naturalness MOS over the best baseline that combines existing datasets. Human raters judged scaled labels on par with human labels.
- **Open weights + licence:** dataset, models and code released on GitHub [licence unverified].
- **Takeaway:**
  - Speaker-level traits can be labelled once per Vaani speaker (Vaani has speaker IDs) and propagated to all that speaker's clips.
  - A three-signal agreement filter (classifier + text + audio-LLM) gives precise situational labels. Precision is what our rubric rewards.
  - Replace Gemini with Qwen3-Omni for openness.

### VoiceSculptor (Hu et al., arXiv 2026) — arXiv:2601.10629
- **Key idea:**
  - **Design then clone:**
    - a voice-design model (Llasa-3B fine-tuned) creates a prompt waveform from a free-form description;
    - CosyVoice2 clones that voice for any text.
  - Chain-of-thought attribute tokens (pitch, rate, loudness, age, emotion…) are predicted before speech tokens, with joint text plus speech cross-entropy.
  - **Attribute-token dropout of 0.2**, so the model also follows raw text.
  - Retrieval-augmented generation retrieves similar instruction examples for out-of-domain descriptions.
- **Data/training recipe:**
  - ASR (Paraformer, Whisper, SenseVoice) plus forced alignment give **timestamps and pause durations**.
  - Gemini 2.5 Pro gives multi-dimensional annotations, rewritten into captions by DeepSeek.
  - Emotion from an ensemble: Emo2Vec, Qwen3-72B, SenseVoice, Qwen3-Omni.
  - Gender and age from VoxProfile.
  - Continuous prosody values are binned with human-calibrated boundaries.
- **Key numbers:** open-source SOTA on InstructTTSEval-Zh at the time; CoT and text-CE loss each give consistent ablation gains (numbers in paper tables).
- **Open weights + licence:** code and models released [licence unverified; Llasa base is CC-BY-NC].
- **Takeaway:**
  - The two-stage design → clone split is how to get **N different speakers for one description**: design N reference voices (different seeds, filtered by SV distance and relevance), then clone each for the Hindi/Tamil text.
  - Qwen3-TTS's own model card recommends the same workflow (VoiceDesign → `create_voice_clone_prompt` on Base → `generate_voice_clone`).
  - CoT attribute tokens with dropout are a cheap add-on to our SFT.

### InstructTTSEval (Huang et al., arXiv 2025) — arXiv:2506.16381
- **Key idea:**
  - Benchmark with three tasks: Acoustic-Parameter Specification (APS), Descriptive-Style Directive (DSD) and Role-Play (RP).
  - EN and ZH, 1k items each per task (6k total), paired with reference audio from film and TV.
  - Gemini is the automatic judge, validated against human agreement.
- **Data/training recipe:** n/a (evaluation).
- **Key numbers:** the scores quoted under Qwen3-TTS above. Open models (Parler, VoxInstruct, PromptTTS) score far below commercial ones on RP.
- **Open weights + licence:** code and data on GitHub.
- **Takeaway:**
  - Its LLM-as-judge protocol is a template for our "generation instruction relevance" proxy.
  - Swap Gemini for our own captioner plus Qwen3-8B as the judge.
  - Report human agreement on a subset to show rigour.

### NVSpeech (Liao et al., arXiv 2025) — arXiv:2508.04195
- **Key idea:**
  - Paralinguistic-aware ASR that emits inline tags ("…[Laughter]").
  - It auto-labels a large corpus, which is then used to fine-tune zero-shot TTS (CosyVoice-family) with **tags at arbitrary word positions**.
- **Data/training recipe:**
  - 48,430 human-annotated utterances with **18 word-level categories** ([Laughter], [Cough], [Breathing], [Sigh], fillers…).
  - Auto-labelled set: 174,179 utterances (573 h), Mandarin.
  - Audio-tagging baselines: PANNs, SenseVoice, Qwen-Audio.
- **Key numbers:** see paper. Not re-extracted beyond the dataset statistics.
- **Open weights + licence:** dataset and demos at nvspeech170k.github.io [licence unverified].
- **Takeaway:**
  - The recognise-then-synthesise loop for non-verbal sounds is exactly our captioner↔generator loop.
  - Mine Vaani's spontaneous speech for laughs, breaths and fillers with an audio tagger plus captioner timestamps, then train the generator with inline tags.
  - Fillers are lexical in Hindi/Tamil ("matlab", "haan", "athu"…) and can stay in the transcript.

### IndicVoices-R (Sankar et al., NeurIPS 2024 D&B) — arXiv:2409.05356
- **Key idea:** turn the IndicVoices ASR corpus into TTS-quality data by restoration.
- **Data/training recipe:**
  - Restoration chain: HTDemucs (demix) → VoiceFixer (dereverb) → DeepFilterNet3 (artefact cleanup).
  - Filters: C50 ≥ 30 dB, SNR ≥ 25 dB, 0.2–30 s, pitch mean ≤ 350 Hz, pitch std ≤ 150 Hz, rate ≤ 30 chars/s.
  - Fine-tuned VoiceCraft (English-pretrained) on it, improving zero-shot speaker generalisation over fine-tuning on IndicTTS.
- **Key numbers:**
  - **1,704 h, 10,496 speakers, 22 languages** (Hindi and Tamil included).
  - Per-language hours are in its Table 3 [not extracted cleanly].
  - Quality on par with LJSpeech, LibriTTS and IndicTTS by NORESQA, SNR and C50.
- **Open weights + licence:** **CC BY 4.0** (inherits IndicVoices). HF access is gated (contact sharing).
- **Takeaway:**
  - The main clean, many-speaker Hindi/Tamil pool for language adaptation and for fitting the speaker prior.
  - Vaani (16 kHz phone speech) needs bandwidth extension before it can serve as a ≥24 kHz target. Alternatively, keep Vaani as "phone channel" data only and render the channel by DSP.
  - Its restoration chain is reusable.

### Rasa (AI4Bharat / IIT Madras, Interspeech 2024) — arXiv:2407.14056 (search-level read; abstract and summary only)
- **Key idea:** expressive TTS dataset for Assamese, Bengali and **Tamil**: about 10 h neutral plus 1–3 h per Ekman emotion. Scripts were LLM-assisted and human-checked.
- **Key numbers:** about 1 h neutral plus 30 min per emotion gives "fair" MUSHRA; fear and surprise are hardest. Model is FastPitch + HiFiGAN.
- **Open weights + licence:** data on HF (gated) [licence unverified].
- **Takeaway:** the only open Tamil emotional TTS data we found; already inside Indic-Parler's training mix. Use it to teach Tamil emotion tags.

### Speaker Generation / TacoSpawn (Stanton et al., ICASSP 2022) — arXiv:2111.05095
- **Key idea:**
  - Learn a **mixture-of-Gaussians prior p(s | locale, gender)** over a multi-speaker TTS's learned speaker-embedding table, fitted after training.
  - Sample from it to make **new voices that are not any training speaker**.
  - Includes objective metrics (embedding-distance-based) that correlate with human judgements of speaker similarity.
- **Data/training recipe:** multi-speaker Tacotron trained with speaker metadata; the MoG prior is fitted with an MLP from metadata.
- **Key numbers:** see paper (speaker-distance metrics); not re-extracted.
- **Open weights + licence:** none (Google).
- **Takeaway:** the simplest workable speaker-diversity mechanism for us.
  - Embed all Vaani and IndicVoices-R speakers with the generator's speaker encoder.
  - Fit a conditional GMM or flow on (gender, age band, pitch band, language, region).
  - Draw 10 samples per description with **farthest-point / repulsive sampling**, checked against the SV threshold.
  - Clone each one.

---

## C. Cross-cutting answers to the focus questions

**Q1, backbone comparison (Hindi + Tamil, rich descriptions, 4× L4):**

| Model | Hi/Ta out of the box | Params | Token rate / SR | Description control | Licence | Fine-tune code |
|---|---|---|---|---|---|---|
| Qwen3-TTS-12Hz (Base / VD / CV) | No (10 langs) | 0.6B / 1.7B | 12.5 Hz × 16 cb / 24 kHz | Best open (InstructTTSEval EN DSD 82.4) | Apache-2.0 | Single-speaker SFT only; write instruct SFT |
| Indic-Parler-TTS | **Yes** (21 langs) | 0.9B | 86 Hz × 9 cb DAC / 44.1 kHz [unverified for Indic] | Coarse tags + emotions | Apache-2.0 | Full (parler-tts + dataspeech) |
| Fun-CosyVoice3-0.5B | No (9 langs) | 0.5B (+ flow + vocoder) | 25 Hz FSQ / 24 kHz [unverified] | NL instructions + `[laughter]`, `[breath]`, `<strong>` | Apache-2.0 | Full recipe + RL (GRPO / DiffRO) |
| IndicF5 | **Yes** (11 langs) | [unverified] | mel / 24 kHz | None (reference clone only) | MIT | F5 code (MIT) |
| Spark-TTS / Llasa / F5 / MaskGCT | No | 0.5B / 1–8B / ~0.3B / ~1B | 16 kHz (Spark, Llasa) | Attribute CoT (Spark) | **NC** | Yes |
| IndexTTS2 | No | [unverified] | — | Emotion soft instruct + duration | bilibili custom | partial |

**Q2, fine-grained temporal control:**
1. Inline tags in the transcript: CosyVoice 2/3 `[laughter]`, `[breath]`, `<strong>`; NVSpeech word-level tags; CapSpeech `<event>` with `<I>` / `<B>` spans.
2. Exact length or token count per segment: IndexTTS2; length set at inference in MaskGCT and F5.
3. Infilling or editing at a time span: VoiceCraft, F5, Audiobox, Step-Audio-EditX.
4. Pauses via punctuation and explicit silence (VoiceSculptor annotates pause durations from forced alignment).

For ±250 ms rubric precision, the most reliable option is **segment-wise rendering plus deterministic composition**. A planner LLM turns the description into a timeline: segments with style, pause durations in ms, and events with times. Each segment is generated with a length budget. Events and silences are spliced, then the recording chain is applied (RIR, noise at SNR, codec or band-limit).

**Q3, non-verbal vocalisations:**
- Three proven routes:
  - (a) learned inline tags (CosyVoice; NVSpeech, which bootstraps tags with a paralinguistic ASR);
  - (b) editing pairs, i.e. tag-removed TTS versus original (Step-Audio-EditX);
  - (c) splicing real event clips at aligned word gaps (CapSpeech, Audiobox).
- For Hindi/Tamil we have no tagged corpus, so start with (c) and mine Vaani for in-language laughs and breaths with an audio tagger. Then train (a) on the result.

**Q4, speaker diversity:** plain sampling of a description-conditioned model gives low variation (PromptTTS 2: pairwise similarity 0.77–0.91). Mechanisms that work:
- a sampleable latent or prior over timbre: PromptTTS 2 variation network (0.355), TacoSpawn GMM prior, MiniMax T2V 128-d timbre generator, Spark-TTS global tokens;
- design → clone (VoiceSculptor; Qwen3-TTS model card).

Add repulsive or farthest-point selection under the evaluation SV model, plus verifier filtering (Llasa-style best-of-N).

**Q5, data recipes:**
- binned DSP features → LLM rewrite (Parler, PromptTTS 2 placeholders, Audiobox style bank);
- augment-and-recaption (Audiobox RIR/noise; Fugatto Praat/Pedalboard);
- speaker-similarity propagation of intrinsic tags plus multi-signal agreement for situational tags (ParaSpeechCaps);
- alignment-based event insertion (CapSpeech);
- large-margin synthetic pairs (Step-Audio-EditX);
- self-distilled timbre pairs (Seed-TTS);
- synthetic-only training (EmoVoice);
- restoration of ASR corpora into TTS data (IndicVoices-R).

---

## Synthesis

**Top 8 actionable takeaways**
1. **Render the recording axis (channel, room, noise, Lombard-free mixing) by DSP after generation, not with the model.**
   - Parler could not control C50; Audiobox and Fugatto get exact labels from known transforms.
   - This gives near-perfect relevance on that axis, and the same transforms produce free labels for the captioner.
2. **Plan, render per segment, then compose for timed items.**
   - Qwen3-8B parses the description into a JSON timeline (segments, style, pause in ms, event times).
   - The generator renders each segment with a length budget (12.5 Hz = 80 ms/frame).
   - Events and silences are spliced at exact times, which meets ±250 ms by construction.
3. **Non-verbal sounds:**
   - Splice real in-language event clips at aligned word gaps first (CapSpeech: ≥0.3 s gap, MFA or CTC timestamps).
   - Then train inline tags (`[laughter]`, `[breath]`) on that data, as in CosyVoice and NVSpeech.
4. **Speaker diversity through an explicit timbre prior:**
   - Fit p(speaker embedding | gender, age band, pitch band, language) on Vaani + IndicVoices-R speakers (TacoSpawn / MiniMax-T2V style).
   - Sample 10 with farthest-point selection under the evaluation SV model.
   - Clone each with Qwen3-TTS Base (x-vector mode).
   - Expected effect: PromptTTS 2 dropped pairwise similarity from about 0.8 to 0.355.
5. **Captions:** binned DSP measures plus LLM rewrite with a persona style bank, with speaker-level tags propagated per Vaani speaker ID (ParaSpeechCaps). Write only what passes multi-signal agreement.
6. **Instruction SFT format:** ChatML with a speaker slot and a style slot that are randomly masked (CosyVoice 3), CoT attribute tokens with 0.2 dropout (VoiceSculptor/Spark), and description dropout for CFG (VoxInstruct).
7. **Round-1+ improvement without big training:**
   - Verifier best-of-N (Llasa), scoring with captioner relevance, IndicConformer CER and SV distance.
   - Then DPO on large-margin pairs (CosyVoice 2, Step-Audio-EditX), with the captioner as judge.
8. **Language adaptation data:** IndicVoices-R (CC-BY-4.0, 10.5k speakers) + Indic-Parler/Rasa sources + restored Vaani (HTDemucs → VoiceFixer → DeepFilterNet; Vaani's 16 kHz needs bandwidth extension). Record per-example source and labeller for the manifest.

**Recommended generator backbone:**
- **Qwen3-TTS-12Hz-1.7B (Base + VoiceDesign weights)**, continued-pretrained on Hindi/Tamil and instruction-SFT'd.
- Why:
  - Apache-2.0 and 24 kHz output.
  - Strongest open instruction following.
  - The 12.5 Hz tokenizer keeps 30 s clips at 375 frames.
  - A jointly trained speaker encoder supports the timbre-prior diversity plan.
  - The team already has the tokenizer.
- Fit on 4× L4 needs FSDP/ZeRO-3 (my own estimate: full AdamW fine-tuning at about 16 B/param ≈ 27 GB exceeds one L4), or LoRA, or the 0.6B model.
- **Indic-Parler-TTS is the round-0 baseline and the fallback**: it supports Hi/Ta today and has a full training stack.
- **IndicF5 (MIT) is a backup "clone renderer"** for design → clone.

**3 biggest risks**
1. **Qwen3-TTS has no Hindi/Tamil.** The 12Hz tokenizer may reconstruct Indic phonetics poorly, and Qwen BPE is token-inefficient for Tamil. Gate this in week 1 by measuring resynthesis CER.
2. **Training compute and code gaps.** Official fine-tuning is single-speaker only, and the 1.7B model is tight on L4s. Multi-speaker plus instruction SFT and continued pre-training must be written and validated by us.
3. **Diversity–relevance tension.** Samples spread for diversity may break described traits (pitch, age), and only passing samples count. The timbre prior must be conditioned, and the SV-threshold filter needs a relevance check.
