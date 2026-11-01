# Scene generation and rendering support

These papers inform the recording/ecology axis and compositional requests. Their general-sound or guitar results are supporting evidence, not direct Hindi/Tamil speech results.

## 2305.01980 — Diverse and Vivid Sound Generation from Text

[Source](https://arxiv.org/abs/2305.01980). Read: spectrogram codebook/objectives, text conditioning in an extra range, metrics, human ratings and conclusion.

**Method and evidence.** A text-conditioned Transformer predicts VQGAN spectrogram codes, then MelGAN renders waveform audio. Compare text encoders and global versus sequence features on AudioCaps/Clotho. CLAP-conditioned human relevance averages 6.79/10 versus BERT 5.50; quality changes much less, 6.13 versus 6.08. Generated captions are used as one relevance proxy. The conclusion explicitly leaves chronological order and duration for further work.

**Limits and decision.** A stronger text embedding or good FID cannot guarantee requested event sequence, exact placement or linguistic text. Thirty-token descriptions and general sound generation do not meet the PS interface by themselves. Retain native TTS for content and generate/retrieve only scene components with a common clock. Check event identity, activity, ordering and masking after composition. Do not use caption-generator agreement as the only evidence that the requested sound actually occurred.

## 2309.08051 — Retrieval-Augmented Text-to-Audio Generation

[Source](https://arxiv.org/abs/2309.08051). Read: retrieval encoders, conditioned diffusion, retrieval protocol, tail-class results and ablations.

**Method and evidence.** Add retrieved text/audio features to an AudioLDM-style generator. On the reported AudioCaps setup, the small model's FAD changes from 2.31 without retrieval to 1.48 with three text/audio neighbors; audio-only retrieval reaches 1.95. Returns flatten near five-to-ten neighbors. Tail-category CLAP consistency is more stable than compared baselines, while larger models add cost for modest aggregate gains.

**Limits and decision.** Retrieval access and duplicate/lineage control matter beyond excluding the exact target file. The model works at 16 kHz and evaluates broad sound relevance, not native speech or precise temporal clauses. Use an eligible source-indexed background library as a low-cost option for rare scene components, with bounded retrieval and explicit dry/wet status. Keep scene assets distinct from identity references, prevent contributed-test retrieval, and independently verify event realization instead of relying on the same retrieval similarity model.

## 2309.08773 — Representation Similarity Regularization for Audio Generation

[Source](https://arxiv.org/abs/2309.08773). Read: conditional/unconditional objectives, extra range covering relational loss, pooling/CFG ablations and results.

**Method and evidence.** Match pairwise audio-representation similarities to pairwise text similarities during classifier-free/unconditional training, rather than directly maximizing one audio-text cosine. On the sound-effects model, FAD changes from 1.52 to 1.43 and CLAP from 0.30 to 0.31. Max pooling works better than mean pooling; applying the regularizer in ordinary conditioned steps fails to improve the reported metrics. Training uses 16/32 GPUs and thousands of sound/music hours.

**Limits and decision.** Global pooled similarity still misses negation, count and timing. Small metric gains do not justify reproducing this training recipe on L4s. Keep relational or contrastive losses optional and test single-claim hard negatives against actual realization. Avoid making a global CLAP reward the primary generator objective, especially because description-specific differences can be much smaller than between-example semantic differences.

## 2406.00294 — CTAG: Synthesizer Programming

[Source](https://arxiv.org/abs/2406.00294). Read: synthesizer architecture/search, evaluation design, classifier/human results, optimization and explicit limitations.

**Method and evidence.** Search 78 synthesizer parameters using gradient-free optimization and CLAP similarity; simpler/more complex synthesizers are compared. A small human study finds 56.0% sound identification versus AudioGen 59.5% and AudioLDM 34.0%, with CTAG perceived as more artistic. Signals are rendered at 48 kHz. The authors distinguish acoustic descriptors from validated perceptual-quality measures.

**Limits and decision.** Per-prompt iterative optimization is costly, and short abstract non-mixture sounds are not natural voices or full scenes. High sample rate does not establish realism. Programmatic oscillators/noise/envelopes can supply simple whistles, hums or fantastical textures with known controls; do not reproduce open-ended search for every output. Cache reusable sound recipes, measure rendered audibility/timing, and reserve a pretrained eligible sound branch for requests whose acoustic complexity exceeds these primitives.

## 2411.14972 — Open-Amp

[Source](https://arxiv.org/abs/2411.14972). Read: online effect rendering, contrastive encoder protocol, one-to-many model and unseen-device enrollment.

**Method and evidence.** Render chosen inputs through crowdsourced neural guitar effect models, enabling independent variation of source and device. Experiments use 59 amplifier and 101 pedal captures; parameterized variants give 394 synthetic devices. A shared FiLM-conditioned model learns device embeddings, and frozen-model embedding enrollment can work with little unseen-device data. Dedicated one-to-one models still perform better in the displayed test losses.

**Limits and decision.** Guitar effects do not validate telephone/microphone processing of speech, and model/capture terms differ. The transferable lesson is renderer-factor control and held-out effect families, not importing every distortion model. Build speech-appropriate channel transformations with exact source/parameter provenance and test on real unseen channels. Separate device identity from speech identity and train on multiple voices per effect, so a captioner learns audible processing rather than memorizing a particular source or generator fingerprint.
