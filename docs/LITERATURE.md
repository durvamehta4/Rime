# Literature map (248 entries)

Curated from six parallel reviews. Full per-paper notes (key idea, recipe, numbers, licence, takeaway) are in `research/notes_0*.md`, shipped alongside this package. Entries marked [unverified] in the notes were not confirmed against a primary source.


## Speech/audio captioners and audio-language models (47)

1. Qwen3-Omni Technical Report (arXiv 2025) — arXiv:2509.17765 (+ HF card Qwen/Qwen3-Omni-30B-A3B-Captioner)
2. Qwen-Audio (arXiv 2023) — arXiv:2311.07919
3. Qwen2-Audio Technical Report (arXiv 2024) — arXiv:2407.10759
4. Qwen2.5-Omni Technical Report (arXiv 2025) — arXiv:2503.20215
5. SALMONN (ICLR 2024) — arXiv:2310.13289
6. Listen, Think, and Understand — LTU (ICLR 2024 [venue unverified]) — arXiv:2305.10790
7. Joint Audio and Speech Understanding — LTU-AS (ASRU 2023 [venue unverified]) — arXiv:2309.14405
8. Audio Flamingo 2 (ICML 2025 [venue unverified]) — arXiv:2503.03983
9. Audio Flamingo 3 (NeurIPS 2025) — arXiv:2507.08128
10. Audio Flamingo Next (arXiv 2026) — arXiv:2604.10905 (+ HF nvidia/audio-flamingo-next-captioner-hf)
11. Kimi-Audio Technical Report (arXiv 2025) — arXiv:2504.18425
12. Step-Audio 2 Technical Report (arXiv 2025) — arXiv:2507.16632
13. GAMA (EMNLP 2024 [venue unverified]) — arXiv:2406.11768
14. UALM: Unified Audio Language Model (ICLR 2026 per brief) — arXiv:2510.12000
15. Omni-Captioner (arXiv 2025) — arXiv:2510.12720
16. MOSS-Audio Technical Report (arXiv 2026) — arXiv:2606.01802 (+ HF card)
17. TAC: Timestamped Audio Captioning (arXiv 2026) — arXiv:2602.15766
18. TAC2: Timestamped Audio Captioning as composable functions (arXiv 2026) — arXiv:2610.36568
19. Towards Fine-grained Temporal Perception: Post-Training LALMs with Audio-Side Time Prompt (arXiv 2026) — arXiv:2604.13715
20. SECap: Speech Emotion Captioning (AAAI 2024 [venue unverified]) — arXiv:2312.10381
21. ParaSpeechCaps (arXiv 2025 [venue unverified]) — arXiv:2503.04713
22. SpeechCraft (ACM MM 2024 [venue unverified]) — arXiv:2408.13608
23. CapSpeech (arXiv 2025 [venue unverified]) — arXiv:2506.02863
24. AudioSetCaps (arXiv 2024 [venue unverified]) — arXiv:2411.18953
25. Factor-Conditioned Speaking-Style Captioning (Interspeech 2024 [venue unverified]) — arXiv:2406.18910
26. TVPara (arXiv 2026) — arXiv:2610.19678
27. StyleInstructCaps — A Benchmark for Controllable Speaking-Style Captioning (AACL 2026) — arXiv:2610.33036
28. MMAU (ICLR 2025) — arXiv:2410.19168
29. MMAU-Pro (AAAI 2026) — arXiv:2508.13992
30. MMAR (arXiv 2025 [venue unverified]) — arXiv:2505.13032
31. AIR-Bench (ACL 2024 [venue unverified]) — arXiv:2402.07729
32. Do Audio LLMs Really LISTEN, or Just Transcribe? (arXiv 2025) — arXiv:2510.10444
33. Can Large Audio-Language Models Truly Hear? (MATCH) (arXiv 2024 [venue unverified]) — arXiv:2410.16130
34. Audio-Aware Decoding (AAD) (arXiv 2025) — arXiv:2506.07233
35. TAD: Token-Adaptive Contrastive Decoding (arXiv 2026) — arXiv:2609.07286
36. BRACE: Benchmark for Robust Audio Caption Quality Evaluation (arXiv 2025) — arXiv:2512.10403
37. FENSE / "Can Audio Captions Be Evaluated with Image Caption Metrics?" (ICASSP 2022 [venue unverified]) — arXiv:2110.04684
38. CLAIR-A (arXiv 2024 [venue unverified]) — arXiv:2409.12962
39. VAANI: Capturing the language landscape for an inclusive digital India (arXiv 2026) — arXiv:2603.28714
40. VAANI Noise Event Dataset (arXiv 2026) — arXiv:2609.02474
41. Vaani Benchmark V1.0 (Hindi) (arXiv 2026) — arXiv:2606.21408
42. Rasa: Expressive TTS for Indian languages (arXiv 2024 [venue unverified]) — arXiv:2407.14056
43. Indic Parler-TTS (HF model card, ai4bharat/indic-parler-tts) — no arXiv paper
44. IndicContextEval (arXiv 2026) — arXiv:2606.19157
45. ms-swift Qwen3-Omni example scripts (modelscope/ms-swift, `examples/models/qwen3_omni/*.sh`, `examples/megatron/multimodal/omni/moe.sh`)
46. Top 8 actionable design takeaways
47. 3 biggest risks

<details><summary>Synthesis</summary>

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

</details>


## Instruction/description-conditioned TTS (32)

1. Qwen3-TTS Technical Report (Qwen Team, tech report 2026) — arXiv:2601.15621
2. Indic Parler-TTS (AI4Bharat + HF, model card 2024) — no arXiv; huggingface.co/ai4bharat/indic-parler-tts
3. Natural language guidance of high-fidelity TTS with synthetic annotations (Lyth & King, arXiv 2024) — arXiv:2402.01912
4. CosyVoice 2 (Du et al., tech report 2024) — arXiv:2412.10117
5. CosyVoice 3 (Du et al., tech report 2025) — arXiv:2505.17589
6. Spark-TTS (Wang et al., arXiv 2025) — arXiv:2503.01710
7. Llasa (Ye et al., arXiv 2025) — arXiv:2502.04128
8. MiniMax-Speech (MiniMax, tech report 2025) — arXiv:2505.07916
9. IndexTTS2 (Zhou et al., arXiv 2025) — arXiv:2506.21619
10. Step-Audio-EditX (StepFun, tech report 2025) — arXiv:2511.03601
11. F5-TTS (Chen et al., arXiv 2024; venue [unverified]) — arXiv:2410.06885
12. IndicF5 (AI4Bharat, model card 2025) — no arXiv; huggingface.co/ai4bharat/IndicF5
13. MaskGCT (Wang et al., ICLR 2025) — arXiv:2409.00750
14. Seed-TTS (ByteDance, tech report 2024) — arXiv:2406.02430
15. VoiceCraft (Peng et al., ACL 2024) — arXiv:2403.16973
16. UniAudio (Yang et al., ICML 2024) — arXiv:2310.00704
17. Audiobox (Vyas et al., Meta, arXiv 2023) — arXiv:2312.15821
18. Fugatto 1 (Valle et al., NVIDIA, ICLR 2025) — OpenReview B2Fqu7Y2cd (no arXiv found)
19. PromptTTS (Guo et al., ICASSP 2023) — arXiv:2211.12171
20. PromptTTS 2 (Leng et al., ICLR 2024) — arXiv:2309.02285
21. InstructTTS (Yang et al., submitted to TASLP 2023; final venue [unverified]) — arXiv:2301.13662
22. TextrolSpeech / Salle (Ji et al., ICASSP 2024) — arXiv:2308.14430
23. VoxInstruct (Zhou et al., ACM MM 2024) — arXiv:2408.15676
24. EmoVoice (Yang et al., ACM MM 2025) — arXiv:2504.12867
25. CapSpeech (Wang et al., arXiv 2025) — arXiv:2506.02863
26. ParaSpeechCaps (Diwan et al., arXiv 2025) — arXiv:2503.04713
27. VoiceSculptor (Hu et al., arXiv 2026) — arXiv:2601.10629
28. InstructTTSEval (Huang et al., arXiv 2025) — arXiv:2506.16381
29. NVSpeech (Liao et al., arXiv 2025) — arXiv:2508.04195
30. IndicVoices-R (Sankar et al., NeurIPS 2024 D&B) — arXiv:2409.05356
31. Rasa (AI4Bharat / IIT Madras, Interspeech 2024) — arXiv:2407.14056 (search-level read; abstract and summary only)
32. Speaker Generation / TacoSpawn (Stanton et al., ICASSP 2022) — arXiv:2111.05095

<details><summary>Synthesis</summary>

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

</details>


## Self-improving loops, synthetic data, preference/RL alignment (46)

1. Listening while Speaking: Speech Chain by Deep Learning (ASRU 2017 [venue unverified, arXiv lists none]) — arXiv:1707.04879
2. Improving Neural Machine Translation Models with Monolingual Data (ACL 2016) — arXiv:1511.06709
3. Dual Learning for Machine Translation (NIPS 2016) — arXiv:1611.00179
4. Self-training with Noisy Student improves ImageNet classification (CVPR 2020) — arXiv:1911.04252
5. Improved Noisy Student Training for Automatic Speech Recognition (Interspeech 2020) — arXiv:2005.09629
6. STaR: Bootstrapping Reasoning With Reasoning (NeurIPS 2022 [venue unverified on abs page]) — arXiv:2203.14465
7. Reinforced Self-Training (ReST) for Language Modeling (arXiv 2023) — arXiv:2308.08998
8. Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models (ReST^EM) (TMLR 2024) — arXiv:2312.06585
9. Self-Rewarding Language Models (ICML 2024) — arXiv:2401.10020
10. AI models collapse when trained on recursively generated data (Nature 631:755–759, 2024; arXiv preprint "The Curse of Recursion") — arXiv:2305.17493, DOI 10.1038/s41586-024-07566-y
11. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv 2024; later COLM 2024 [unverified]) — arXiv:2404.01413
12. Self-Consuming Generative Models Go MAD (ICLR 2024 [venue unverified on abs page]) — arXiv:2307.01850
13. SpeechAlign: Aligning Speech Generation to Human Preferences (NeurIPS 2024 [unverified]) — arXiv:2404.05600
14. Preference Alignment Improves Language Model-Based TTS (Tian et al., ICASSP 2025 [venue unverified]) — arXiv:2409.12403
15. Enhancing Zero-shot Text-to-Speech Synthesis with Human Feedback (UNO) (arXiv 2024) — arXiv:2406.00654
16. Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance (EMNLP 2025 [unverified]) — arXiv:2502.05236
17. Seed-TTS (ByteDance tech report 2024), Section 4.2 RL — arXiv:2406.02430
18. CosyVoice 3: Towards In-the-wild Speech Generation via Scaling-up and Post-training (2025) — arXiv:2505.17589
19. F5R-TTS: Improving Flow-Matching based Text-to-Speech with Group Relative Policy Optimization (2025) — arXiv:2504.02407
20. Emo-DPO: Controllable Emotional Speech Synthesis through Direct Preference Optimization (ICASSP 2025 [unverified]) — arXiv:2409.10157
21. Advancing Zero-shot TTS Intelligibility across Diverse Domains via Preference Alignment (INTP) (ACL 2025) — arXiv:2505.04113
22. FlexiVoice: Enabling Flexible Style Control in Zero-Shot TTS with Natural Language Instructions (arXiv 2026) — arXiv:2601.04656
23. Diagnose, Then Refine: A Closed-Loop TTS System with AudioLLM-Guided Correction (LoopTTS) (EMNLP 2026) — arXiv:2608.28970 [abstract only]
24. BATON: Aligning Text-to-Audio Model with Human Preference Feedback (arXiv 2024) — arXiv:2402.00744
25. Tango 2: Aligning Diffusion-based Text-to-Audio Generations through Direct Preference Optimization (ACM MM 2024 [unverified]) — arXiv:2404.09956
26. TangoFlux: Super Fast and Faithful Text to Audio Generation with Flow Matching and Clap-Ranked Preference Optimization (arXiv 2024) — arXiv:2412.21037
27. Reinforcement Learning Outperforms Supervised Fine-Tuning: A Case Study on Audio Question Answering (R1-AQA) (arXiv 2025) — arXiv:2503.11197
28. Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models (arXiv 2025) — arXiv:2503.02318
29. SARI: Structured Audio Reasoning via Curriculum-Guided Reinforcement Learning (arXiv 2025) — arXiv:2504.15900
30. Omni-R1: Do You Really Need Audio to Fine-Tune Your Audio LLM? (arXiv 2025) — arXiv:2505.09439
31. AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives (arXiv 2025) — arXiv:2512.24052
32. REVE: Efficient Hallucination Correction for Large Audio-Language Models via Reused Encoder States (arXiv 2026) — arXiv:2609.26028 [abstract only]
33. AVCap: Reinforcing Audio-Video Joint Caption with Detail-Aware Reward (arXiv 2026) — arXiv:2608.06930
34. AudioMap: Cloze-and-Choice Reinforcement Learning for Time-Aware Dense Audio Captioning (arXiv 2026) — arXiv:2608.09559
35. Hard-Synth: Synthesizing Diverse Hard Samples for ASR using Zero-Shot TTS and LLM (arXiv 2024) — arXiv:2411.13159
36. On the Effect of Purely Synthetic Training Data for Different ASR Architectures (SynData4GenAI 2024 [venue unverified]) — arXiv:2407.17997
37. Scaling Rich Style-Prompted Text-to-Speech Datasets (ParaSpeechCaps) (EMNLP 2025) — arXiv:2503.04713
38. Empowering Low-Resource Language ASR via Large-Scale Pseudo Labeling (Pratinidhi) (arXiv 2024) — arXiv:2408.14026
39. A Novel Self-training Approach for Low-resource Speech Recognition (Interspeech 2023) — arXiv:2308.05269 [abstract only]
40. FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023) — arXiv:2305.14251
41. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative LLMs (EMNLP 2023) — arXiv:2303.08896
42. Language Models with Conformal Factuality Guarantees (ICML 2024 [venue unverified]) — arXiv:2402.10978
43. Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations (arXiv 2024) — arXiv:2411.00640
44. Top 8 actionable takeaways
45. Recommended loop (pseudo-code)
46. 3 biggest risks

<details><summary>Synthesis</summary>

## Synthesis

### Top 8 actionable takeaways
1. **Accumulate and anchor, never replace.** Each round trains from the *base* checkpoint on real Vaani (with fresh clips added each round) + transform-labelled real speech + all verified synthetic data so far (Gerstgrasser 2404.01413; ReST^EM; MAD 2307.01850; Nature 2024: 10% real retention largely prevents degradation). Keep synthetic data at about 10–30% of the mix (Hard-Synth found more synthetic data hurt).
2. **Train only on verified *claims*, not whole captions.** Decompose pseudo-captions into atomic claims (FActScore). Keep a claim only if it is confirmed by a known transform, a DSP measurement, metadata, or by ≥m/K self-consistent samples plus a second model's agreement (SelfCheckGPT, Pratinidhi consensus). Set the threshold with conformal-style calibration. Start strict and relax over rounds (NST gradational filtering).
3. **Captioner reward = AudioMap/AVCap-style asymmetric claim reward:** +1 correct, about −0.5 omitted, −1 wrong, plus IoU for timed events and a 300-word cap. Holistic judge scores *increase* hallucination (AVCap). GRPO with verifiable rewards on about 10–40k items for about 500 steps beats SFT (R1-AQA, SARI).
4. **Captioner anti-hallucination DPO:** rejected caption = chosen caption + one injected false or contradicted claim (AHA counterfactual negatives). This targets the rubric's FALSE items directly.
5. **Generator: one round of DPO on self-sampled pairs (codec-LM)** following Tian 2409.12403 / Koel-TTS. 6–10 samples per (text, description). Combined/Pareto rank over CER (a *different* ASR than IndicConformer), speaker sim, per-statement adherence from the captioner-judge, and UTMOS-like naturalness. β≈0.01. Pairs must dominate on all metrics. A few hundred to a few thousand pairs suffices, so this is feasible on 4xL4 with LoRA. A second round only on hard prompts (INTP), and only if held-out results improve.
6. **Attribute-contrast negatives for instruction relevance:** same text, description perturbed in one attribute (Tango 2, Emo-DPO). Optionally a binary audio-LLM judge GRPO stage per statement (FlexiVoice), run *after* DPO and not jointly.
7. **Target weak areas by measured error:** per-axis rubric error of the current captioner on a dev set. Pick its worst clips as voice and channel prompts for the generator (Hard-Synth). Order RL data easy to hard by pass rate and drop items that are never solved (SARI). Cap samples per prompt (ReST^EM).
8. **Guard diversity and naturalness:** quality selection is sampling bias that kills recall (MAD). Select the 10 eval samples by best-of-N *subject to distinct speaker embeddings*. Watch for over-articulation (Seed-TTS) and length growth (Self-Rewarding, Tian). Always evaluate with metric models not used as rewards.

### Recommended loop (pseudo-code)
```
R0: C0 = Qwen3-Omni-Captioner (+LoRA SFT on transform-labelled Vaani clips, verified claims only)
    G0 = Qwen3-TTS-1.7B (+SFT on Vaani with C0 descriptions, verified claims only)
DEV = per-language held-out real clips (>=200, speaker-disjoint); TEST = 30+30 frozen
for r in 1..2:                                   # stop early if no paired-bootstrap gain
  # (1) caption the pool -> verified data
  for clip in fresh_vaani_slice(r) ∪ transform_clips:
      caps = C_{r-1}.sample(clip, K=5)
      claims = decompose(caps)                    # Qwen3-8B
      keep = {c: freq(c)>=tau_r and verifier(c, dsp, metadata, transforms)!=FALSE}
      D_cap += rewrite(keep) with provenance(source, labeler=C_{r-1}, round=r)
  # (2) generator
  G_r = SFT(G_base, real ∪ D_cap)                 # from base, accumulate
  pairs = []
  for (text, desc) in hard_and_weak_prompts(r):
      ys = G_r.sample(text, desc, N=8)
      score each y: CER(alt-ASR), adherence = per-statement verified by C_{r-1}+DSP, SIM, MOSproxy
      pairs += pareto_dominant(best, worst) + perturbed_desc_negatives(desc)
  G_r = DPO(G_r, pairs, beta=0.01) + SFT_on_winners
  # (3) targeted synthetic -> captioner
  weak_axes = per_axis_error(C_{r-1}, DEV)
  synth = [G_r(text, desc_known) for desc_known in templates(weak_axes)] + known_transforms
  synth = filter(synth, C-judge agrees on known desc, CER<thr)          # cap per prompt
  C_r = SFT(C_base, real_verified ∪ ⋃_{k<=r} synth_k  [synth<=25%])
  C_r = GRPO(C_r, reward = asym_claim_score + IoU_time - len_penalty)   # verifiable items, curriculum
  C_r = DPO(C_r, chosen=verified caption, rejected=+1 injected false claim)
  report paired bootstrap (clip/speaker-clustered) of rubric-proxy, CER, SIM-diversity on DEV/TEST; compute GPU-h
  if no significant gain: stop
inference: captioner = K samples -> keep claims with freq>=tau* (calibrated) -> REVE/detector check
           generator = N>10 samples -> best by adherence s.t. distinct speakers -> top 10
```

### 3 biggest risks
1. **Shared blind spots / reward hacking.** The captioner judges the generator, and the generator's audio then trains the captioner, so errors can be *mutually confirmed* (a private code, as in dual learning; reward rises while humans disagree, as in ReST). Mitigation: independent verifiers (DSP, transforms, a second model), held-out metric models, and human spot-checks per round.
2. **Collapse of tails and diversity.** Rare voices, Tamil, creaky/falsetto voice and events vanish under quality filtering (Nature 2024, MAD). This directly costs speaker-diversity and rubric recall. Mitigation: accumulate real data, add fresh real data each round, use diversity-aware selection, and cap per-prompt samples.
3. **Synthetic-to-real gap plus underpowered evaluation.** Captioner gains on TTS audio may not transfer to 16 kHz Vaani phone speech (2407.17997, Hard-Synth). With 30 test clips, round-over-round gains may be within noise, and gains may come from language priors (Omni-R1). Mitigation: cap the synthetic share, run no-audio ablations, use a larger speaker-disjoint dev set, and report paired, clustered bootstrap CIs with a minimum detectable effect.

</details>


## Measurement tools and quality metrics (42)

1. CREPE (ICASSP 2018), arXiv:1802.06182 / github.com/marl/crepe
2. torchcrepe — github.com/maxrmorrison/torchcrepe
3. PENN / FCNF0++ — "Cross-domain Neural Pitch and Periodicity Estimation" (arXiv 2023, v3 2024), arXiv:2301.12258 / github.com/interactiveaudiolab/penn
4. PESTO (ISMIR 2023, Best Paper; TISMIR 2025), arXiv:2309.02265 and arXiv:2508.01488 / github.com/SonyCSLParis/pesto
5. RMVPE (Interspeech 2023), arXiv:2306.15412 / github.com/Dream-High/RMVPE
6. Parselmouth / Praat (Journal of Phonetics 2018) — github.com/YannickJadoul/Parselmouth
7. Comparative Evaluation of Acoustic Feature Extraction Tools for Clinical Speech (arXiv 2025), arXiv:2506.01129
8. Silero VAD — github.com/snakers4/silero-vad (no paper)
9. pyannote speaker-diarization-3.1 + powerset segmentation (Interspeech 2023), arXiv:2310.13025 / HF pyannote/speaker-diarization-3.1
10. Brouhaha (ASRU 2023 [venue unverified]; arXiv 2022), arXiv:2210.13248 / github.com/marianne-m/brouhaha-vad, HF pyannote/brouhaha
11. Impulse Response Data Augmentation and DNNs for Blind Room Acoustic Parameter Estimation (Bryan, ICASSP 2020 [venue unverified]), arXiv:1909.03642
12. A Universal Deep Room Acoustics Estimator (WASPAA 2021), arXiv:2109.14436
13. blind_rt60 (PyPI `blind-rt60`), github.com/nuniz/blind_rt60
14. Data-driven detection and analysis of the patterns of creaky voice (Drugman, Kane, Gobl; Computer Speech & Language 2014), arXiv:2006.00518 / COVAREP
15. DeepFry: Identifying Vocal Fry Using DNNs (Interspeech 2022), arXiv:2203.17019 / github.com/bronichern/DeepFry
16. CPP / H1–H2 / HNR for breathiness (clinical literature; via Parselmouth or VoiceSauce)
17. Falsetto / register detection (search-level only)
18. Vox-Profile (TMLR 2026 [venue inferred from the OpenReview/JMLR-style header, unverified]), arXiv:2505.14648 / github.com/tiantiaf0627/vox-profile-release
19. Speech-based Age and Gender Prediction with Transformers (audEERING, ITG 2023 [venue unverified]), arXiv:2306.16962 / HF audeering/wav2vec2-large-robust-24-ft-age-gender
20. emotion2vec (ACL Findings 2024 [venue unverified]) and emotion2vec+, arXiv:2312.15185 / github.com/ddlBoJack/emotion2vec
21. ECAPA-TDNN (Interspeech 2020), arXiv:2005.07143 / HF speechbrain/spkrec-ecapa-voxceleb
22. WavLM (IEEE JSTSP 2022), arXiv:2110.13900 / HF microsoft/wavlm-base-plus-sv
23. PANNs (IEEE/ACM TASLP 2020), arXiv:1912.10211 / github.com/qiuqiangkong/panns_inference
24. AST: Audio Spectrogram Transformer (Interspeech 2021), arXiv:2104.01778 / github.com/YuanGongND/ast
25. BEATs (ICML 2023 [venue unverified]), arXiv:2212.09058 / microsoft/unilm
26. EAT: Efficient Audio Transformer (IJCAI 2024), arXiv:2401.03497 / github.com/cwx-worst-one/EAT
27. LAION-CLAP (ICASSP 2023), arXiv:2211.06687 / github.com/LAION-AI/CLAP
28. Robust Laughter Detection in Noisy Environments (Interspeech 2021) — github.com/jrgillick/laughter-detection
29. MMS: Scaling Speech Technology to 1,000+ Languages (JMLR 2024 [venue unverified]), arXiv:2305.13516 / torchaudio `MMS_FA`
30. IndicConformer 600M multilingual (AI4Bharat) — HF ai4bharat/indic-conformer-600m-multilingual
31. Praat syllable-nuclei speaking rate (de Jong & Wempe, Behavior Research Methods 2009), doi:10.3758/BRM.41.2.385
32. UTMOS (Interspeech 2022), arXiv:2204.02152
33. UTMOSv2: T05 system for VoiceMOS 2024 (SLT 2024), arXiv:2409.09305 / github.com/sarulab-speech/UTMOSv2
34. The VoiceMOS Challenge 2024 (SLT 2024), arXiv:2409.07001
35. DNSMOS and DNSMOS P.835 (ICASSP 2021 / ICASSP 2022), arXiv:2010.15258 and arXiv:2110.01763 / github.com/microsoft/DNS-Challenge (DNSMOS/)
36. NISQA (Interspeech 2021), arXiv:2104.09494 / github.com/gabrielmittag/NISQA
37. Meta Audiobox Aesthetics (arXiv 2025), arXiv:2502.05139 / github.com/facebookresearch/audiobox-aesthetics
38. Natural language guidance of high-fidelity TTS with synthetic annotations (Lyth & King, arXiv 2024; Parler-TTS), arXiv:2402.01912
39. DataSpeech (Hugging Face), github.com/huggingface/dataspeech
40. ParaSpeechCaps: Scaling Rich Style-Prompted TTS Datasets (Diwan et al., 2025; EMNLP 2025 [venue unverified]), arXiv:2503.04713
41. Bandwidth and codec detection (search-level)
42. Lombard effect acoustics (Korn 1954 via PMC; Ngo et al. J. Signal Processing 2017; Bauer et al. Speech Prosody 2026)

<details><summary>Synthesis</summary>

## Synthesis

**Items read: 42** (36 with a primary source read: paper full text, README or model card; 6 at search or abstract level: blind_rt60, Universal Room Estimator, CPP/H1-H2 validity, falsetto, bandwidth/codec, Lombard).

| Rubric item | Recommended tool(s) | Output (time-localised?) | Confidence |
|---|---|---|---|
| Speaker | Vaani metadata; audEERING age-gender; Vox-Profile sex/age; pyannote 3.1 (speaker count) | sex prob, age band, n speakers + segments | Sex high (~97–98% acc); age low (MAE 7–11 y); accent/dialect: none for Indic, use metadata |
| Source (phonation) | DeepFry / Kane-Drugman creak (20 ms); Parselmouth CPP, H1–H2, HNR within-speaker; Vox-Profile voice quality | creak spans; relative breathiness | Creak medium (F1 ~0.6–0.7; Kane high-P/low-R); breathy/strained/falsetto low |
| Morphology | Silero VAD + MMS-FA boundaries; PENN slope over last 300 ms; creak at phrase end | phrase onset/offset times, final rise/fall in st | Medium |
| Pitch | **PENN** (10 ms, periodicity) + RMVPE in noise; PESTO fallback | median/p10–p90 F0 in Hz and semitones, contour events | High (RPA ~0.95–0.98 on speech) |
| Timing | MMS-FA (uroman) / IndicConformer; de Jong-Wempe nuclei; Silero pauses | syll/s, pause ms, word spans | Medium-high |
| Event | Gillick laughter + PANNs framewise; CLAP/AST windowed check | event label + start–end s | Medium (laughter F1 ~0.6–0.75 [secondary]) |
| Channel | NISQA dims; DNSMOS SIG; DSP bandwidth/clipping; synthetic-trained codec classifier | NB/WB cutoff Hz, distortion type | Bandwidth high; codec low-medium |
| Space | Brouhaha C50 (real MAE 1.1 dB); own T60 regressor (Bryan-style, synthetic RIRs) | C50 dB, T60 s | Medium |
| Other sounds | PANNs framewise; Brouhaha frame SNR; DNSMOS BAK; CLAP open-vocabulary | class + spans; SNR dB | Medium (SNR MAE 2.3 dB synthetic) |
| Coupling (Lombard) | Derived: windowed SNR against intensity, F0 and spectral tilt correlation | "louder/higher when noise rises at t" | Low |
| Addressee | No acoustic tool; ASR transcript + LLM; Vaani prompt context | text inference | Low, so abstain or state generically |
| Subtext | emotion2vec+, Vox-Profile arousal/valence (CCC ~0.6) + acoustic corroboration | windowed class probs | Low (SER macro-F1 ~0.4) |
| Change | Change-points on windowed F0, energy, rate, SNR, emotion probabilities | "from X to Y at t s" | Medium for acoustic change, low for intent |

**Three biggest risks**
1. **Domain shift.** Almost every tool was trained on English, clean or Western audio: PENN on PTDB, Brouhaha on LibriSpeech, creak models on American English, Vox-Profile on English accents. Vaani is spontaneous 16 kHz phone speech in Hindi and Tamil. DataSpeech's SNR bins (17–75 dB) already sit outside Brouhaha's 0–30 dB training range. We must recalibrate with controlled transforms (known SNR, RIR, pitch shift, splices) on Vaani before turning numbers into words.
2. **Low-accuracy perceptual labels meet a penalty for false claims.** Voice-quality F1 is about 0.70, SER about 0.4, age about 65%, and even humans agree on only about 50% of ParaSpeechCaps intrinsic tags. The captioner needs per-claim confidence gating that favours abstaining over guessing. Hedging between alternatives earns no credit.
3. **Licences and gating limit what we can redistribute.** CC-BY-NC-SA applies to audEERING and the NISQA weights, RAIL non-commercial to Vox-Profile, GPL to Parselmouth, LGPL to PESTO, and CC-BY-NC to MMS [unverified]. pyannote and Brouhaha need gated HF tokens. Torchaudio removes the forced-alignment APIs in 2.9. Pin versions and record the labeler of every example in the manifest.

</details>


## Indic speech resources and neural codecs (37)

1. VAANI: Capturing the language landscape for an inclusive digital India (arXiv 2026), arXiv:2603.28714 / HF `ARTPARK-IISc/Vaani`
2. Vaani Benchmark V1.0 (arXiv 2026), arXiv:2606.21408
3. IndicVoices (ACL Findings 2024 [unverified venue]), arXiv:2403.01926 / HF `ai4bharat/IndicVoices`
4. IndicVoices-R (NeurIPS 2024 D&B), arXiv:2409.05356 / HF `ai4bharat/indicvoices_r`
5. Rasa (INTERSPEECH 2024), arXiv:2407.14056 / HF `ai4bharat/Rasa`
6. IndicTTS database (IIT Madras) + "Towards Building TTS Systems for the Next Billion Users" (ICASSP 2023), arXiv:2211.09536
7. LIMMITS'23/'24 / SYSPIN (IISc; ICASSP 2023 SPGC; IEEE OJSP 2024)
8. Kathbath / IndicSUPERB (AAAI 2023 [unverified venue]), arXiv:2208.11761 / HF `ai4bharat/Kathbath`
9. Shrutilipi (AI4Bharat; IndicWav2Vec paper arXiv:2111.03945 and "Effectiveness of mining audio-text pairs") / HF `ai4bharat/Shrutilipi`
10. LAHAJA (INTERSPEECH 2024 [unverified venue]), arXiv:2408.11440 / HF `ai4bharat/Lahaja`
11. Svarah (INTERSPEECH 2023 [unverified venue]), arXiv:2305.15760 / HF `ai4bharat/Svarah`
12. RESPIN-S1.0 (NeurIPS 2025 D&B)
13. Tamil dialect ID work: DravidianLangTech-2026 shared task (ACL Anthology 2026.dravidianlangtech-*) + Bharathi et al. 2025 multi-dialect corpus + Nanmalar et al. arXiv:2408.13739 / 2408.14887
14. Hindi dialect/text resources (HinDialect 1.1; VarDial 2018 ILI shared task)
15. IndicConformer-600M multilingual — HF `ai4bharat/indic-conformer-600m-multilingual` (the official Track-2 intelligibility judge)
16. Vistaar / IndicWhisper (INTERSPEECH 2023), arXiv:2305.15386 / GitHub AI4Bharat/vistaar
17. "What is lost in Normalization?" (arXiv 2024), arXiv:2409.02449
18. IndicLID (ACL 2023), arXiv:2305.15814 / GitHub AI4Bharat/IndicLID
19. IndicXlit / Aksharantar (EMNLP Findings 2023), arXiv:2205.03018
20. Indic NLP Library — GitHub anoopkunchukuttan/indic_nlp_library
21. Indic-Parler-TTS — HF `ai4bharat/indic-parler-tts` (team has locally)
22. Parler-TTS / "Natural language guidance of high-fidelity TTS with synthetic annotations" (arXiv 2024), arXiv:2402.01912
23. IndicF5 — HF `ai4bharat/IndicF5`
24. Qwen3-TTS Technical Report (arXiv 2026), arXiv:2601.15621 / HF `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`
25. Qwen3-TTS-Tokenizer-12Hz — HF `Qwen/Qwen3-TTS-Tokenizer-12Hz`
26. SoundStream (IEEE/ACM TASLP 2022 [venue unverified]), arXiv:2107.03312
27. EnCodec (TMLR 2023 [unverified venue]), arXiv:2210.13438
28. DAC — Improved RVQGAN (NeurIPS 2023 spotlight), arXiv:2306.06546 / GitHub descriptinc/descript-audio-codec
29. Mimi (in Moshi; arXiv 2024), arXiv:2410.00037 / HF `kyutai/mimi`
30. X-Codec 2.0 (Llasa paper; arXiv 2025), arXiv:2502.04128 / HF `HKUSTAudio/xcodec2`
31. WavTokenizer (ICLR 2025), arXiv:2408.16532
32. BigCodec (arXiv 2024), arXiv:2409.05377
33. Do Neural Codecs Generalize? (arXiv 2026), arXiv:2601.12205
34. Indian-language codec evaluation (blog, Aman Agrawal, r4plh.github.io 2025/26; not peer reviewed)
35. Indic-CodecFake meets SATYAM (ACL Findings 2026), arXiv:2604.19949; SEA-CF (arXiv 2606.15968)
36. Recommended data mix
37. Three biggest risks

<details><summary>Synthesis</summary>

## Synthesis

### Recommended data mix

| Dataset | Lang | Hours (verified) | Licence | Use |
|---|---|---|---|---|
| IndicVoices-R | hi / ta | 74.6 h, 399 spk / 99.5 h, 1,084 spk | CC-BY-4.0 | **Generator core** (48 kHz, many speakers); captioner (pitch/SNR/C50/rate columns -> numeric descriptions); accent probe (district/state) |
| Rasa | hi / ta | 50.8 h / 56.1 h (2 spk each) | CC-BY-4.0 | Generator style/emotion control; captioner affect (balanced with IV-R) |
| LIMMITS / SYSPIN | hi | about 40 h × 2 spk | CC-BY-4.0 (SYSPIN) [LIMMITS terms unverified] | Generator naturalness (Hindi only) |
| IndicTTS (IITM) | hi / ta | ≥8 h/spk, 2 spk each | [unverified — check] | Generator, only if the licence permits |
| Vaani (transcribed part) | hi / ta | 1,003.8 h / 24.4 h transcribed (14,923.7 h / 848.2 h total) | CC-BY-4.0 | **Captioner** (in-domain phone/noise; tag-derived event labels); accent probe (state/district); phone-channel generator targets |
| IndicVoices (incl. 8 kHz conversations) | hi / ta | 445K / 423K train rows (hours not on card) | CC-BY-4.0 | Captioner (channel/space variety, age_group/area); Tamil accent probe |
| Kathbath | hi / ta | 150.2 h / 185.1 h | CC-BY-4.0 / CC0 | Captioner (read phone speech); SV negatives |
| Vaani-Benchmark-V1.0 | hi | 10.9 h, 1,062 spk | CC-BY-4.0 | **Eval only** (captioner test clips, CER sanity) |
| Lahaja | hi | 12.5 h, 132 spk | CC-BY-4.0 / MIT tag | **Eval only**: L1/region accent probe |
| Tamil dialect shared-task / Bharathi corpus | ta | about 24.5 h, 240 spk | [unverified] | Accent probe eval (4 regions) |

### Three biggest risks

1. **Qwen3-TTS has never seen Hindi or Tamil.** It officially supports 10 languages, and its Hindi/Tamil codec fidelity is unmeasured. CustomVoice has only 9 fixed speakers, which caps the speaker-diversity score. Mitigation:
   - fine-tune Base/VoiceDesign on IV-R + Rasa + LIMMITS;
   - run a tokenizer resynthesis CER/SIM test first;
   - keep Indic-Parler-TTS and IndicF5 as fallbacks.
2. **CER mismeasurement.** IndicConformer's vocabulary has no digits, no Latin and no punctuation. Whisper-style normalisers delete matras. Use NFC, strip punctuation, verbalise numerals, transliterate English, compute corpus-level CER, and calibrate against ground truth (Tamil is structurally about 2× higher).
3. **Weak and unbalanced labels.**
   - Tamil Vaani has only 24 h transcribed.
   - Tamil dialect ID tops out around 73%, so region claims risk hallucination penalties.
   - Vaani is 16 kHz noisy phone audio, and Rasa emotions come from 2 speakers, which invites shortcut learning.

</details>


## Scene simulation, timed control, non-verbal sounds, editing (44)

1. Pyroomacoustics: A Python package for audio room simulations and array processing algorithms (ICASSP 2018) — arXiv:1710.04196 / github.com/LCAV/pyroomacoustics
2. gpuRIR: A Python library for room impulse response simulation with GPU acceleration (Multimedia Tools and Applications 2020) — arXiv:1810.11359 / github.com/DavidDiazGuerra/gpuRIR
3. A Study on Data Augmentation of Reverberant Speech for Robust Speech Recognition (ICASSP 2017), Ko, Peddinti, Povey, Seltzer, Khudanpur — no arXiv; danielpovey.com/files/2017_icassp_reverberation.pdf (read full text)
4. OpenSLR 26 (Simulated RIR database) and OpenSLR 28 (RIRS_NOISES) — openslr.org/26, openslr.org/28
5. Building and Evaluation of a Real Room Impulse Response Dataset, BUT ReverbDB (IEEE JSTSP 2019) — arXiv:1811.06795 / speech.fit.vut.cz
6. Statistics of natural reverberation enable perceptual separation of sound and space, MIT IR Survey (PNAS 2016), Traer & McDermott — mcdermottlab.mit.edu/Reverb/IR_Survey.html (no arXiv)
7. ACE Challenge corpus (WASPAA 2015 / IEEE TASLP 2016), Eaton, Gaubitch, Moore, Naylor — arXiv:1606.03365 (results report) / Zenodo 6257551
8. TS-RIR: Translated synthetic room impulse responses for speech augmentation (ASRU 2021) — arXiv:2103.16804
9. MUSAN: A Music, Speech, and Noise Corpus — arXiv:1510.08484 / openslr.org/17
10. Deep Noise Suppression (DNS) Challenge data (Interspeech 2021 / ICASSP 2023) — arXiv:2101.01902 / github.com/microsoft/DNS-Challenge
11. FSD50K: An Open Dataset of Human-Labeled Sound Events (IEEE/ACM TASLP 2022) — arXiv:2010.00475 / zenodo.org/records/4060432
12. ESC-50: Dataset for Environmental Sound Classification (ACM MM 2015), Piczak — github.com/karolpiczak/ESC-50
13. WHAM! Extending Speech Separation to Noisy Environments (Interspeech 2019) — arXiv:1907.01160
14. Scaper: A library for soundscape synthesis and augmentation (WASPAA 2017), Salamon et al. — github.com/justinsalamon/scaper
15. Deep Feature CycleGANs: Speaker identity preserving non-parallel microphone–telephone domain adaptation for speaker verification (2021) — arXiv:2104.01433
16. Analysis of Speaker Verification Performance Trade-offs with Neural Audio Codec Transmission (APSIPA ASC 2025) — arXiv:2509.02771
17. Codec tooling check (local environment, verified this session) — ffmpeg on this machine; torchaudio AudioEffector tutorial (docs.pytorch.org/audio/2.3.0)
18. PicoAudio: Enabling precise timestamp and frequency controllability of audio events in text-to-audio generation (arXiv 2024) — arXiv:2407.02869
19. AudioTime: A temporally-aligned audio-text benchmark dataset (arXiv 2024) — arXiv:2407.02857
20. AudioComposer: Towards fine-grained audio generation with natural language descriptions (ICASSP 2025) — arXiv:2409.12560
21. Make-An-Audio 2: Temporal-enhanced text-to-audio generation (arXiv 2023) — arXiv:2305.18474 / github.com/bytedance/Make-An-Audio-2
22. PicoAudio2: Temporal controllable text-to-audio generation with natural language description (arXiv 2025) — arXiv:2509.00683
23. FreeAudio: Training-free timing planning for controllable long-form text-to-audio generation (arXiv 2025) — arXiv:2507.08557
24. FlexSED: Towards open-vocabulary sound event detection (WASPAA 2025) — arXiv:2509.18606 / github.com/JHU-LCAP/FlexSED
25. Stable Audio Open (arXiv 2024) — arXiv:2407.14358 / huggingface.co/stabilityai/stable-audio-open-1.0
26. AudioLDM 2 (arXiv 2023) — arXiv:2308.05734 / github.com/haoheliu/AudioLDM2 / huggingface.co/cvssp/audioldm2
27. TangoFlux: Super fast and faithful text to audio generation with flow matching and CLAP-ranked preference optimization (arXiv 2024) — arXiv:2412.21037 / github.com/declare-lab/TangoFlux
28. AudioX: A unified framework for anything-to-audio generation (ICLR 2026) — arXiv:2503.10522 / huggingface.co/HKUSTAudio/AudioX
29. AUDIT: Audio editing by following instructions with latent diffusion models (NeurIPS 2023) — arXiv:2304.00830
30. AudioEditor: A training-free diffusion-based audio editing framework (arXiv 2024) — arXiv:2409.12466 / github.com/NKU-HLT/AudioEditor
31. VoiceCraft: Zero-shot speech editing and text-to-speech in the wild (ACL 2024) — arXiv:2403.16973 / github.com/jasonppy/VoiceCraft
32. SSR-Speech: Towards stable, safe and robust zero-shot text-based speech editing and synthesis (ICASSP 2025) — arXiv:2409.07556 / github.com/WangHelin1997/SSR-Speech
33. NonverbalTTS: A public English corpus of text-aligned nonverbal vocalizations with emotion annotations for TTS (arXiv 2025) — arXiv:2507.13155 / huggingface.co/datasets/deepvk/NonverbalTTS
34. NVSpeech: An integrated and scalable pipeline for human-like speech modeling with paralinguistic vocalizations (arXiv 2025) — arXiv:2508.04195
35. CapSpeech: Enabling downstream applications in style-captioned text-to-speech (arXiv 2025) — arXiv:2506.02863
36. EXPRESSO: A benchmark and analysis of discrete expressive speech resynthesis (Interspeech 2023) — arXiv:2308.05725 / speechbot.github.io/expresso
37. Laughter synthesis using pseudo phonetic tokens with a large-scale in-the-wild laughter corpus (Interspeech 2023) — arXiv:2305.12442
38. LaughNet: Synthesizing laughter utterances from waveform silhouettes and a single laughter example (arXiv 2021) — arXiv:2110.04946 (search-result abstract only)
39. Speaking style adaptation in TTS using seq2seq models with attention / Lombard speech synthesis using transfer learning in a Tacotron TTS system (ICASSP 2019 prep. / Interspeech 2019), Bollepalli, Juvela, Alku — arXiv:1810.12051
40. Lombard acoustic correlates and voice conversion (arXiv:2507.09310, Clarity Challenge 2023; arXiv:2309.10485; plus search summaries)
41. Fugatto 1: Foundational Generative Audio Transformer Opus 1 (ICLR 2025), NVIDIA — openreview B2Fqu7Y2cd / proceedings.iclr.cc (full text read from proceedings PDF)
42. ClearerVoice-Studio (MossFormer2 / FRCRN; toolkit paper arXiv:2506.19398) — github.com/modelscope/ClearerVoice-Studio
43. Renderer spec ("ecology renderer"; every label is computed from the render log, not from the request)
44. Three biggest risks

<details><summary>Synthesis</summary>

## Synthesis

### Renderer spec ("ecology renderer"; every label is computed from the render log, not from the request)
1. **Source gate.** Inputs are clean-ish speech (generator outputs, Expresso-style studio data, or best-DNSMOS Vaani). Run MossFormer2 enhancement and measure residual SNR, blind T60 (validated on ACE), bandwidth and FlexSED events on the residual. Record a "pre-existing condition" record. Only state an added property when it clearly dominates what the source already had (e.g., added SNR at least 10 dB below the residual SNR; T60 increase of 0.3 s or more).
2. **Vocal-event insertion.** Forced-align, choose inter-word gaps (≥0.3 s apart, as in CapSpeech), and splice same-speaker NV (generator with inline NV tag, or NV clips from NonverbalTTS/NVSpeech-style tagged Vaani) with 10–30 ms fades. Keep audio outside the edit bit-exact (SSR-Speech principle). Log the span in ms.
3. **Point-source events.** Scaper-style plan: class, file, onset, duration and level relative to speech, from per-class level priors. Sources: FSD50K CC0/CC-BY, ESC-50 (internal only), Stable Audio Open/TangoFlux for fantastical prompts, trimmed by an onset detector.
4. **Room.** 50% real RIRs (OpenSLR 28, BUT ReverbDB, MIT survey) and 50% pyroomacoustics ISM+ray at 24/48 kHz with random sub-band EQ (TS-RIR lesson). Use different source positions for speech and events. Labels: T60, DRR, C50 computed from the RIR.
5. **Background bed.** DNS CC0/CC-BY noise, WHAM! (internal), MUSAN noise. SNR is defined on active-speech loudness, sampled 0–30 dB, with the *achieved* SNR logged.
6. **Coupling.** Lombard only when generated under the condition; otherwise the label says "no effort change".
7. **Channel.** ffmpeg chain: band-pass, then G.711, GSM, Opus 6–24 kbps, G.722 or Codec2 (AMR-NB needs an ffmpeg rebuild), then packet loss, then AGC. Describe audible properties, not codec names.
8. **Label compiler and QC.** Salience thresholds, then Fugatto-style LLM-written instruction generators (Qwen3-8B), absolute and relative (dry/wet). QC: FlexSED must re-detect each event within ±250 ms after the channel; drop failures.

### Three biggest risks
1. **Sim-to-real gap and shortcut learning.** PicoAudio2 simulated-only training dropped Seg-F1 from 0.857 to 0.589, and AudioComposer lost 13 F1_seg without real data. Mitigation: mix real pseudo-labelled clips every round; keep a held-out real test set.
2. **Label ≠ percept on noisy Vaani bases**, plus masked events that become hallucinated "true" items the grader marks false. Mitigation: source gate, salience thresholds, re-detection QC.
3. **Unnatural edits.** Splice artefacts, poor event quality (CapSpeech IMOS) and missing Lombard coupling hurt naturalness CMOS and could teach the captioner wrong correlations. Licence hygiene (NC/ND/AGPL) is a secondary manifest risk.

</details>
