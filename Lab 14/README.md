# AI Capex Diagnostic Modeling

## Objective
Audit the structural integrity of an Ordinary Least Squares regression model predicting AI Software Revenue from 2026 Nvidia capital expenditure and deployment data by formally diagnosing Gauss-Markov violations and applying heteroscedasticity-consistent corrections to restore inferential validity.

---

## Methodology

- **Baseline Model Construction:** Estimated a naive OLS model regressing AI Software Revenue on Hardware Capex, Data Center Power (MW), and Cloud GPU Deployments using `statsmodels`, establishing a deceptive baseline of high R² and artificially low p-values.

- **Visual Residual Forensics:** Plotted residuals against fitted values via `matplotlib` and `seaborn` to detect non-constant error variance, revealing a pronounced cone-shaped dispersion pattern expanding at high capital expenditure tiers — a hallmark of heteroscedasticity.

- **White Test (Formal Hypothesis Test):** Executed the White Test for heteroscedasticity against the model's design matrix to statistically confirm that error variance is a systematic function of the predictors, rejecting the null of homoscedasticity.

- **Multicollinearity Diagnostics (VIF):** Computed Variance Inflation Factors for all predictors by iterating over the design matrix (excluding the intercept column to prevent metric inflation), quantifying the degree of linear dependence among the capital expenditure regressors.

- **HC3 Robust Standard Error Correction:** Re-estimated the model using MacKinnon-White HC3 heteroscedasticity-consistent covariance matrix estimation, replacing the OLS variance-covariance assumptions with ones robust to arbitrary patterns of non-constant error variance.

**Tools & Libraries:** Python · pandas · statsmodels · matplotlib · seaborn

---

## Key Findings

The naive OLS model exhibited severe heteroscedasticity concentrated at elevated capital expenditure levels, where error variance scaled proportionally with predicted revenue — a structural pattern consistent with the stochastic nature of high-stakes AI infrastructure deployment. This violated the Gauss-Markov assumption of homoscedastic errors, causing the model to systematically underestimate standard errors and generate false statistical confidence across deployment metric coefficients.

Upon applying HC3 Robust Standard Errors, standard errors widened materially, and previously statistically significant predictors lost significance at conventional thresholds. This "p-value shock" does not reflect model degradation — it reflects the *removal* of inferential distortion. The corrected model represents a conservative and defensible estimate of true coefficient precision, appropriate for policy-relevant capital allocation analysis in high-dimensional, stochastic technology sector environments.

Multicollinearity diagnostics further revealed structural redundancy among hardware and infrastructure regressors, consistent with the high co-movement of capital expenditure categories in large-scale AI buildout cycles. These findings collectively underscore the inadequacy of naive OLS for inference in modern technology sector data and validate the necessity of robust estimation procedures.
