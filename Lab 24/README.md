# Causal ML — Double Machine Learning for 401(k) Policy Evaluation

## Objective
Apply Double Machine Learning (DML) to estimate the causal effect of 401(k) retirement plan eligibility on net financial assets, using the Chernozhukov & Hansen dataset to demonstrate why naïve ML fails for causal inference and how cross-fitted residualization solves it.

## Methodology
- Demonstrated regularization bias by applying LASSO directly to a simulated DGP (TRUE_ATE = 5.0), showing the coefficient is systematically shrunk toward zero
- Configured a DoubleML Partially Linear Regression (PLR) model with Random Forest nuisance learners (200 trees, max depth 5) and 5-fold cross-fitting on 9,915 observations
- Residualized both outcome (net_tfa) and treatment (e401) on 11 confounders including age, income, education, family size, and homeownership
- Estimated Conditional Average Treatment Effects (CATE) by splitting the sample into income quartiles and fitting separate DML models per subgroup
- Conducted sensitivity analysis to assess robustness of the ATE to potential unmeasured confounders (e.g., financial literacy)

## Key Findings
- **Full-sample ATE: $8,380** (SE = $417) — 401(k) eligibility significantly increases net financial assets, controlling for all observed confounders
- **Treatment effects rise sharply with income:** Q1 ($3,799), Q2 ($2,958), Q3 ($6,754), Q4 ($15,478) — higher-income households have far greater capacity to contribute and benefit from tax-deferred compounding
- **Robustness Value = 0.195** — an unmeasured confounder would need to explain over 19.5% of residual variance in both eligibility and assets simultaneously to nullify the estimate, indicating a credible and robust causal finding
- Results are consistent with the published literature and suggest means-tested policy designs may need to account for differential take-up capacity across the income distribution
