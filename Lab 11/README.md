# Data Wrangling & Engineering Pipeline

## Objective
Systematically engineer structural features and impute missing values across a high-entropy HR economics dataset to produce a analytically rigorous, model-ready input for downstream econometric estimation.

---

## Methodology

- **Missingness Diagnostics:** Audited the dataset using `missingno` to map and classify missing data mechanisms, confirming Missing At Random (MAR) structures and informing appropriate imputation strategies.
- **Feature Engineering:** Constructed structural features from raw variables to improve signal quality and reduce noise prior to model fitting.
- **Multicollinearity Mitigation:** Identified and resolved perfect multicollinearity arising from full dummy variable sets by systematically dropping a reference class per categorical variable — a canonical application of the Dummy Variable Trap correction in OLS contexts.
- **High-Cardinality Encoding:** Applied Target Encoding via `category_encoders` to compress high-cardinality geographic variables, replacing sparse nominal levels with continuous posterior estimates of the target mean — preserving information while eliminating dimensionality risk.
- **Pipeline Tooling:** Orchestrated the full wrangling and transformation workflow using `pandas` and `statsmodels`, maintaining reproducibility and modularity throughout.

---

## Key Findings

The pipeline successfully resolved all pre-modeling data quality issues present in `messy_hr_economics.csv`. MAR missingness was correctly identified and handled without introducing bias through listwise deletion. Perfect multicollinearity was eliminated prior to estimation by enforcing reference-class discipline in categorical encoding. Geographic variables with prohibitively high cardinality were compressed into econometrically tractable continuous representations via Target Encoding, retaining predictive information without inflating the design matrix. The resulting dataset is structurally sound and estimation-ready for OLS or comparable linear econometric models.

---

*Stack: Python · pandas · statsmodels · missingno · category_encoders*
