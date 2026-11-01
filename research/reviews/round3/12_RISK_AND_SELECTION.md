# Risk, rejection and what guarantees actually mean

Theoretical passages were checked beyond the heuristic packets. Guarantees apply to the chosen loss, calibration units and distribution assumptions, not automatically to the PS score.

## 2306.10193 — Conformal Language Modeling

[Source](https://arxiv.org/abs/2306.10193). Read: sampling/rejection algorithm and admission definition in an extra range, task-dependent label proxies, results and component selection.

**Method and evidence.** Calibrate quality, duplicate-rejection and stopping thresholds so a set contains at least one admissible response with high probability, using Learn then Test. Main experiments cap generation at 20 candidates. Likelihood-aware policies reduce excess samples; in QA the reported set-size AUC for MAX/SUM is less than half the FIRST-K baseline. Admission is task-specific, including extracted radiology labels or ROUGE thresholds, rather than universal truth.

**Limits and decision.** Existence of a correct candidate does not identify which candidate is correct, and returning alternatives is incompatible with the PS's committed prose requirement. Do not import a set-coverage guarantee as final-caption factuality. Study bounded sampling/rejection only in development/training, accounting for every candidate's compute; it cannot justify final generator resampling under the PS's no-selection rule. Independently evaluate the final selected output; a caption set containing one good answer is not a successful single-output submission.

## 2110.01052 — Learn then Test

[Source](https://arxiv.org/abs/2110.01052). Read: null hypotheses, finite-sample p-values and family-wise correction in an extra range, selective/multilabel experiments and marginal-guarantee limitations.

**Method and evidence.** For a fixed discrete family of policies, test each null that its expected loss exceeds a target. Valid p-values plus family-wise error control identify a set of risk-controlling policies; a bounded loss need not be monotonic in the policy parameter. Experiments show fixed-sequence testing can be less conservative than generic uniform bounds, including FDR and selective error tasks. The paper explicitly warns that errors may concentrate in a meaningful subgroup despite marginal control.

**Limits and decision.** Calibration size, independent valid sampling and multiplicity determine whether any useful policy can be certified. Learning new candidates or a test ordering on the same calibration labels invalidates a naive implementation. Add LTT as an optional offline calibration experiment for actual retained-claim FDP, whose denominator makes it nonmonotonic. Freeze candidates/order on tuning data, include empty-policy fallback, and report per-language/type empirical coverage. Keep this distinct from V3's simpler false-count/fixed-budget CRC proxy and from hidden official weighted facts.

## 2310.01262 — Non-Exchangeable Conformal Risk Control

[Source](https://arxiv.org/abs/2310.01262). Read: main bound, weight assumptions and practical selection in an extra range, time-series/QA examples and limits.

**Method and evidence.** Extend bounded monotonic-loss CRC with weighted calibration and an additional total-variation shift term. With data-independent weights the expected test loss is bounded by the target plus a weighted TV penalty. QA experiments use embedding-similarity weights and explicitly relax the fixed-weight assumption; set size decreases from 24.6 to 23.0 at similar observed risk around 0.30. Unknown shift magnitudes remain a practical problem.

**Limits and decision.** Weighting nearby examples does not magically preserve the nominal risk under arbitrary drift: the extra term may be unknown or vacuous, and data-dependent weights need a different conditional analysis. Do not label a heuristic domain-weighted threshold “distribution-free under shift.” Treat channel/language shift as an audit and recalibration problem. Record when no calibration stratum represents a clip, omit unsupported high-specificity claims, and distinguish exploratory weighting from any formal statement about expected risk.

## 1901.09192 — SelectiveNet

[Source](https://arxiv.org/abs/1901.09192). Read: prediction/selection/auxiliary heads, coverage-penalized objective, datasets and coverage recalibration results.

**Method and evidence.** Jointly optimize a predictor and rejector under a target-coverage penalty, with a full-coverage auxiliary task to preserve useful features. Tests on vision classification and regression show improved risk/coverage tradeoffs versus post-hoc confidence rejection. Training at one coverage then calibrating near it works better than large changes; the displayed CIFAR matrix is often best near its diagonal.

**Limits and decision.** An optimization penalty is not finite-sample certified risk, and vision results do not establish audio claim calibration. Rejecting hard examples can also hide low recall on whispers, unusual channels or Tamil. Use coverage-aware claim training only as a bounded ablation and track omissions by PS type. Keep factuality calibration separate from the learned reject head, and evaluate total weighted utility as well as precision so an almost-empty caption is never presented as the best architecture merely because it makes few false claims.
