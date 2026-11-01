# Core full-text findings and architecture consequences

These notes distinguish author-reported evidence from our design judgments. None of the experiments was reproduced here. Page numbers refer to locally downloaded PDF snapshots; inspect `papers/*.source.json` for hashes. Most of the wider corpus receives a selective excerpt review, not cover-to-cover reading. The deeper checks below also have explicit section/page scope rather than an assertion that every appendix was read.

## 1. CycleSpeech — arXiv:2609.24771

Inspected: introduction and shared-profile method, Joint SFT and CycleGRPO (pp. 1–7), main results and ablations (pp. 8–10).

The model uses a frozen Step-Audio-2-mini backbone and two LoRA adapters for generation and understanding. A structured profile supplies fixed supervision targets; the public generation inputs remain instruction, transcript, and speaker reference. After a generation warm-up, the understanding adapter is exposed to generated audio. CycleGRPO alternates updates and uses profile matching plus content/quality guards.

The distinction between a full-system gain and the incremental reciprocal gain matters. English Instruction Match is 75.47 for the base, 81.97 after Joint SFT, and 85.53 after CycleGRPO (Table 3). English WER goes from 2.74 after Joint SFT to 3.08 after CycleGRPO. Understanding OS changes from 76.54 to 76.84 in English and 77.98 to 78.36 in Chinese. Table 8's no-cycle/frozen-feedback results are close on several understanding metrics; do not conclude every metric decisively benefits from reciprocal RL. Chinese Instruction Match is not best against every external system in Table 3. Subjective evaluation uses 50 samples/system and 100 ratings/system, which limits precision and generalization.

**Consequence:** reciprocal speech/profile learning is existing work. Use it as a required nearest comparator, not our novelty claim. The paper's Chinese/English data, speaker-reference interface, and profile-based task are different from Hindi/Tamil free descriptions spanning ecology and timed intent changes. Those differences motivate experiments; they do not prove our proposed contribution is new. Prefer the cheaper verified-data loop initially; test whether reciprocal optimization adds value beyond supervised adaptation.

Source: https://arxiv.org/abs/2609.24771

## 2. TAC — arXiv:2602.15766

Inspected: methodology pp. 3–5 and evaluation passage p. 7.

TAC mixes sources using constrained scene templates, labels realized activity using RMS-based maps, and varies style, resolution, activity threshold, and merge threshold. It reports about 150K mixtures / 1.2K hours. It fine-tunes a frozen Qwen2-Audio backbone using LoRA, represents timestamps with atomic special tokens, and upweights timestamp losses. Separate ASR supplies text for detected speech spans. The paper explicitly limits reliable per-speaker transcription under inseparable overlap. Evaluation includes TACOS and zero-shot AudioCaps/Clotho; the selected baseline formatting condition was chosen permissively on test data, while TAC's setting used development data.

**Consequence:** synthetic mixtures, timestamp tokens, and weighted temporal supervision are established precedents. Adopt realized activity labeling and interval supervision. Test acoustic masking after mixing: a scheduled source can be inaudible. Do not claim TAC's generic-event results establish Hindi/Tamil phonation, social intent, or ±250 ms success on the PS.

Source: https://arxiv.org/abs/2602.15766

## 3. UALM — arXiv:2510.12000

Inspected: architecture/training strategy and reasoning procedure pp. 2–7.

UALM uses a 25 Hz acoustic input encoder, MLP adapter, Qwen2.5-7B initialization, and a 50 Hz eight-codebook output representation. Its base waveform path is 16 kHz, with a separate enhancement VAE for 48 kHz stereo. The paper describes rich captions, generate–understand–critique–refine reasoning, task blending, alignment warm-up, and SFT/DPO stages. The authors report that their autoregressive generation needed substantially more data than their diffusion comparisons: 30M examples / about 80K audio hours. The described pretraining uses 128 A100-80GB GPUs and 660K steps.

**Consequence:** rich-caption planning and self-reflection are prior work. Reproducing unified-model pretraining is a poor use of 1,000 T4 GPU-hours. Transfer its training principles, not its compute recipe. A nominal high output sample rate through a separate restoration stage is not proof that every fine acoustic detail was preserved.

Source: https://arxiv.org/abs/2510.12000

## 4. Fugatto 1 — official project PDF

Inspected: abstract, instruction/data strategy, ComposableART formulation, and text-to-voice evaluation passages.

The official project hosts a 28-page PDF headed “Under review as a conference paper at ICLR 2025”; that snapshot's heading alone is not proof of final acceptance. Fugatto uses generated/augmented instructions, absolute and relative controls, captions from understanding models, dataset transmutation, and known audio transformations. ComposableART extends classifier-free guidance over multiple conditions, models, and mel-frame-dependent weights. This explicitly precedes proposed temporal compositional guidance.

**Consequence:** keep arbitrary-description residuals and time-varying controls in the generator interface. Frame-wise control composition is not automatically additive in perception: validate joint instructions and linguistic content. A paper and demo do not establish that eligible downloadable weights are available for our runtime.

Source: https://fugatto.github.io/FUGATTO_ICLR_2025.pdf

## 5. Natural-language TTS with synthetic annotations — arXiv:2402.01912

Inspected: metadata, model, and objective/subjective evaluations, pp. 2–4.

The work labels accent, pitch, speaking rate, estimated SNR and C50, then bins continuous measurements and rewrites them into descriptions. Its model prepends transcript tokens and cross-attends to a fixed T5 description encoder, predicting DAC codes. It needs no reference speech at inference. The reported data is primarily English audiobook speech. The authors report weaker accent control than gender control and poor C50 control; they also explain why generated speech can appear more relevant than the original recording when the original description has label noise. Their objective control evaluation reuses annotation models.

**Consequence:** description conditioning, measured metadata, and language-model rewrites are prior art. Track label uncertainty. Reusing a labeling model for evaluation can favor its own biases. Keep independent native listening. For room control, test explicit rendering against learned-only control instead of assuming the latter works. A Hindi/Tamil checkpoint is a separate verification requirement.

Source: https://arxiv.org/abs/2402.01912

## 6. F5-TTS — arXiv:2410.06885

Inspected: abstract, flow/CFG formulation, training/inference and architecture pp. 3–4, reported NFE results p. 6, limitations p. 9.

F5 trains text-guided mel infilling with conditional flow matching. It pads characters to audio-frame length and improves representations with ConvNeXt before DiT processing. Reference audio/transcript and generated text condition inference; the paper estimates total duration from character-length ratios rather than learning exact phone timing. Sway sampling trades NFE against quality. The reported RTF of 0.15 is an author result, not a T4 measurement. The limitations explicitly name mel-sequence cost and lack of fine-grained paralinguistic control.

**Consequence:** IndicF5 is a language-capable starting point, not a finished description-controlled generator. Add conditioning only after a native-language baseline; validate local timing rather than assuming text timestamps control a padded sequence. Inspect quality at 8/16/32 NFE locally; do not borrow throughput from the paper.

Source: https://arxiv.org/abs/2410.06885

## 7. Audio Flamingo 3 — arXiv:2507.08128

Inspected: architecture p. 3, data excerpts p. 5, staged training and experimental setup p. 7; official repository architecture/license documentation was also consulted.

AF3 adapts Whisper-large-v3 into AF-Whisper using caption supervision covering speech, sound and music. It couples this encoder through an adapter to a language model and trains in stages: adapter alignment, encoder tuning, broader tuning, and LoRA-based context/reasoning extension. The paper's training uses 128 A100-80GB GPUs. Metadata-driven synthetic captions and external teachers are part of its training recipe.

**Consequence:** a compact 7B frozen-backbone adapter experiment is sensible, but reproducing AF3 from scratch is not. Synthetic source labels need audits. Published broad benchmark results do not establish native Hindi/Tamil intent accuracy, quantized T4 memory fit, or timing calibration. Use a native-language ASR side channel as a tested hypothesis, not a claimed fix.

Source: https://arxiv.org/abs/2507.08128

## 8. Qwen3-Omni / Qwen3-TTS — arXiv:2509.17765 and 2601.15621

Inspected: full-text architecture/result excerpts and official model-family/language documentation.

Qwen3-Omni uses specialized reasoning/generation components and hierarchical codebook prediction; its 30B total parameters must not be confused with its active-parameter count. Qwen3-TTS documents a multilingual family, low-frame-rate representations, voice design, and instruction following. Its official ten-language list does not include Hindi or Tamil. Individual VoiceDesign, Base, and CustomVoice interfaces differ.

**Consequence:** optional teacher/baseline candidates, not mandatory final backbones. Confirm actual native pronunciation before spending adaptation compute. A public suggestion in the PS is not evidence of task-language support.

Sources: https://arxiv.org/abs/2509.17765 ; https://arxiv.org/abs/2601.15621

## 9. PromptTTS / PromptTTS++ — arXiv:2211.12171 and 2309.08140

Inspected: style/content architecture, identity conditioning, and evaluation excerpts.

PromptTTS separates style and content prompts and reports controlled style-factor accuracy. PromptTTS++ adds natural-language speaker prompts and a probabilistic mechanism for voice variation. Its evaluation discusses a tradeoff: averaged non-sampling voices can be preferred for naturalness, while sampling enables diverse identities.

**Consequence:** separate speaker identity from local delivery, and evaluate diversity among relevant samples rather than maximizing embedding dispersion. A model can have high average naturalness while failing the requested diversity objective.

Sources: https://arxiv.org/abs/2211.12171 ; https://arxiv.org/abs/2309.08140

## 10. VoiceLDM — arXiv:2309.13664

Inspected: dual conditions, latent diffusion, and evaluation protocol excerpts.

VoiceLDM conditions jointly on descriptive environmental text and linguistic content, with dual classifier-free guidance. Its reported evaluation uses an English-speech subset of AudioCaps with generated transcripts.

**Consequence:** joint speech/environment generation is prior work. It is a relevant architectural comparator, but English AudioCaps results do not establish Hindi/Tamil intelligibility or exact local control. Modular speech plus ecology is an engineering tradeoff, not an inherent research advance.

Source: https://arxiv.org/abs/2309.13664

## 11. SpeechCraft — arXiv:2408.13608

Inspected: tools/labeling p. 4, reported label checks p. 6, abstract.

SpeechCraft combines signal-processing measurements and learned classifiers to produce expressive-speech descriptions. The paper evaluates annotation components, including age/gender/emotion predictions, on specific corpora.

**Consequence:** automated fine-grained caption construction is prior art; classifier accuracy on one corpus is not a guarantee for spontaneous Hindi/Tamil. Do not treat inferred demographic labels or semantic narratives as verified acoustic facts.

Source: https://arxiv.org/abs/2408.13608

## 12. InstructTTSEval and the instruction–perception gap

Sources: https://arxiv.org/abs/2506.16381 ; https://arxiv.org/abs/2509.13989

Inspected: dataset/task construction, evaluator methodology, limitations and listener-quality-control excerpts.

InstructTTSEval distinguishes acoustic-parameter, descriptive-style, and role-play instructions; its English/Chinese setup uses model-assisted evaluation and acknowledges role-play subjectivity. The instruction–perception study separately probes degree modifiers, emotion intensity, perceived age and word emphasis using objective features and human listeners.

**Consequence:** require a local Hindi/Tamil instruction test grid. “Very,” “slightly,” and plausible role-play prose should not be credited without audible realization. Native listening is indispensable for intent and subtle expression; general objective similarity is insufficient.

## 13. IndicVoices and IndicVoices-R

Sources: https://arxiv.org/abs/2403.01926 ; https://arxiv.org/abs/2409.05356

Inspected: dataset scope, split/evaluation, restoration pipeline, and TTS result excerpts.

IndicVoices emphasizes spontaneous, extempore and conversational speech and geographically diverse speakers. IndicVoices-R restores ASR-oriented recordings for TTS, including denoising and enhancement from low-sampling-rate sources, and evaluates adapted synthesis.

**Consequence:** keep raw audio for ecology/phonation evidence and a separately restored view for clean-speech TTS when appropriate. Restoration can remove exactly the evidence Track 2 wants described. Do not present enhancement as measured recovery of the original missing bandwidth.

## 14. Calibration, imperfect synthesis, and recursive collapse

Sources: https://arxiv.org/abs/1706.04599 ; https://arxiv.org/abs/2110.11479 ; https://arxiv.org/abs/2305.17493 ; https://arxiv.org/abs/2011.13439

Inspected: calibration methods/results, synthetic-distribution correction, recursion setup, and uncertainty-driven filtering excerpts.

Calibration work establishes that raw model confidence can misrepresent correctness. Synt++ explicitly addresses synthetic/real distribution mismatch. The recursion paper studies distributional information loss under repeated model-generated replacement; it is not a theorem that all mixed synthetic-data use fails. DUST shows the value of uncertainty filtering in a particular ASR domain-adaptation setup; its thresholds cannot be copied directly to caption claims.

**Consequence:** retain real replay, calibrate per claim/type/language, mask unknown labels, and test uncertainty filtering against random selection at matched cost. A reciprocal loop needs an external real-data anchor, not just model agreement.

## 15. Efficient adaptation and verification

Sources: https://arxiv.org/abs/2106.09685 ; https://arxiv.org/abs/2305.14314 ; https://arxiv.org/abs/2008.02487 ; https://arxiv.org/abs/2304.03515

Inspected: adaptation/quantization and evaluation excerpts, plus QLoRA evaluation limitations.

LoRA/QLoRA support freezing most weights and adapting limited parameters; their text-model memory/quality results do not guarantee compatibility with any audio stack. Speaker-verification work documents sensitivity to vocal effort and overlapping speakers. QLoRA's own evaluation discussion notes judge/order biases.

**Consequence:** profile the exact T4 audio model, use independent blinded evaluators, and test diversity/identity under channel and delivery shifts. A speaker-embedding difference alone is not proof of a new speaker.

## 16. RASMALAI / IndicParlerTTS — arXiv:2505.18609

Inspected: data construction, model setup, main automatic/subjective results and conclusion (pp. 1–4); public checkpoint card/API metadata checked separately.

The paper constructs speech–transcript–description triples across Indian languages, using measured/available metadata and language-model-generated descriptive, concise, attribute-robust and native-language prompts. It adapts Parler-TTS Mini with an expanded transcript tokenizer, reporting 13K hours of multilingual pretraining and 32 H100 GPUs for 1.5 days. The paper's broad language coverage must be distinguished from the current release card's officially supported languages and tested emotion subset. Reported automatic attribute accuracies are high, including binned C50 control; these are not equivalent to continuous temporal control or full Track 2 evaluation. Perceptual emotion classification has substantial confusion for some classes, especially neutral. Its cross-lingual expressive evaluation also degrades from native to distal-language speakers.

**Consequence:** use the released description-native Hindi/Tamil model as the first G0 candidate. Compare pretrained vs studio-finetuned releases for the quality/diversity tradeoff. Keep IndicF5 with new adapters as an alternative rather than the assumed default. The native voice pool is small, especially Tamil; native pronunciation and diverse passing identities must be evaluated together. The public card can be read unauthenticated, but gated weights/config still require model access. Paper-reported training costs are not a fine-tuning budget estimate for T4s.

Sources: https://arxiv.org/abs/2505.18609 ; https://huggingface.co/ai4bharat/indic-parler-tts

## 17. TAC2 and frame-level grounding: particularly close recent work

Sources: https://arxiv.org/abs/2610.36568 ; https://arxiv.org/abs/2609.15215

TAC2 inspected scope: abstract and methodology pp. 1, 3–6, reasoning/generation validation passages pp. 7–8. Frame-level grounding inspected scope: architecture/method p. 2 and evaluation-oriented excerpt p. 3.

TAC2 fuses captioning, diarization and event-detection teachers using time-registered IoU matching, with attribute-specific authorities and temporal owners. An Instruction–Input–Output format allows autonomous or externally conditioned descriptions. TAC2-S adds speech specialists for stress, intonation, emotion, voice profile and acoustics, and distills their annotations into a unified student. The described teacher uses Qwen3Omni-Captioner, so parameter-efficient adaptation does not imply a small resident backbone. The paper also validates descriptions as supervision for temporally controllable audio generation. Public checkpoint availability and Hindi/Tamil performance were not established by reading the project page.

The separate frame-level-grounding paper combines contextual query representations with frozen frame-level acoustic features, upsampling and a fine-resolution CNN branch. It treats localization as an external temporal-evidence tool for a LALM. This directly precedes the proposed dedicated temporal evidence path.

**Consequence:** multi-teacher timed fusion, paralinguistic specialists, describe-then-reason, temporal tools and caption-to-generation supervision all have close prior art. A Hindi/Tamil implementation must cite these explicitly. The proposed study should isolate the value of calibrated, partially verified supervision and compute-aware weak-area selection rather than claim that its shared timeline or teacher fusion is new.
