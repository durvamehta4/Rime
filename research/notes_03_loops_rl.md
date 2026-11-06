# Notes 03: self-improving and mutually-improving loops, synthetic data, pseudo-labelling, preference/RL alignment for speech

Cluster owner: lit-review agent 03. Written 2026-11-04 for the Track 2 brief (Hindi and Tamil captioner <-> generator loop).
Method: abstracts plus method and results sections read through arxiv.org/abs, arxiv.org/html, or the PDF text. Numbers are copied from the papers. Anything I could not confirm is marked [unverified]. Where I only read the abstract, the entry says so.

Papers read: 41 (grouped A–H below).

---

## A. Classic closed loops and self-training

### Listening while Speaking: Speech Chain by Deep Learning (ASRU 2017 [venue unverified, arXiv lists none]) — arXiv:1707.04879
- **Key idea:** Couple ASR and TTS in a closed loop. Each model labels unpaired data for the other: speech-only data goes ASR -> text -> TTS reconstruction loss, and text-only data goes TTS -> speech -> ASR reconstruction loss.
- **Method:** Seq2seq ASR and Tacotron-like TTS. Supervised warm-up on a small paired set, then joint training on paired plus unpaired data. A coefficient α weights the paired loss against the unpaired loss.
- **Key numbers:** BTEC single-speaker: ASR CER fell by 4.6% (absolute or relative not stated clearly) compared with the paired-only model, and TTS MSE also improved. Multi-speaker WSJ: both models improved, but α=0.5 (more weight on paired data) beat α=0.25 *because the baseline was weaker*.
- **Takeaway for Track 2:** This is the original "two models teach each other" design. The weaker the round-0 models, the more weight the real or paired anchor data needs. Start with a high anchor weight and lower it only once both models are strong.

### Improving Neural Machine Translation Models with Monolingual Data (ACL 2016) — arXiv:1511.06709
- **Key idea:** Back-translation. Pair real target-side monolingual text with synthetic source sentences produced by a reverse model, then train the forward model on the result as extra parallel data.
- **Method:** No architecture change. Synthetic pairs are mixed with real parallel data.
- **Key numbers:** WMT15 En<->De +2.8 to +3.7 BLEU. IWSLT14 Tr->En (low-resource) +2.1 to +3.4 BLEU.
- **Takeaway for Track 2:** Put the synthetic material on the *input* side and keep the *target* side real. For the captioner, that means real audio with machine-written captions is the weak side. The stronger direction is a *known* description (from controlled transforms or templates) -> generator audio -> captioner learns to recover the known description. Real-side targets are the reason back-translation does not drift.

### Dual Learning for Machine Translation (NIPS 2016) — arXiv:1611.00179
- **Key idea:** A primal model and a dual model (En->Fr, Fr->En) play a game on monolingual data with RL rewards.
- **Method:** Reward = LM likelihood of the intermediate output (fluency) + reconstruction log-likelihood after the round trip. Policy gradient on both models.
- **Key numbers:** Fr->En with a 10% bilingual warm start matched NMT trained on 100% of the bilingual data (abstract only; no table read).
- **Takeaway for Track 2:** Round-trip reward = description -> generator -> captioner -> description', scored by claim agreement. The round trip alone can be satisfied by a *private code* the two models share (steganography-like), so add a naturalness/prior term (like dual learning's LM term) and an external verifier. Never rely on cycle consistency alone.

### Self-training with Noisy Student improves ImageNet classification (CVPR 2020) — arXiv:1911.04252
- **Key idea:** Teacher pseudo-labels unlabeled data. An equal-or-larger student trains with noise (dropout, stochastic depth, RandAugment). The student becomes the next teacher. Iterate.
- **Key numbers:** 88.4% top-1 on ImageNet with 300M unlabeled images. ImageNet-A 61.0 -> 83.7.
- **Takeaway for Track 2:** Noise the student and not the teacher. For the captioner student, augment the audio (codec, RIR, noise) while labels come from the clean-input teacher plus known-transform labels. This also builds robustness to Vaani phone channels.

### Improved Noisy Student Training for Automatic Speech Recognition (Interspeech 2020) — arXiv:2005.09629
- **Key idea:** Noisy Student for ASR, with SpecAugment as the noise, plus filtering, balancing and "gradational" schedules across generations.
- **Method:** Filtering score s = (S − μℓ − β)/(σ√ℓ) normalises the fusion score by transcript length, with parameters re-fit on dev for each generation. *Gradational filtering*: cutoff relaxed over generations (1, 0.5, 0, −1, −∞ across gens 1–5). *Gradational augmentation*: SpecAugment strength increases as data grows. Token-distribution balancing via sub-modular sampling. Batch-wise mixing of supervised and pseudo-labelled data at a fixed ratio.
- **Key numbers:** LibriSpeech 100h + 860h unlabeled: 4.2/8.6 test-clean/other (prior best 4.74/12.20). 960h + LibriLight-60k: 1.7/3.4. Best model was generation 4 of 0–5, so gains saturate after about 4 generations. A score cutoff of 0 filtered about 50% of utterances.
- **Takeaway for Track 2:** (1) Length-normalise any confidence before thresholding, because long captions have lower total log-probability. (2) Start strict and relax the threshold as the teacher improves. (3) Rebalance pseudo-labelled captions so axes or attributes match the target distribution and frequent "phone, quiet room, neutral" captions do not dominate. (4) Most of the gain arrives in the first 1–2 generations, which matters here because fewer rounds are rewarded.

### STaR: Bootstrapping Reasoning With Reasoning (NeurIPS 2022 [venue unverified on abs page]) — arXiv:2203.14465
- **Key idea:** Generate rationales, keep only those that reach the correct answer, fine-tune, repeat. "Rationalization" regenerates a rationale with the answer given as a hint for the failed cases.
- **Key numbers:** On CommonsenseQA, comparable to fine-tuning a model 30x larger (abstract).
- **Takeaway for Track 2:** Filtering on a *verifiable outcome* is the core of every successful self-improvement loop. The "rationalization" analogue for the captioner: for clips with known transform labels, give the captioner the hint (e.g., "reverb RT60≈0.6 s, laugh at 3.2–3.9 s") and have it write a fluent description that includes the hint. This is hint-conditioned caption synthesis, and it fixes failure cases rather than reinforcing successes only.

### Reinforced Self-Training (ReST) for Language Modeling (arXiv 2023) — arXiv:2308.08998
- **Key idea:** Grow step: sample a dataset from the policy. Improve steps: fine-tune (BC/NLL) on samples above a reward threshold that rises each step.
- **Method:** Thresholds τ from [0.0, 0.7, 0.8, 0.9, 0.95, 0.99]. Each Improve step fine-tunes a new policy *from the original data plus the filtered Dg*. MT with the Metric X reward model.
- **Key numbers:** Each Improve step raised the reward-model score on IWSLT14 De-En, WMT20 Zh-En and Web Domain. A second Grow step added +5.3 (IWSLT) and +0.8 (Web Domain) reward points. **However, human evaluation said one Grow step was best, even though the reward kept rising with more Grow steps.** Plain BC beat offline-RL losses (OAC, BVMPO, GOLD). A footnote reports that online PPO quickly exploited BLEU and BLEURT.
- **Takeaway for Track 2:** This is the clearest evidence that *reward goes up while true quality does not* after one or two rounds with a learned reward. Use the captioner-as-reward for at most one or two Grow rounds, check against an independent signal (human spot-check, or a held-out judge not used in training), and prefer filtered-SFT (BC) over complex RL.

### Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models (ReST^EM) (TMLR 2024) — arXiv:2312.06585
- **Key idea:** EM-style self-training with binary correctness reward: generate, filter, fine-tune, repeat.
- **Method:** 32 samples per MATH problem and 64 per APPS problem (top-K 40, T=0.7). **At most 10 kept solutions per problem**, to avoid over-representing easy problems. **Each iteration fine-tunes from the base pretrained model**, not the previous checkpoint, to limit drift.
- **Key numbers:** MATH +5.94% (PaLM2-S) and +6.34% (PaLM2-L). APPS +5.6% and +6.4%. MATH iterations: 1 iteration with 3x data 40.3% < iteration 2 41.0% < iteration 3 41.9%. **APPS iteration 2 regressed** (overfitting on a small training set), and HumanEval transfer also regressed. Beat SFT on human data.
- **Takeaway for Track 2:** (1) Cap the number of synthetic examples per prompt or description so easy cases do not dominate. (2) Retrain from the base checkpoint each round on (real anchor + all verified synthetic), not by continued fine-tuning. (3) With small pools (Tamil, about 850 h, and far fewer verified clips), expect regressions in round 2. Gate each round on held-out improvement.

### Self-Rewarding Language Models (ICML 2024) — arXiv:2401.10020
- **Key idea:** One model generates responses *and* judges them (LLM-as-judge, 5-point additive rubric). Iterative DPO on its own judgments.
- **Method:** N=4 samples per prompt. Score averaged over 3 judge samples. Pair = highest vs lowest score, ties dropped.
- **Key numbers:** AlpacaEval 2.0 win rate vs GPT-4 Turbo: M1 9.94% -> M2 15.38% -> M3 20.44%. Judge agreement with humans 65.1 -> 78.7 -> 80.4 -> 81.7%. **Response length grew from about 1092 to 1552 to 2552** across iterations. Only 3 iterations were run, and reward hacking was not studied.
- **Takeaway for Track 2:** The captioner can improve as a *judge* while improving as a captioner, but verbosity is the default exploit. Our rubric penalises false items, and the grader cuts descriptions at 300 words, so add explicit length control and score claim precision, not overall quality.

---

## B. Model collapse and data accumulation

### AI models collapse when trained on recursively generated data (Nature 631:755–759, 2024; arXiv preprint "The Curse of Recursion") — arXiv:2305.17493, DOI 10.1038/s41586-024-07566-y
- **Key idea:** Recursive training on generated data makes the tails of the distribution disappear. Shown for GMMs, VAEs and LLMs.
- **Method:** OPT-125m fine-tuned on wikitext2, each generation trained on data generated by the previous one.
- **Key numbers:** With no original data kept, perplexity rose from about 20 to about 28 (real-data fine-tune ≈34; zero-shot 115; numbers as reported in the arXiv v3 HTML). **With 10% of original data preserved, there was only "minor degradation."** Causes: statistical approximation error (finite sampling, the primary cause) and functional approximation error. A repetition penalty did not prevent collapse. Later generations also showed a "much longer tail" of outputs the original model would almost never produce, i.e. accumulated errors.
- **Takeaway for Track 2:** The tails at risk here are rare voices, Tamil dialects, unusual events and creaky or falsetto voice. These are exactly what the rubric's timed items and the speaker-diversity score reward. Always keep real Vaani data in every round's training mix.

### Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (arXiv 2024; later COLM 2024 [unverified]) — arXiv:2404.01413
- **Key idea:** *Replace* (train only on the latest synthetic data) collapses. *Accumulate* (real + all previous synthetic) does not.
- **Key numbers:** Holds across LM pretraining, diffusion models (molecules) and VAEs (images). Linear-model theory: test error under accumulation has a finite upper bound regardless of the number of iterations, while under replacement it grows with iterations.
- **Takeaway for Track 2:** Training data for round r = Vaani real + transform-labelled real + ∪_{k≤r} verified synthetic. Never drop earlier rounds. Record in the manifest which round and labeler produced each example (the brief already requires this).

### Self-Consuming Generative Models Go MAD (ICLR 2024 [venue unverified on abs page]) — arXiv:2307.01850
- **Key idea:** Three loop types: fully synthetic, synthetic augmentation (fixed real set), and fresh-data loop (new real data each generation). Plus sampling bias λ (cherry-picking for quality).
- **Key numbers:** Fully synthetic: precision and recall both fall. With bias, precision can hold but recall (diversity) falls faster. A fixed real set only *delays* MAD. Fresh real data *prevents* it, converging to a level that depends on n_real, n_synth and λ. Stronger quality bias lowers the amount of synthetic data that can be mixed in safely. Mostly Gaussian simulations plus image models.
- **Takeaway for Track 2:** Quality filtering (best-of-N, DPO winners) is sampling bias λ<1 and directly erodes diversity. The speaker-diversity score (2 pts) counts distinct speakers over 10 samples, so selection must be diversity-aware. Bring *new* real Vaani clips into each round (14,900 h Hindi is far from exhausted). Tamil is the scarce side.

---

## C. Preference / RL alignment for TTS (codec-LM and flow)

### SpeechAlign: Aligning Speech Generation to Human Preferences (NeurIPS 2024 [unverified]) — arXiv:2404.05600
- **Key idea:** Pair golden codec tokens (preferred) with the model's own generated tokens (dispreferred) for the same text, then iterate preference optimisation.
- **Method:** About 50k LibriSpeech pairs, growing to 100k (new + previous). Compared CoH, DPO, RLHF-PPO and Best-of-N. 8xA100. DPO: batch 128, LR 5e-7, 2000 steps.
- **Key numbers:** LibriSpeech WER/SIM: SFT 7.2/0.87 -> DPO it1 6.7/0.88 -> it2 6.2/0.89 -> it3 6.0/0.90. PPO 7.1/0.89. Continued SFT on golden tokens 8.0/0.88 (no gain). **Small 130M model: iteration 1 helped (11.4->9.3 WER), then WER drifted upward in later iterations.**
- **Takeaway for Track 2:** DPO beats PPO and plain SFT for codec-LMs at low cost. Iteration helps big models but hurts small ones. Qwen3-TTS 1.7B is mid-sized, so plan one round with an optional second gated by held-out results.

### Preference Alignment Improves Language Model-Based TTS (Tian et al., ICASSP 2025 [venue unverified]) — arXiv:2409.12403
- **Key idea:** A systematic DPO study on a 1.15B multi-scale-transformer codec LM (55k h English).
- **Method:** 10 samples per condition. Winner = top 20%, loser = bottom 20% by metric. Rank by WER, SPK_SIM, proxy MOS, or a combined rank.
- **Key numbers:** test-clean WER 4.5->3.0, SPK_SIM 0.635->0.667, proxy MOS 3.80->4.23. Gains held on *unseen* metric models (OWSM WER 5.0->3.2, ECAPA SIM, DNSMOS). β=0.01 was best. **GT-as-winner pairs were too easy (99.8% win after 20 updates), so self-generated pairs work better.** WER-only ranking gave the weakest WER; combined ranking was the most balanced. **Works with 1 hour of data (258 pairs).** **A second DPO round hurt (WER 3.1->5.1).** DPO lengthened outputs (+5.1% vs GT); length normalisation reduced this.
- **Takeaway for Track 2:** This is the most directly usable recipe. Self-sampled pairs, multi-metric combined rank, β≈0.01, small data is enough, and evaluate with metric models *not* used for ranking (e.g., rank with a different ASR than IndicConformer and evaluate with IndicConformer). Treat iteration as fragile.

### Enhancing Zero-shot Text-to-Speech Synthesis with Human Feedback (UNO) (arXiv 2024) — arXiv:2406.00654
- **Key idea:** Uncertainty-aware optimisation. A KTO-style loss on *unpaired* desirable/undesirable labels, with label uncertainty scaling the KL allowance (1/u replaces β).
- **Method:** VoiceCraft 330M/830M. K=400 samples drawn from varied speaker prompts. Labels from MOS simulators trained on SOMOS (or 3 human listeners, with uncertainty set from agreement).
- **Key numbers:** WER 8.4->2.4%, SIM 0.84->0.92, MOSNet 3.65->4.31, human MOS 3.38->4.06 (GT 4.55). About 10 min for 400 samples on one A100. Emotional TTS valence 0.55->0.67.
- **Takeaway for Track 2:** Binary "passes verification / fails" labels from the captioner-judge fit a KTO/UNO-style loss directly, without needing pairs. Judge uncertainty (e.g., disagreement across judge samples) should *shrink* the update. Very cheap, so it fits 4xL4.

### Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance (EMNLP 2025 [unverified]) — arXiv:2502.05236
- **Key idea:** Encoder-decoder codec-LM TTS with DPO/RPO using ASR-CER and speaker-verification rewards, plus CFG.
- **Method:** 6 samples per (text, speaker). Pareto ranking on CER and SSIM. Chosen = top, rejected = bottom. Pairs dropped if the chosen sample is worse on *either* metric. About 58k pairs, including 800 hard repeated-word texts. LR 2e-7, β=0.01, ≤4k iterations, batch 64. CFG with 10% condition dropout and γ=2.5.
- **Key numbers:** Unseen speakers: CER 2.56->0.62 (DPO) ->0.58 (+CFG). SSIM 0.601->0.645->0.678.
- **Takeaway for Track 2:** (1) Use Pareto or dominance filtering across rewards so no metric regresses: require the chosen sample to beat the rejected one on CER *and* description adherence. (2) CFG on the *description* condition is an inference-time lever for instruction relevance, and is cheap if Qwen3-TTS supports condition dropout. (3) Include hard texts deliberately.

### Seed-TTS (ByteDance tech report 2024), Section 4.2 RL — arXiv:2406.02430
- **Key idea:** RL fine-tuning of the zero-shot ICL model with REINFORCE using reward models, compared against DPO.
- **Key numbers:** RL-SIM-WER: WER EN 2.249->1.945, ZH 1.115->1.002, hard 7.585->6.423. SIM slightly up. CMOS +0.14 vs ICL. RL-SER: emotion accuracy angry 0.46->0.91, happy 0.44->0.80, sad 0.53->0.78, surprise 0.13->0.82. **Reward hacking: optimising WER made speech slower and over-articulated, hurting naturalness.** Self-distillation via speaker perturbation improved timbre disentanglement (VC SIM 0.491->0.753 EN).
- **Takeaway for Track 2:** A classifier reward per attribute (emotion, etc.) gives large controllability gains. This is evidence that per-axis verifiers (pitch, rate, reverb, event detectors) can steer the generator. Guard against WER-reward over-articulation, which would hurt CMOS naturalness (2 pts). The speaker-perturbation self-distillation idea suits the speaker-diversity requirement, because it forces timbre to come from the description or speaker prompt.

### CosyVoice 3: Towards In-the-wild Speech Generation via Scaling-up and Post-training (2025) — arXiv:2505.17589
- **Key idea:** DiffRO computes rewards directly on speech tokens. A Token2Text ASR-like model gives log P(text | tokens), and Gumbel-softmax makes the reward differentiable, so training is backprop rather than RL rollouts through the vocoder. Token-level KL to the reference.
- **Key numbers:** SEED test-zh CER 1.16->0.75 (0.5B). test-en 2.02->1.76. CV3-Eval hard-zh 14.15->8.26. Korean 12.8->4.02. RL slightly *reduces* speaker similarity. DiffRO-EMO raised emotion accuracy (happy 0.64->0.98) but can hurt pronunciation. Multi-task reward (SER, MOS, AED) is described but only the emotion variant is reported.
- **Takeaway for Track 2:** Qwen3-TTS-12Hz is also a token LM. A token-level critic (a small classifier on codec tokens predicting text, or description attributes) avoids decoding audio for every rollout. That matters on 4xL4. Expect a pronunciation vs style trade-off, so keep a CER term in the reward at all times.

### F5R-TTS: Improving Flow-Matching based Text-to-Speech with Group Relative Policy Optimization (2025) — arXiv:2504.02407
- **Key idea:** Make flow-matching outputs Gaussian (predict μ, σ) so GRPO can compute log-probabilities. Reward = λ_W(1−WER) + λ_S·SIM.
- **Key numbers:** GRPO took 1,100 updates on 8xA100-40G using only 100 h. WenetSpeech4TTS ZH WER 2.10->1.48 (−29.5% rel), SIM 0.698->0.730. Hard set WER 11.30->10.63. Reward hacking was not analysed. Group size not stated.
- **Takeaway for Track 2:** GRPO on TTS converges in about 1k steps on about 100 h, which is affordable. Most relevant if we switch to a flow-based generator. For the codec-LM path, DPO is simpler.

### Emo-DPO: Controllable Emotional Speech Synthesis through Direct Preference Optimization (ICASSP 2025 [unverified]) — arXiv:2409.10157
- **Key idea:** Pairs are the same text in the target emotion (chosen) vs another emotion (rejected), with a JSD regulariser for stability.
- **Method:** CosyVoice-300M-Instruct initialisation. ESD (10 speakers × 5 emotions). DPO 3 epochs, batch 8, 4 GPUs.
- **Key numbers:** Emotion similarity 98.87 vs CosyVoice 98.73. Prosody similarity 3.89 vs 3.69. AB preference 88.7% vs CosyVoice.
- **Takeaway for Track 2:** *Contrastive-attribute pairs* (same text, description says X, rejected = audio that matches description ¬X) teach the generator to *differentiate* attributes. We can make these for free: render "breathy" vs "modal", or "reverberant hall" vs "dry", by controlled transforms or prompting. This directly targets instruction relevance (5 pts).

### Advancing Zero-shot TTS Intelligibility across Diverse Domains via Preference Alignment (INTP) (ACL 2025) — arXiv:2505.04113
- **Key idea:** A 251k-pair intelligibility preference dataset. Intra-model pairs (lowest vs highest WER of N samples, with a WER-gap threshold), inter-model pairs, and perturbed-text negatives. Hard texts (repeats, code-switching, rewrites) come from DeepSeek-V3.
- **Key numbers:** Average WER: ARS 24.47->15.41, F5-TTS 17.78->9.62, MaskGCT 14.04->9.73, CosyVoice2 13.09->10.56, Ints 11.97->7.96. Weak-to-strong: models not used to build INTP still improved. **Iterative round 2 on a challenging-prompt subset: 7.96->7.10, much smaller than round 1.** Human check: intra-pair labels 90.4% accurate for CosyVoice 2.
- **Takeaway for Track 2:** (1) Round 2 should *target hard prompts only* (weak-area focus). Expect diminishing returns. (2) LLM-generated hard text is cheap with Qwen3-8B locally: Hindi-English code-mixing and Tamil numerals. (3) Perturbed-input negatives = description perturbations (Tango 2-style), see below.

### FlexiVoice: Enabling Flexible Style Control in Zero-Shot TTS with Natural Language Instructions (arXiv 2026) — arXiv:2601.04656
- **Key idea:** Progressive post-training: (S1) DPO on emotion-contrast pairs; (S2) multi-objective GRPO with an emotion2vec SER probability plus a CAM++ speaker-verification binary reward, to disentangle instruction from reference timbre; (S3) instruction GRPO with **Kimi-Audio-7B-Instruct as a binary yes/no judge** of instruction adherence.
- **Key numbers:** InstructTTSEval average 66.4 (base) -> 69.0 (S1) -> 71.7 (S2) -> 79.3 (S3). Order matters: S3 alone 72.3, joint S2+S3 75.5 (conflicting gradients), sequential 79.3. A small share of S2 data mixed into S3 counters forgetting. 14k instruction-text inputs for S3, with 6k instructions from DeepSeek-V3. Group size and compute not reported in the part I read.
- **Takeaway for Track 2:** The closest public analogue of "captioner as reward for the generator". An open audio-LLM judge giving *binary* adherence per instruction works for GRPO. Apply it *per statement* of the description, since the human relevance check is per statement. Stage rewards in sequence (DPO for easy attributes, then GRPO with the judge) rather than summing everything.

### Diagnose, Then Refine: A Closed-Loop TTS System with AudioLLM-Guided Correction (LoopTTS) (EMNLP 2026) — arXiv:2608.28970 [abstract only]
- **Key idea:** An AudioLLM judge localises prosodic defects and writes refinement instructions. A Refiner TTS re-synthesises the flawed spans. Refiner-DB has 42k examples with AudioLLM word-level weak labels.
- **Key numbers:** Only qualitative human-eval claims in the abstract.
- **Takeaway for Track 2:** An inference-time option for generator relevance: caption the output, diff it against the target description, and regenerate the failing spans or samples. With 10 samples per description required, a cheaper version is reject-and-resample.

---

## D. Text-to-audio alignment with captioner / CLAP rewards

### BATON: Aligning Text-to-Audio Model with Human Preference Feedback (arXiv 2024) — arXiv:2402.00744
- **Key idea:** Collect binary human alignment labels, train a CLAP-based reward model, then reward-weighted fine-tuning of TANGO, regularised with the pretraining loss (β=0.5).
- **Key numbers:** About 2.7k annotated clips. 28.4% (integrity) and 59.4% (temporal order) of generated clips were *misaligned*. CLAP integrity 33.0->35.3, temporal 35.9->41.9. MOS-F temporal 3.83->4.41.
- **Takeaway for Track 2:** Temporal order and event placement are the weakest generator skills, and they match the rubric's *timed* items (±250 ms). Reward-weighted SFT plus a pretraining-loss regulariser is the simplest stable recipe.

### Tango 2: Aligning Diffusion-based Text-to-Audio Generations through Direct Preference Optimization (ACM MM 2024 [unverified]) — arXiv:2404.09956
- **Key idea:** The Audio-Alpaca preference set. (1) Best-of-4 by CLAP. (2) GPT-4 *perturbs the prompt* (swap or remove events) and the audio rendered from the perturbed prompt becomes the loser. (3) Temporal reorder perturbations. Then diffusion-DPO.
- **Method:** Two CLAP checkpoints must agree. Winner CLAP ≥ thresholds. Winner-loser gap Δ within a band (e.g., 0.05–0.35). About 15k pairs. 2xA100, about 3.5 h.
- **Key numbers:** CLAP 0.54->0.57. Human OVL 3.81->3.99, REL 3.77->4.07. FAD slightly worse (2.51->2.69). Removing the perturbation strategies hurt.
- **Takeaway for Track 2:** (1) Use *description perturbation* negatives: change one atomic attribute ("laugh at 3.2 s" -> "at 6 s"; "breathy" -> "modal") to get hard, attribute-specific negatives at no annotation cost. (2) Use **two independent judges must agree** plus a *bounded* margin (drop pairs that are too easy or too close).

### TangoFlux: Super Fast and Faithful Text to Audio Generation with Flow Matching and Clap-Ranked Preference Optimization (arXiv 2024) — arXiv:2412.21037
- **Key idea:** CRPO is an iterative online loop. Each iteration: 20k prompts × 5 samples, CLAP picks winner and loser, train DPO-FM + FM loss on the winner. 5 iterations.
- **Key numbers:** **Online (fresh samples each iteration) kept improving to about iteration 4. Offline reuse of one dataset peaked at iteration 2, then degraded (reward over-optimisation).** Adding the FM loss on winners (CRPO) slowed loss blow-up. CLAP best-of-15 raised CLAP 0.480->0.502 at inference. No CLAP-vs-human correlation was reported.
- **Takeaway for Track 2:** If we iterate generator preference training, *regenerate pairs from the current policy each round* (on-policy) and add an SFT term on winners. At inference, best-of-N reranking by the captioner-judge is a free relevance gain. Pick the 10 eval samples from N>10, but select for *distinct speakers* too.

---

## E. RL / synthetic data for audio LLMs (understanding side)

### Reinforcement Learning Outperforms Supervised Fine-Tuning: A Case Study on Audio Question Answering (R1-AQA) (arXiv 2025) — arXiv:2503.11197
- **Key idea:** GRPO on Qwen2-Audio-7B-Instruct with rule-based rewards (+1 correct, +1 format).
- **Method:** Group 8, 500 steps, LR 1e-6, KL 0.04, 8xH800, about 38k AVQA items.
- **Key numbers:** MMAU test-mini 64.5% (GRPO, answer-only prompt) vs 61.1% (with think) vs LoRA-SFT 56.4% vs full SFT 51.8%. Full SFT *overfit* and degraded on test. Explicit reasoning did not clearly help.
- **Takeaway for Track 2:** For the captioner, RL with *verifiable* rewards on modest data (tens of thousands of items, 500 steps) generalises better than SFT. Transform-labelled clips give verifiable rewards (SNR bucket, pitch shift amount, event time). Chain of thought is not needed.

### Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models (arXiv 2025) — arXiv:2503.02318
- **Key idea:** CoTA, 1.2M synthetic structured-CoT samples (planning/captioning/reasoning/summary) generated mainly by Gemini, with a model-based review stage (True/False hallucination check).
- **Key numbers:** MMAU-mini 49.20->61.71 (Qwen2-Audio base). CoVoST2 and MELD also improved. No rejection rates reported for the review stage.
- **Takeaway for Track 2:** Large synthetic caption corpora help, but they came from a closed teacher, which is fine for training data but not for the final models. We have Qwen3-Omni-Captioner and Qwen3-8B as open teachers. Always add a verification pass, and *report* the rejection rates (rigour points).

### SARI: Structured Audio Reasoning via Curriculum-Guided Reinforcement Learning (arXiv 2025) — arXiv:2504.15900
- **Key idea:** SFT warm-up (about 2k CoT examples), then GRPO on about 30k MCQs ordered *easy -> hard by base-model pass rate*. Questions the base model always fails are removed.
- **Key numbers:** Qwen2-Audio 49.20 -> 65.55 MMAU test-mini. Qwen2.5-Omni variant 67.08. Curriculum gave about +2 points and faster convergence. RL without SFT warm-up produced meaningless reasoning.
- **Takeaway for Track 2:** Curriculum by *current model pass rate* is cheap weak-area targeting. Drop items that are never solved (zero GRPO advantage, and likely label noise). Order the rest easy to hard. Do a short SFT warm-up before any RL.

### Omni-R1: Do You Really Need Audio to Fine-Tune Your Audio LLM? (arXiv 2025) — arXiv:2505.09439
- **Key idea:** GRPO on Qwen2.5-Omni-7B with an accuracy-only reward. QA auto-generated by ChatGPT from Qwen2-Audio captions.
- **Key numbers:** MMAU test-mini 65.9 -> 71.3 (VGGS-GPT synthetic QA, 2000 steps). 4xA6000-48GB. **Text-only fine-tuning on ARC-Easy reached 68.2**, almost as much as AVQA audio training (68.6). Much of the gain is better text reasoning.
- **Takeaway for Track 2:** (1) GRPO on a 7B omni model fits on 4 consumer-class 48 GB GPUs. Our 4xL4 (24 GB) needs LoRA/FP8 and a smaller group size. (2) Caution for evaluation: captioner gains may come from *language priors* rather than listening. Run a "no-audio / shuffled-audio" ablation to show gains are acoustic. Description-rubric points require listening, and priors produce hallucinated true-sounding items.

### AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives (arXiv 2025) — arXiv:2512.24052
- **Key idea:** DPO with *counterfactual hard negatives* covering four hallucination types: event omission, false event identity, temporal relation error, quantitative temporal error. Chosen answers come from GT captions. Rejected answers are LLM-written with a specific injected error.
- **Method:** Qwen2.5-Omni-7B, LoRA r16, β=0.3, 4xA100. AudioTime multi-event subset (11.5k train).
- **Key numbers:** AHA-Eval error rates: temporal relation 30.5->15.9%, event omission 70.6->53.8%, quantitative temporal 69.6->52.6%. MMAU +1.8 with no general regression.
- **Takeaway for Track 2:** For the *captioner*, build DPO pairs where the rejected caption is the chosen caption with one *injected false claim* (wrong time, wrong event, wrong pitch direction). This trains exactly against the rubric's FALSE items and contradictions. With known-transform clips, the ground truth is exact.

### REVE: Efficient Hallucination Correction for Large Audio-Language Models via Reused Encoder States (arXiv 2026) — arXiv:2609.26028 [abstract only]
- **Key idea:** Post-hoc verification of each generated sound-event mention using the LALM's own encoder states (frame-level class readouts). Unsupported mentions are removed.
- **Key numbers:** Removes 92.9% of label-unsupported mentions on AudioSet under a recall constraint. About 1/18 of the latency of a CED-Base verifier.
- **Takeaway for Track 2:** Post-hoc *claim deletion* is a cheap precision booster for the captioner at inference. Event claims can be checked with an audio-event detector (e.g., CED/BEATs-style), and timing with VAD or the detector's frames.

### AVCap: Reinforcing Audio-Video Joint Caption with Detail-Aware Reward (arXiv 2026) — arXiv:2608.06930
- **Key idea:** Da-GRPO. A judge writes N=20 probe questions from the GT caption and answers them from the GT (gold) and from the candidate caption. Reward = mean 0–5 similarity.
- **Method:** Qwen3-Omni-30B-A3B (main) and Qwen2.5-Omni-7B. G=8, 200 steps, LoRA r128, KL 0.01. SFT took about 5 h on 32 GPUs; GRPO about 23 h.
- **Key numbers:** AVCap-Score 53.03 (SFT) -> 56.94. **A holistic 1–5 LLM-judge reward only reached 53.68 and *increased* hallucination (10.4->11.6), while probes lowered it (10.3).** BLEU reward 54.28. Gains saturate near N=20 probes.
- **Takeaway for Track 2:** Use *decomposed, probe/claim-level* rewards for the captioner, not holistic scores. This matches the private rubric's structure (weighted atomic items). Same base model family (Qwen3-Omni-30B-A3B) as our suggested captioner, so LoRA-GRPO is feasible, but 32-GPU-class compute means we must cut steps or group size or use the 7B model on 4xL4.

### AudioMap: Cloze-and-Choice Reinforcement Learning for Time-Aware Dense Audio Captioning (arXiv 2026) — arXiv:2608.09559
- **Key idea:** A frozen examiner LLM answers multiple-choice cloze questions *using only the caption*. **Asymmetric scoring: +1 correct, −0.5 "Not given", −1 wrong.** Plus an event-conditioned temporal reward: the examiner extracts the interval the caption assigns to a named event, scored by IoU with the reference. Length reward flat to 2048 tokens, then linear decay.
- **Method:** Qwen2.5-Omni. SFT then GRPO on 12.5k clips in two curriculum stages, 8 rollouts, KL 0.06, 8xA800.
- **Key numbers:** Omni-Cloze 64.6 (vs scalar LLM-judge reward 58.7, checklist reward 61.1). TACOS temporal 57.4 vs Qwen3-Omni-Captioner 41.5. Removing asymmetric scoring lowered every metric. The temporal reward gave +2.7 TACOS. The paper notes checklist rewards can be gamed by keyword repetition or long unsupported text.
- **Takeaway for Track 2:** **This is almost exactly the Track 2 grading rule** (false/contradicted items cost more than omissions, and timed items count only within a span). Implement the captioner reward as: an examiner (Qwen3-8B, local) answers cloze/MCQ items built from *known* labels (transform metadata plus verified annotations), using asymmetric scoring plus IoU on event times (±250 ms tolerance), with a 300-word length cap. This is the single most actionable paper for the captioner.

---

## F. Synthetic speech data for recognition/understanding; pseudo-labelling at scale

### Hard-Synth: Synthesizing Diverse Hard Samples for ASR using Zero-Shot TTS and LLM (arXiv 2024) — arXiv:2411.13159
- **Key idea:** A weak ASR model finds its *hardest* training utterances (by CER), which become zero-shot TTS prompts. Text is LLM-rewritten (Llama-3.1-8B). Synthetic speech is filtered by a strong ASR (CER>10% dropped).
- **Key numbers:** 16.15 h synthetic on top of 100 h real (about 16%). test-other 17.43->16.67 (hard prompts + rewrite) vs random prompts 17.02. Gender WER gap 2.06->1.66. **About 15 h synthetic was optimal. More (30.87 h) was worse because of the synthetic-real gap.** VoiceCraft beat the higher-quality F5-TTS for ASR utility.
- **Takeaway for Track 2:** This is the weak-area-targeting step (3) of the brief, done for ASR. Pick the captioner's highest-error clips and axes, use them as generator prompts (voice, channel), and synthesise variations. Keep the synthetic share small (about 10–20% of the mix) and verify every sample. Generator perceptual quality ≠ training utility, so measure utility directly.

### On the Effect of Purely Synthetic Training Data for Different ASR Architectures (SynData4GenAI 2024 [venue unverified]) — arXiv:2407.17997
- **Key idea:** Train ASR only on TTS-regenerated LibriSpeech-100 and compare architectures.
- **Key numbers:** AED dev-clean/other: real 7.5/18.9 vs synthetic 14.1/37.6. Oracle durations recover some (10.9/31.8). A bigger TTS helped (AED 14.1->10.5) even when TTS loss suggested overfitting.
- **Takeaway for Track 2:** Purely synthetic training roughly doubles error. Synthetic data must *supplement* real data, not replace it. Prosody and duration realism (timing ms, morphology) is what synthetic speech lacks most, which is also a rubric axis. Do not train the captioner's *timing/prosody* judgments mainly on generator output.

### Scaling Rich Style-Prompted Text-to-Speech Datasets (ParaSpeechCaps) (EMNLP 2025) — arXiv:2503.04713
- **Key idea:** Auto-annotate 59 rich style tags at scale. Situational tags use an expressivity filter (DVA classifier) + text-embedding semantic match + an audio-LLM acoustic check (Gemini rating 1–5, keep top). Intrinsic tags propagate to speakers whose VoxSim speaker embedding has cosine ≥0.8 to an annotated speaker. Mistral-7B turns tags into captions.
- **Key numbers:** 282 h human (342 h in arXiv v1) + 2,427 h auto. Auto-labelled tag *recall* matched human-labelled (situational 71.3 vs 68.1). Each filter stage mattered (dropping the acoustic check: 71.3->63.3). Parler-TTS consistency MOS 3.55->3.83, naturalness 3.10->3.58.
- **Takeaway for Track 2:** (1) Multi-stage *cascade* filtering (cheap classifier -> semantic -> audio-LLM check) is how to scale pseudo-captions on Vaani. (2) Speaker-level attributes (gender, voice quality) can be *propagated* across Vaani clips of the same speaker ID, since the metadata has speaker IDs. (3) Note they measured recall, not precision. We must measure precision, because the rubric penalises false items.

### Empowering Low-Resource Language ASR via Large-Scale Pseudo Labeling (Pratinidhi) (arXiv 2024) — arXiv:2408.14026
- **Key idea:** Hindi pseudo-labelling on YouTube with *consensus* of two transcribers (CTC and RNNT heads, exact match), then evaluators (RNNT Rényi-entropy confidence ≥0.7, SONAR audio-text similarity ≥0.8).
- **Key numbers:** 28,616 h unlabeled -> 4,862 h after consensus (17%) -> 1,840 h after filtering (6.4%). IndicYT WER 33.3->24.7. Out-of-domain Vistaar unchanged (11.9).
- **Takeaway for Track 2:** For Indic data, a *very aggressive* filter (keep about 6%) still gives large gains because the pool is huge. Vaani Hindi has 14.9k h, so we can afford to keep only claims where ≥2 independent labelers agree. Tamil (850 h) needs a lighter filter or more transform-generated data. The same team (AI4Bharat) built IndicConformer, the grader's CER model.

### A Novel Self-training Approach for Low-resource Speech Recognition (Interspeech 2023) — arXiv:2308.05269 [abstract only]
- **Key idea:** Iterative pseudo-labelling for Punjabi with a confidence threshold relaxed across iterations (per search snippet; the abstract does not state the schedule [unverified]).
- **Key numbers:** 14.94% relative WER improvement over baseline across four datasets.
- **Takeaway for Track 2:** Consistent with NST's gradational filtering: a strict-then-relaxed threshold schedule suits low-resource Indic languages.

---

## G. Claim-level verification, hallucination detection, abstention

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023) — arXiv:2305.14251
- **Key idea:** Split long text into atomic facts and verify each against a knowledge source. Score = % supported.
- **Key numbers:** ChatGPT 58% on biographies. The automated estimator (retrieval + LM) had <2% error vs humans. 6,500 generations evaluated, which would have cost $26K with humans.
- **Takeaway for Track 2:** The grader effectively computes a weighted FActScore with penalties. Build our own *offline proxy grader*: Qwen3-8B decomposes captions into atomic claims, and each claim is checked against (a) known transform labels, (b) signal-processing measurements (F0, SNR, RT60 estimate, VAD timings, event detector), and (c) metadata. Use it both as the eval metric (bootstrap CIs) and as the RL reward.

### SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative LLMs (EMNLP 2023) — arXiv:2303.08896
- **Key idea:** Facts the model "knows" recur across stochastic samples. Hallucinated facts vary. Sentence-level consistency scoring needs no external database.
- **Key numbers:** Higher AUC-PR than grey-box baselines (abstract only, no figures read).
- **Takeaway for Track 2:** Sample the captioner K times per clip. Keep claims that appear in ≥m/K samples (claim frequency). This is a training-free precision filter for pseudo-labels *and* for final inference.

### Language Models with Conformal Factuality Guarantees (ICML 2024 [venue unverified]) — arXiv:2402.10978
- **Key idea:** Split output into sub-claims, score each (frequency across 5 samples, or model confidence), drop claims below a threshold calibrated by split conformal prediction so that P(all kept claims correct) ≥ 1−α.
- **Key numbers:** FActScore task: factuality about 25%->about 80% while keeping about half of sub-claims. NQ: +15 points by removing about a quarter. MATH: +15 by removing about 10%. Frequency scoring was the most promising scorer.
- **Takeaway for Track 2:** This gives a *principled abstention threshold* for the captioner. Calibrate the claim-frequency threshold on a small labelled calibration set per language (e.g., the 30 recorded test clips are *not* to be used; record or label a separate set). The rubric score = (true − false)/total, so the optimal threshold maximises expected (precision-weighted) gain, not guaranteed-all-correct. Tune α directly on the proxy grader. Hedging does not count, so drop uncertain claims rather than hedge.

---

## H. Measurement

### Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations (arXiv 2024) — arXiv:2411.00640
- **Key idea:** Treat eval items as samples from a super-population. Report SEs, cluster when items share structure, reduce variance via resampling, use paired comparisons, and run power analysis.
- **Key numbers:** Clustered SEs can be about 3x naive (DROP 1.34 vs 0.44). K resamples per item cut variance (e.g., by about 1/2 at K=4 in the paper's example). Paired SE = √(SE_A²+SE_B²−2·Corr·SE_A·SE_B). Power example: δ=3% needs about 969 items. With n=198, the minimum detectable effect goes from 13.2% (K=1) to 7.5% (K=10).
- **Takeaway for Track 2:** With 30 clips per language, single-sample comparisons can only detect *large* per-round effects. (1) Compare rounds *paired by clip*. (2) Cluster by speaker (Vaani speakers recur). (3) For the generator, the 10 samples per description act as K. (4) Report the minimum detectable effect, and expand the internal dev set (e.g., 200+ clips per language) for decisions while keeping the 30-clip set for reporting.

---

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
