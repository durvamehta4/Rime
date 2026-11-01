# Literature synthesis for Rime Track 2

The current design is [version 3](ARCHITECTURE_V3.md), following [ten additional detailed main-text reviews](reviews/round2/DETAILED_REVIEWS.md). First-pass counts below retain their original scope. The new pass separately records 16 acquired publications, ten reviewed in detail and six unfinished leads, with no overlap in IDs.

## Additional findings from the deeper pass

- **Explicit variation beats assuming decoder noise creates identities.** PromptTTS 2 motivates a learned missing-variation path; ControlSpeech shows why reference identity and style can conflict. Version 3 budgets a small conditioning-interface/prior experiment, with separate identity and delivery tests.
- **Delivery requires suitable evidence.** StyleCap's WavLM features outperform speaker x-vectors on delivery factors. LibriTTS-P separates speaker-level descriptions from utterance-level labels. PENN shows why unreliable voicing can hide behind accurate voiced-frame pitch. These motivate a small windowed delivery path and validity masks.
- **Confidence needs a defined target.** Conformal Risk Control requires a bounded monotone loss and suitable exchangeability. Version 3 freezes proposals and the word budget, then calibrates nested claim removal on a false-claim-count proxy; it does not promise official-score control. ParaCLAP's transfer failures caution against using audio-text similarity as truth.
- **Event quality needs its own evaluation.** CapSpeech reports low WER alongside weaker event intelligibility. Brouhaha distinguishes source-specific acoustics and measurement windows from output frame rates. Version 3 specifies rendering ownership and separate event/audibility/timing checks.
- **Synthetic filtering changes coverage.** The MAD study distinguishes fixed, fresh and fully synthetic loops and sampling bias. Its generator/image results motivate mixture and diversity audits, not a universal collapse claim for this one-round captioner loop.

Methods, reported numbers, caveats and exact transfer decisions are in the new reviews. No training or experimental gains are claimed.

## Scope and evidence

The first pass inspected 296 publication records, retaining 277 relevant works after 19 exclusions. It read abstracts and selected PDF/HTML passages; 28 core sources received additional scoped checks in [CORE_FINDINGS.md](reviews/CORE_FINDINGS.md). This is not 277 exhaustive full-paper readings. The [ledger](paper_ledger.csv) includes exclusions; the [dossier](reviews/PAPER_BY_PAPER.md) exposes the inspected passages. No paper result was independently reproduced.

Searches used arXiv's API, foundational seeds verified against returned metadata, thematic title/abstract screening and core follow-up. False-positive name matches, erroneous seed identifiers and duplicate research lineages were excluded. Fugatto was resolved through its official project PDF. This is a broad engineering review, not a census of every publisher or an exhaustive citation-network search. Recent preprints remain provisional evidence.

| Primary theme | Retained works |
|---|---:|
| Speech/audio generation and control | 95 |
| Captioning and grounding | 60 |
| Evaluation and reliability | 43 |
| Loop learning and data selection | 32 |
| Representations and codecs | 23 |
| Data and Indic speech | 19 |
| Efficiency and adaptation | 5 |
| **Total** | **277** |

These single primary-theme assignments support navigation; themes overlap. Peripheral background is weaker evidence than a task-specific controlled study.

## Findings that change the design

**Start from an Indian description-native generator.** [RASMALAI / IndicParlerTTS](https://arxiv.org/abs/2505.18609) directly matches the generator's transcript-plus-description interface. Its public [checkpoint card](https://huggingface.co/ai4bharat/indic-parler-tts) explicitly lists Hindi/Tamil; API metadata reports approximately 938M parameters, an Apache-2.0 card license and automatically gated access. Compare its pretrained and studio-finetuned releases as G0 candidates before building description adapters into IndicF5. The [F5-TTS paper](https://arxiv.org/abs/2410.06885) itself acknowledges limited fine-grained paralinguistic control. Conversely, [Qwen3-TTS](https://arxiv.org/abs/2601.15621)'s documented languages exclude Hindi/Tamil, so a public baseline suggestion is not proof of language suitability.

**Reciprocal understanding/generation is prior work.** [CycleSpeech](https://arxiv.org/abs/2609.24771) already connects understanding and generation through shared profiles and reciprocal optimization. Its full-system gains include substantial supervised adaptation; incremental reciprocal-stage understanding gains are smaller, and English WER worsens slightly from SFT to CycleGRPO. [UALM](https://arxiv.org/abs/2510.12000) already uses rich captions and generate–understand–critique–refine reasoning. Its large pretraining recipe is outside the 1,000 T4 GPU-hour budget. Adapt specialists and prove a useful verified-data loop before adding reciprocal RL.

**Timed schemas and teacher fusion also have close precedents.** [TAC](https://arxiv.org/abs/2602.15766) combines synthetic mixtures, realized activity labels and timestamp supervision. [TAC2](https://arxiv.org/abs/2610.36568) combines multi-teacher timeline fusion, expressive specialists, distilled descriptions and generation supervision. [Frame-level grounding](https://arxiv.org/abs/2609.15215) supplies external temporal evidence, while [ATTEST](https://arxiv.org/abs/2610.17149) studies counterfactual/attention-grounded temporal rewards. These support the design while narrowing novelty claims. Their benchmark scores do not establish the PS's tolerance on Hindi/Tamil, and a paper does not establish available eligible weights.

**Measure what listeners hear.** [InstructTTSEval](https://arxiv.org/abs/2506.16381) separates acoustic parameters, descriptive style and role-play. The [instruction–perception study](https://arxiv.org/abs/2509.13989) probes degree modifiers and expressive dimensions with measurements and listeners. A plausible requested style is not a valid label for generated audio. [VoiceCraft](https://arxiv.org/abs/2403.16973) also reports disagreement between ASR WER and listener intelligibility. Use CER, similarity metrics and quality predictors as separate diagnostics rather than substitutes for native instruction checks.

**Separate identity from delivery.** [PromptTTS++](https://arxiv.org/abs/2309.08140) discusses sampling versus averaged-voice tradeoffs. Verification studies on [vocal effort](https://arxiv.org/abs/2008.02487) and [speaker overlap](https://arxiv.org/abs/2304.03515) warn against treating every embedding shift as a new speaker. Indic Parler lists only four native Hindi and two native Tamil named voices: ten seeds cannot guarantee ten identities. Compare cross-lingual identity choices and pretrained/fine-tuned priors while monitoring accent and relevance.

**Ecology includes interactions, not just mixing.** [VoiceLDM](https://arxiv.org/abs/2309.13664), [WavJourney](https://arxiv.org/abs/2307.14335) and [Fugatto](https://fugatto.github.io/FUGATTO_ICLR_2025.pdf) precede joint environmental conditioning, compositional planning and instruction-data construction. Known effects supply useful partial labels, but gain is not shouting, pitch shift is not falsetto, and added noise is not a Lombard response. Generic [description-based TTS](https://arxiv.org/abs/2402.01912) reported weak C50 control, whereas RASMALAI reports high binned C50 accuracy. Different models, metrics and distributions make learned versus explicit room control an experiment to run, not a settled answer.

**Keep synthetic learning anchored in real data.** [Synt++](https://arxiv.org/abs/2110.11479), [DUST](https://arxiv.org/abs/2011.13439) and [Synth-AC](https://arxiv.org/abs/2309.09705) precede synthetic-distribution correction, uncertainty filtering and synthetic caption supervision. [Recursion research](https://arxiv.org/abs/2305.17493) motivates real support, but does not prove every real/synthetic mixture must collapse. Verify realized properties, retain real replay, and mask unverified attributes instead of trusting whole synthetic descriptions.

## Recommended research question

Does **calibrated, per-claim verification plus weakness-targeted generation** improve real Hindi/Tamil captioning more efficiently than random verified synthesis, extra real replay or mutual model agreement?

Do not claim schemas, teacher fusion, synthetic transformations, targeting or cycle consistency as individually new. Establish any contribution through precise comparison with the closest prior methods and matched-budget ablations.

The recommendation is [ARCHITECTURE_V3.md](ARCHITECTURE_V3.md). The unresolved evidence is experimental: checkpoint access/compatibility, native quality, timing, T4 throughput, relevant diversity and whether the loop beats its controls. No literature result establishes a guaranteed winning architecture.
