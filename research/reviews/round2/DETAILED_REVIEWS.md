# Additional literature: detailed reading and design consequences

Date: 2026-11-01. This pass deliberately adds **different publications** to the first-pass corpus. All 16 acquired arXiv IDs are absent from the prior 296-record ledger. **Ten received main-text reading**, including methods, experiments, ablations and limitations where present; the remaining six are acquisition leads, not completed detailed reviews. Reading refers to extracted PDF text, not a visual inspection of every figure, a proof audit, a reproduction, or a cover-to-cover appendix review. Page numbers below are PDF page numbers; section/table names are more reliable locators when versions change.

The main-text scope for the ten reviewed papers runs from their introduction through their conclusion/discussion, including tables in that span. CapSpeech's final results table follows its conclusion and was included. The MAD paper's appendices were encountered during extraction but are not counted as comprehensively reviewed. The risk-control paper's main-text theorem and proof discussion were inspected; its assumptions are not established for our data simply by citing it.

Source URLs, publication/update dates and exact acquired PDF hashes are in [ledger.csv](ledger.csv) and the per-paper `*.source.json` files. Those JSON files describe **acquisition status**; the ledger and [STATUS.json](STATUS.json) describe reading status. PDFs and extracted text remain in the ignored local cache. No paper experiments were reproduced. Numerical results below are the authors' reported results, not Rime measurements.

## 1. PromptTTS 2 — describing an underspecified voice

[Paper](https://arxiv.org/abs/2309.02285). Locators: methods §§3–4; experimental results and variation analysis, especially Table 3.

**Question and method.** Natural-language style descriptions omit much of a voice's variability. PromptTTS 2 uses a prompt encoder and a training-time reference encoder, then trains a diffusion variation network to predict reference-derived representations from the prompt. At inference, sampled variation supplies the missing information without requiring a user-provided recording. Prompt and sampled variation are passed to the speech generator. Its prompt pipeline combines recognized attributes with LLM wording. The large underlying recipe uses NaturalSpeech 2 and approximately 44K hours of English MLS; it is not a lightweight training recipe for our hardware.

**Evidence.** The reported mean attribute accuracy is 93.33%, compared with 91.54% and 91.47% for the compared PromptTTS and InstructTTS configurations. MOS is 3.88±0.08 versus 3.77 and 3.80. Table 3 isolates sources of variation: changing the variation-network sample yields WavLM-TDNN similarity 0.355, versus 0.914 for TTS noise, 0.873 for changed content and 0.775 for prompt paraphrases. This supports the claim that decoder noise and paraphrasing are weak substitutes for an explicit variation path.

**Limits.** The similarity number is not the PS's passing-speaker diversity score, and can reflect style as well as identity. English scale and backbone-specific conditioning do not establish Hindi/Tamil transfer. A learned latent may still ignore prompt constraints or entangle identity and delivery. The variation network predicts representations that its own TTS model was trained to consume; arbitrary vectors cannot simply be injected into Indic Parler.

**Rime change.** Move the conditional identity/variation-prior experiment into the first generator round, with an early adapter-interface gate. Train only the supported conditioning interface and small prior. Compare it with named voices and decoder seeds on separate identity, delivery, relevance and within-clip consistency measures. Keep an internal training reference as an implementation option, never an evaluation input.

## 2. ControlSpeech — separate conditioning paths can still conflict

[Paper](https://arxiv.org/abs/2406.01205). Locators: architecture and style mixture semantic density (SMSD) sections; disentanglement and diversity ablations.

**Question and method.** Independent speaker and style control is difficult because a reference recording carries both. ControlSpeech uses a pretrained FACodec with factorized content, prosody, acoustic and timbre representations. It combines phoneme-conditioned content, BERT style representations, a reference timbre embedding and a mixture-density style sampler. Codec prediction, duration estimation and style-density learning use different losses. The pretrained codec's approximately 60K-hour training is outside our budget.

**Evidence.** Removing disentanglement gives pitch/speed/volume/emotion accuracies of 0.492/0.517/0.582/0.237, compared with 0.833/0.829/0.894/0.557 for the full system in the reported ablation. However, its pitch result does not beat PromptTTS 2's 0.867 in that comparison. SMSD improves style-diversity MOS from 3.66 without SMSD to 4.05. These results support investigating conditioning conflict and stochastic style realizations, not claiming universal superiority.

**Limits.** Style-diversity MOS is not distinct-speaker count. The original system requires a timbre reference. Codec factorization is learned, not proof of causal independence; borrowing its names without a compatible codec achieves nothing. We did not comprehensively review the appendix's mixture choices.

**Rime change.** Use different variables for stable clip identity and local delivery. Before adding losses, run a swap test: vary delivery while holding identity fixed, then vary identity while holding text/delivery fixed. If an existing Indic model's interface cannot preserve these controls, restrict the claim or change the interface; do not retrain FACodec from scratch.

## 3. LibriTTS-P — speaker impressions are not local delivery labels

[Paper](https://arxiv.org/abs/2406.07969). Locators: annotation protocol, evaluation tables and limitations.

**Question and method.** The dataset combines speaker-level human descriptions with automatically derived utterance-level pitch, rate and loudness descriptions. Three annotators hear five clips per speaker. The resulting resource has 373,868 prompts for 2,443 English LibriTTS-R speakers. Continuous measurements are binned with a 10/20/40/20/10 percentile scheme. This separation of annotation scales is more informative than treating every sentence as a uniform style label.

**Evidence.** Agreement drops for intensity adverbs: reported Jaccard values with adverbs are roughly 0.057–0.151, versus 0.215–0.370 without them. Their TTS comparison improves naturalness MOS from 2.47 to 3.37 on a five-point scale, but prompt consistency changes only from 3.06 to 3.11 on its four-point scale. For captioning, human-counted correct terms rise from 2.09 to 5.24 while incorrect terms remain 0.66; caption length rises from 11.42 to 25.56 words. More correct content does not itself demonstrate fewer false claims.

**Limits.** Authors caution that reference differences make some automatic caption-score comparisons unsuitable. Read speech and coarse bins do not cover whisper-to-fast transitions, speaker interactions, or all three PS axes. Subjective perceived speaker characteristics are not biographical ground truth. The paper explicitly notes the lack of temporal style changes.

**Rime change.** Store global identity evidence separately from interval-level delivery. Do not copy a speaker description to every segment as if locally verified. Test paraphrases for preservation of intensity, negation, timing and quantities. Measure false assertions independently of descriptive coverage.

## 4. StyleCap — a compact delivery expert rather than another large model

[Paper](https://arxiv.org/abs/2311.16509). Locators: speech representation comparison, prefix-length ablation, augmentation examples.

**Question and method.** StyleCap learns an aggregation network and mapping from frozen speech features into prefix vectors for a frozen text decoder. Its WavLM BASE+ path uses learned layer weights, BLSTM and attention aggregation. The experiments compare these features with mel representations and speaker-verification x-vectors, as well as GPT-2/Llama 2 decoders. Forty prefix vectors work best in the reported comparison; very short prefixes underfit and longer ones can overfit.

**Evidence.** In the reported style-factor evaluation, WavLM reaches 76.8% average accuracy versus 57.0% for speaker x-vectors. X-vectors retain gender information (94%) but are weak on pitch (40.5%), speed (44.0%) and volume (49.4%). Richer decoders help in combination with suitable speech features; they do not rescue every input representation. Rephrasing improves some configurations, but an example introduces the semantically wrong phrase “normal height” for pitch.

**Limits.** A pooled global vector cannot localize changes within 30 seconds. The work does not establish Hindi/Tamil performance, false-claim control, event understanding or intent recognition. Embedding similarity is insufficient to catch all paraphrase corruption.

**Rime change.** Cache a frozen WavLM layer mixture and train a small global/windowed delivery head alongside the main audio-language captioner. Reuse one large semantic backbone, rather than adding another 7B captioner just for prosody. Keep speaker-verification embeddings for identity diagnostics. Train/reject the optional delivery head according to native held-out gains.

## 5. ParaCLAP — a similarity score is not a universal verifier

[Paper](https://arxiv.org/abs/2406.07203). Locators: query generation, training protocol and cross-corpus results.

**Question and method.** ParaCLAP aligns an emotion-pretrained wav2vec 2.0 audio encoder with BERT text features, using contrastive learning and language queries derived from emotion and acoustic measurements. Its audio branch has approximately 160M parameters and its text branch approximately 110M. Acoustic query attributes derive from eGeMAPS features. Training uses approximately 110 hours of English MSP-Podcast clips, with English and German transfer tests.

**Evidence.** Query diversity is not an unconditional win. On IEMOCAP, emotion-only queries score 0.567 UAR versus 0.560 for the combined-query version, 0.309 without emotion queries and 0.353 for generic CLAP. On two-class FAU Aibo, extended queries improve UAR from 0.535 to 0.604. The paper discusses sadness bias and domain mismatch. Approximately 17.5% of training examples are removed for label disagreement. The described best-epoch selection uses the MSP test set, which weakens a clean validation interpretation.

**Limits.** These are task-specific recognition metrics, not probabilities that arbitrary claims are true. An English emotion encoder's apparent agreement with a caption can be correlated error. Emotion is not communicative intent. Discarding uncertain examples may remove exactly the hard cases the PS values.

**Rime change.** Treat semantic audio-text scores as features, never as the sole reward or pass criterion. Calibrate native pairwise claim checks, including hard negatives and ambiguous speech. Keep disagreement and domain flags; do not simply retain easy high-similarity synthetic examples.

## 6. Brouhaha — output frame rate is not measurement resolution

[Paper](https://arxiv.org/abs/2210.13248). Locators: simulation/labels, multi-task architecture, synthetic and real evaluations.

**Question and method.** A SincNet plus three bidirectional LSTM layers jointly estimates speech activity, SNR and room C50. Training uses approximately 1,250 synthetic hours from speech, AudioSet noise and 385 room impulse responses. Speech and noise can be reverberated separately before mixing. SNR labels use a **two-second sliding window**, shifted by 10 ms. C50 is a property of the sampled room response, broadcast to frames. Model output is approximately every 16 ms.

**Evidence.** The reported synthetic three-task setup has VAD performance 93.7 and C50 MAE 3.5 dB. A real BUT ReverbDB evaluation reports C50 MAE 1.1 dB and R² 0.85. Reported SNR MAE depends on clipping/range; the 2.3 dB result for clipped [-15,30] dB values is not an unbounded guarantee. On real BabyTrain, VAD is 77.2 versus pyannote's 80.8 despite favorable synthetic results elsewhere.

**Limits.** Fine output timestamps do not mean independent 16 ms SNR truth or the ability to identify instantaneous room changes. Single-channel estimates are affected by content and domain. C50 does not identify room materials or an exact microphone distance. This estimator cannot independently validate a scene if its own predictions were used as the only training labels and judge.

**Rime change.** Every measured feature carries its analysis window, valid region and uncertainty. Describe ecology at a supported timescale. In synthesis, give foreground and backgrounds their own acoustic paths and prevent accidental double reverberation. Use known simulation parameters plus independent listening/measurement checks for validation.

## 7. PENN — pitch accuracy requires a voicing mask

[Paper](https://arxiv.org/abs/2301.12258). Locators: periodicity/decoding methods, component ablations and cross-domain results.

**Question and method.** The paper improves neural pitch estimators with fine pitch bins, normalization, local expectation decoding and entropy-based periodicity. Unpitched frames receive random pitch targets during training, encouraging a diffuse posterior. Periodicity is derived from normalized posterior entropy; it is a model estimate, not a perfect voicing label. Speech/music coverage in the training distribution matters for pitch extremes. Model-specific resampling is internal to the estimator.

**Evidence.** The reported FCNF0++ configuration reaches mean pitch error 12.45 cents and voiced/unvoiced F1 0.9816 on the paper's aggregated speech/music evaluation. Removing unvoiced training changes pitch error only slightly (12.62 versus 12.72 cents in that ablation), but voicing F1 drops to 0.8496. Thus a good pitch error on valid frames can hide severe failures in identifying valid frames. Speech-only and music-only training differ in frequency coverage. CPU/RTX 3090 speed figures are not T4 benchmarks.

**Limits.** The tests do not establish accuracy on Hindi/Tamil whispers, creak, overlap or highly noisy clips. Mean F0 is not a complete timbre representation, and pitch variance is not equivalent to expressiveness or intent. Octave errors can appear as spurious style changes. Do not copy OCR-corrupted equations or verbal inequality typos as implementation specifications.

**Rime change.** Mask pitch with calibrated voicing/periodicity, overlap and range flags. Use robust voiced-frame log-F0 summaries and a relative contour, not an unconditional mean including silence. Allow “no reliable pitch estimate.” Keep the original waveform/sample rate for other tasks and resample only each specialist's view.

## 8. Conformal Risk Control — define the loss before claiming control

[Paper](https://arxiv.org/abs/2208.02814). Locators: main theorem/algorithm, non-monotone loss and distribution-shift sections.

**Question and method.** CRC chooses a threshold for exchangeable, bounded, non-increasing and right-continuous losses. With loss bound B, calibration size n and target α, its corrected empirical condition is `n/(n+1) * Rhat(λ) + B/(n+1) <= α`; the threshold convention and a safe extreme must satisfy the theorem's conditions. The base result controls **expected risk marginally over calibration and a future test example**. It is not a per-clip guarantee or a 95% high-probability risk guarantee.

**Evidence.** The theorem establishes a finite-sample result under its assumptions; worked vision/NLP tasks illustrate it. The non-monotone discussion explicitly shows that dropping the monotonicity assumption can fail badly; a monotone envelope can be conservative. Distribution-shift variants require additional information/assumptions, such as suitable importance weights. They do not automatically handle unknown Hindi/Tamil distribution shift.

**Limits.** Ordinary false-discovery rate (false claims divided by retained claims) need not be monotone as a threshold changes. Refilling a word budget, rewriting accepted statements or proposing new claims after thresholding can destroy nestedness. Correlated clips from the same speaker/session are not automatically exchangeable independent examples. Threshold tuning on the calibration set beyond the specified rule invalidates a simple split interpretation. A proxy loss does not become the organizers' weighted score.

**Rime change.** Freeze claim proposal, ranking, maximum count M and text budget first. Increasing λ may only remove proposed claims. Use a bounded monotone proxy `false retained claims / M`, with unresolved claims conservatively counted as false for calibration. Preserve accepted meaning with an audited deterministic prose renderer. Tune on development data; calibrate once on separate native data; evaluate on a separate audit. Calibrate per language only with sufficient independent units. When assumptions cannot be justified, publish empirical risk/coverage curves without a theorem claim.

## 9. CapSpeech — speech fluency does not imply correct sound events

[Paper](https://arxiv.org/abs/2506.02863). Locators: §III datasets/tasks, §IV implementation and Tables III, VI–VIII, conclusion.

**Question and method.** CapSpeech combines large-scale machine-labeled English speech with human-labeled adaptation sets, and evaluates general style, accent, emotion, sound-event and agent TTS. Its AR baseline is Parler-based; its NAR baseline adapts F5-TTS with caption cross-attention and a duration predictor. Sound-event insertion/background positions use control markers; the NAR branch additionally conditions on CLAP event embeddings. Automatic caption tags include PENN-derived pitch and rate measurements, then LLM wording. Its human-engineered sound-event adaptation set has only 500 audio mixtures across ten events. A single-actor expressive set contains 10,000 pairs, about 25.2 hours.

**Evidence.** Large-scale pretraining improves the downstream baselines. For general CapTTS, NAR style accuracy is 66.0% with pretraining versus 46.4% without. However, in CapTTS-SE, NAR WER is 3.0% while intelligibility MOS, incorporating event quality in that task, is only 3.33±0.15; AR WER is worse at 7.7% but IMOS is 3.45±0.14. The authors explicitly identify lower event quality despite good speech WER. A 500-example machine-tag audit reports expressive-tone correctness 0.863, lower than several basic attributes. Filtering pretraining audio at SNR ≥20 dB also limits the ecological coverage we need.

**Cost and limits.** Reported pretraining is 24 days for AR or ten days for NAR on eight H100s; even the duration predictor costs roughly 70 A100 hours. None is a T4 recipe. Released resources are described under CC BY-NC 4.0; eligibility and individual source terms still need checking before use. All current benchmark languages are English. Ten event categories in the small adaptation set and a single expressive actor do not establish compositional event coverage or multi-speaker diversity. Event markers are prior art, not our novelty.

**Rime change.** Use pretrained Indic speech rather than reproducing CapSpeech. Separate native CER, audible event identity, event placement, naturalness and identity checks. Allow internal event markers on an auxiliary control path while preserving the supplied linguistic text. Give vocal events the same identity as the speaker. Preserve noisy/reverberant real data for the captioner's ecology coverage instead of applying a universal clean-audio cutoff.

## 10. Self-Consuming Generative Models Go MAD — filtering can erase diversity

[Paper](https://arxiv.org/abs/2307.01850). Locators: §§2–5 loop definitions/experiments, §6 discussion; main text through PDF p.16.

**Question and method.** The paper separates fully synthetic training, augmentation with a fixed real dataset, and training with fresh real data. A sampling-bias parameter trades quality for coverage. It analyzes finite-sample Gaussian recursion and studies image generators, including DDPM on MNIST and StyleGAN2 on FFHQ. The theoretical analysis is distribution/model-specific; the image experiments are not a theorem about every speech learning loop.

**Evidence.** Under repeated Gaussian refitting, finite-sample estimation produces mean drift and variance collapse, even without deliberate sampling bias. In the image experiments, biased sampling can sustain precision while reducing recall more quickly. Importantly, augmentation setups differ: the StyleGAN experiment accumulates all prior synthetic samples while keeping 70K real images, whereas the MNIST setup uses fixed-size real and synthetic pools. Fresh-data simulations show regimes where moderate synthetic support helps and excessive biased support hurts. Their admissible mixture threshold is not a universal constant.

**Limits.** Most experiments train successive generators from scratch over many generations. Our proposed one-round transfer from G to a captioner, with warm-start adapters, independent claim checks and fixed compute, is different. It is unjustified to predict inevitable captioner collapse or derive a mandatory replay fraction from this work. The acquired but not deeply read SIMS paper is also a lead on different synthetic-data use; its title/abstract alone is not sufficient evidence for adopting that method.

**Rime change.** Track diversity before and after verification, not only average accepted quality. Cap reuse per speaker/prompt and report rejected regions. Compare real-only replay, random verified synthesis and targeted verified synthesis at equal compute. Reserve fresh eligible real training clips separately from audit clips; never recycle the audit into training. Stop additional rounds when real native coverage or diversity regresses.

## Six acquired leads, not completed detailed reviews

| ID | Publication | Why acquired / remaining work |
|---|---|---|
| [2502.07243](https://arxiv.org/abs/2502.07243) | Vevo | Self-supervised content/style/timbre factorization; verify reference requirements, multilingual transfer and actual adapter feasibility. |
| [2301.13662](https://arxiv.org/abs/2301.13662) | InstructTTS | Natural-language style and mutual-information separation; inspect ablations rather than infer independence from its objective. |
| [2408.15676](https://arxiv.org/abs/2408.15676) | VoxInstruct | Instruction/content integration; compare with the PS's separate transcript and description inputs. |
| [2312.10381](https://arxiv.org/abs/2312.10381) | SECap | Emotion captioning; inspect transfer, label construction and false-assertion evaluation. |
| [2101.02703](https://arxiv.org/abs/2101.02703) | Distribution-Free, Risk-Controlling Prediction Sets | Alternative high-probability risk framework; do not conflate its guarantee with base CRC. |
| [2408.16333](https://arxiv.org/abs/2408.16333) | Self-Improving Diffusion Models with Synthetic Data | Counterpoint to generic collapse claims; inspect negative guidance and applicability to a discriminative captioner. |

These sources remain useful follow-up candidates, but no architecture change here depends on claiming that their full methods were reviewed.
