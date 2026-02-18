# Hypothesis Testing & Causal Evidence Architecture
### *The Epistemology of Falsification: Statistical Adjudication on the Lalonde Dataset*

---

## Objective

Most applied ML workflows optimize for estimation — minimizing loss, maximizing AUC, shipping a number. This project pivots from that paradigm to ask a harder question: **can we actually trust the signal?**

Using the Lalonde (1986) experimental dataset — a canonical benchmark in causal inference — I operationalized the scientific method as a formal adjudication framework. The goal was not to predict outcomes, but to rigorously test whether a job training intervention produced a *real, attributable* lift in earnings, or whether the observed difference was statistical noise masquerading as causality.

---

## Technical Approach

- **Average Treatment Effect (ATE) Estimation via Signal-to-Noise Decomposition:** Framed the core inference problem as a ratio — the observed difference in group means (signal) over the pooled standard error (noise) — using **Welch's T-Test** (`scipy.stats.ttest_ind`, `equal_var=False`) to account for unequal variance between treatment and control groups without assuming homoscedasticity.

- **Non-Parametric Validation via Permutation Testing:** Real earnings distributions are heavy-tailed and frequently violate the normality assumptions that parametric tests rely on. To stress-test the T-test result, I ran a **Permutation Test** (`scipy.stats.permutation_test`, 10,000 resamples) which constructs an empirical null distribution by repeatedly shuffling treatment labels. Convergence between both p-values confirms the result is distribution-agnostic.

- **Type I Error Control:** All tests were evaluated against a pre-specified significance threshold of α = 0.05. By anchoring inference to a fixed decision rule before observing results, the analysis guards against post-hoc threshold manipulation — a key discipline in avoiding false positives.

- **Counterfactual Visualization:** KDE plots of the treated and control earnings distributions make the causal "shift" interpretable, grounding the statistical result in an economic narrative.

---

## Key Findings

| Metric | Value |
|---|---|
| Mean Earnings – Treated | ~$6,349 |
| Mean Earnings – Control | ~$4,555 |
| Treatment Effect (ATE) | **+$1,795** |
| T-Test p-value | < 0.05 |
| Permutation p-value | < 0.05 |
| Decision | **Reject H₀** |

The Null Hypothesis — that job training has no effect on real earnings — is rejected via *Proof by Statistical Contradiction*. Both parametric and non-parametric methods converge on the same conclusion, substantially strengthening the evidentiary claim.

---

## Business Insight: Hypothesis Testing as the Safety Valve of the Algorithmic Economy

In production data environments, the path of least resistance is to find a pattern and ship it. With enough features, enough slices, and enough model iterations, *something* will always look significant. This is the core failure mode of modern data science: **data dredging**, where spurious correlations get laundered into business decisions because no one asked whether the signal could have occurred by chance.

Rigorous hypothesis testing is the safety valve that prevents this. By forcing analysts to:

1. **Pre-specify a Null Hypothesis** before looking at outcomes,
2. **Commit to a significance threshold** before running tests, and
3. **Validate parametric assumptions** with non-parametric methods,

...we introduce epistemic accountability into the pipeline. The result isn't just a better number — it's a defensible claim. In domains where algorithmic decisions affect hiring, lending, pricing, or resource allocation, the difference between a real effect and a spurious one isn't academic. It's liability.

The Lalonde dataset earns its "Hello World of causal inference" reputation precisely because it was *randomized* — the gold standard that makes the causal arrow unambiguous. Most production data isn't this clean. That's exactly why the falsification mindset, built here in a controlled setting, matters at scale.

---

*Stack: Python · Pandas · NumPy · SciPy · Seaborn · Matplotlib*
