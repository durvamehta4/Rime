# Adapter efficiency under the actual L4 budget

These language/vision experiments are transfer evidence. None benchmarks the proposed Hindi/Tamil audio pipeline on L4.

## 2402.09353 — DoRA

[Source](https://arxiv.org/abs/2402.09353). Read: magnitude/direction decomposition, task settings, selective-module tuning and quantized results.

**Method and evidence.** Learn a magnitude vector and a low-rank change to normalized weight direction, initialized from pretrained weights. Selected attention-direction plus MLP-magnitude adaptation improves the shown reasoning results while using fewer trainable parameters than the compared LoRA configuration. QDoRA can improve the displayed math accuracy, and the update can be merged for inference. The conclusion explicitly leaves audio generalization to future work.

**Limits and decision.** Mergeable inference does not imply free training: normalization, kernels, activations and quantization compatibility matter. These results do not warrant replacing every baseline adapter. Start with conventional four-bit LoRA on the caption LM and native-generator-supported adapters, then compare DoRA at matched examples, wall/GPU time and validation claims if ordinary LoRA plateaus. Keep a rollback checkpoint and measure actual peak memory; more expressive updates may overfit sparse intent labels or reduce pretrained language competence.

## 2310.08659 — LoftQ

[Source](https://arxiv.org/abs/2310.08659). Read: alternating quantization/SVD residual initialization in an extra range, model/task setup, bit-width and initialization analyses.

**Method and evidence.** Jointly approximate a pretrained matrix with a quantized base plus low-rank correction, alternating quantization and residual SVD before adapter training. A single step is a quantization-error correction; extra steps have diminishing returns. The table shows large benefits in some low-bit configurations, but four-bit Llama-2-7B GSM8K is 35.0 versus QLoRA's 35.1, despite improved perplexity. The prose claim of never observing worse performance should therefore be read cautiously.

**Limits and decision.** Weight reconstruction error, text perplexity and acoustic claim accuracy are different endpoints. Original high-precision weights and initialization memory/I/O are needed, and extreme two-bit training is unnecessary risk here. Use LoftQ only if four-bit captioner quantization measurably harms the native pilot and initialization is supported. Record pre/post-quantization behavior and total setup cost instead of assuming a better initialization universally improves speech or saves GPU-hours.

## 2312.03732 — Rank-Stabilized LoRA

[Source](https://arxiv.org/abs/2312.03732). Read: rank-dependent update definition/theory in an extra range, rank sweep, gradient and loss observations.

**Method and evidence.** Replace the conventional rank scaling α/r with α/√r to preserve update/gradient scale as rank grows. Llama-2/OpenOrca experiments sweep ranks from four to 2,048; conventional scaling yields little improvement with larger rank, while stabilized scaling improves training loss and maintains initial gradient scale. Adapters can be merged, avoiding an extra inference branch.

**Limits and decision.** Asymptotic rank analysis and training perplexity do not prove that maximal affordable rank is best on small native claim data. Higher ranks still cost optimizer/activation memory and may overfit. Test only a small rank ladder, with scaling and learning rate logged together, before allocating more capacity. Prefer stabilized scaling as an inexpensive candidate when rank changes; judge it by held-out acoustic facts/CER and time, not by lower training loss or the assumption that parameter count equals useful diversity.

## 2308.03303 — LoRA-FA

[Source](https://arxiv.org/abs/2308.03303). Read: the currently retrieved revision's frozen-factor/gradient-correction derivation in an extra range, task comparisons and A800 memory results; version/hash recorded in the source record.

**Method and evidence.** Freeze the down-projection and optimize the up-projection with a gradient correction, reducing stored activations. In the displayed A800 setup, LoRA-FA uses 52.2 GB while compared methods exceed 80 GB. The paper reports competitive language-task accuracy and identifies activation memory, rather than trainable-parameter count alone, as the bottleneck. The formulation approximates full updates within a fixed low-rank feature subspace.

**Limits and decision.** A fixed column space is not generally exactly equivalent to every jointly learned low-rank update; interpret expressivity claims as approximation under the paper's conditions, not universal equality. A800 timings/kernels and 52.2 GB do not establish 24 GB L4 feasibility. Keep LoRA-FA as a fallback if profiling shows adapter activations dominate. First reduce length/batch, checkpoint activations and freeze the audio encoder; validate specialized optimizer support before promising an activation-memory saving in the selected audio stack.
