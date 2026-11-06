# Mid-term report skeleton (≤ 6 pages + references) — fill numbers from results.csv

## 1. Problem framing and prior work (≈ 1.3 pages)
**Gap.**
(i) Description-conditioned TTS data recipes (Parler-TTS/DataSpeech, ParaSpeechCaps, SpeechCraft, CapSpeech) use
coarse tag bins without timing.
(ii) Free-text captioners (Qwen3-Omni-Captioner, Audio Flamingo 3, Omni-Captioner) hallucinate more as captions
get longer, and they are not tuned to avoid errors.
(iii) Loops that train two models on each other's outputs assume pseudo-label noise does not compound:
Machine Speech Chain, back-translation, ReST/STaR. With free-text descriptions it does compound, and model
collapse follows when real data is replaced.
(iv) Hindi/Tamil ecology (phone channels, domestic soundscapes) and dialect are absent from all of the above.

**Hypotheses.**
- **H1 (lead).** Restricting loop training data to claims that are measured, constructed, or agreed by
  independent sources makes the rubric score on held-out real audio rise each round, and lowers false-claim
  weight, compared with an unverified loop at equal compute.
- **H2.** Evidence grounding plus calibrated commitment beats the raw 30B captioner even with fewer claims.
- **H3.** A factorised generator (voice model plus programmable ecology, driven by a timed plan) raises
  relevance on timed and recording items without hurting naturalness.

**Why it should work.** 10 of the 13 rubric item types have acoustic correlates we can measure (table: item
type → tool → confidence). The rubric's penalty makes precision worth more than recall.

## 2. Method (≈ 1.5 pages)
- Scene Score (claim = item type, span, $\hat p$, source, value).
- Captioner: evidence → K-sample Omni → atomic claims → self-consistency → fusion rules → isotonic calibration.
  Commitment rule:
  $$\text{state } c \iff \hat p_c > \tau=\frac{q\,w'}{h\,w+q\,w'}$$
  - Knapsack under 300 words: $\max \sum_c \hat p_c w_c$ s.t. $\sum_c \ell_c \le 300$.
- Generator:
  - planner → RenderPlan;
  - speaker prior via farthest-point sampling, $z_{k+1}=\arg\max_z \min_j (1-\cos(z,z_j))$ s.t.
    $\cos<\theta_{SV}$;
  - voice model;
  - WSOLA timing;
  - ecology renderer with labels re-measured from the output.
- Loop: verified pseudo-labels → generator SFT/DPO → weak-area budget
  $n_k = N\,\bar w_k(1-F_k)/\sum_j \bar w_j(1-F_j)$ → captioner LoRA + DPO with injected false claims.

## 3. Baselines and evaluation setup (≈ 1 page)
- Round 0: the suggested pair (exact recipe and hashes). Reference rows: Indic-Parler-TTS, Qwen3-TTS VoiceDesign.
- DevReal rubric: annotation protocol, κ between annotators, κ between grader and humans.
- Generation measures:
  - CER: IndicConformer RNNT plus our Indic normaliser.
  - Diversity: WavLM-SV at 0.86 and ECAPA at 0.25.
  - Relevance proxy: validated on a human subset.
  - Naturalness proxies: relative comparisons only.
- Bootstrap: PS Appendix-A hashing, 1,000 replicates; paired deltas.

## 4. Early results (≈ 1.4 pages)
- Table 1: captioner raw / evidence / fused, rubric score [CI], false-claim weight, per language.
- Table 2: score by item type and axis (failure analysis), with examples of hallucinations removed and of
  claims missed.
- Table 3: generator rows (CER, distinct speakers, relevance proxy, UTMOS) for round0, parler, design, factored.
- E2 codec ceiling; E6 renderer exactness.
- Figure: Pareto frontier of score vs. active params and GPU-hours, with the compute ledger total per round.

## 5. Revised plan (≈ 0.6 page)
- Decision gates and their outcomes (backbone, τ per type, grader).
- Remaining rounds: round 1 = verified pseudo-labels + language-adapted generator; round 2 = DPO both sides.
- Stopping rule: stop when the paired Δ on held-out real audio is below its CI.
- Risks: synthetic-to-real gap, grader mismatch, Tamil data scarcity (24 h of Vaani transcripts) → mitigations.
