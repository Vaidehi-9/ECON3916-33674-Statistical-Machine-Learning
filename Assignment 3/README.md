# Econ 3916 – Assignment 3: Causal Inference & Non-Parametric Analysis
### SwiftCart Logistics | Senior Data Economist Report

---

## Overview

This notebook investigates three core business problems at SwiftCart Logistics using heavy computation and non-parametric statistical methods. All parametric assumptions (normality, homoscedasticity) are deliberately discarded in favor of empirically-driven inference engines built from scratch using native NumPy and Scikit-Learn.

---

## Environment

- **Platform:** Google Colab
- **Notebook Title:** `Econ_3916_Assignment_3_Causal`

### Dependencies
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
```

---

## Dataset

| File | Description |
|---|---|
| `swiftcart_loyalty.csv` | Contains pre-treatment covariates (order volume, account age, support tickets) and post-treatment spending for 1,000 users. Treatment column `D=1` indicates SwiftPass subscriber. |

---

## Structure

### Phase 1 – Bootstrapping Non-Parametric Uncertainty

**Problem:** Driver tip data is zero-inflated and right-skewed, making the Central Limit Theorem unreliable for small sample audits.

**Method:**
- Simulated 250 driver tips: 100 zero-tips + 150 draws from Exponential(scale=5.0)
- Built a manual bootstrap engine with 10,000 resamples using `np.random.randint`
- Extracted 95% Confidence Interval via `np.percentile` at the 2.5th and 97.5th percentiles

**Key Finding:** The bootstrapped CI is asymmetric — the upper bound stretches further than the lower bound — because the underlying tip distribution is skewed. A standard parametric CI would falsely assume symmetry.

**Strict Prohibition:** `scipy.stats.bootstrap` was not used. The resampling loop was written manually.

---

### Phase 2 – Permutation Test (Batch Routing Algorithm A/B Test)

**Problem:** The engineering team claims their new batch routing algorithm reduces delivery times. However, software crash loops introduce extreme outliers in the treatment group, invalidating the homoscedasticity assumption of a standard T-test.

**Method:**
- Generated 500 Control deliveries from Normal(mean=35, sd=5)
- Generated 500 Treatment deliveries from LogNormal(mean=3.4, sigma=0.4)
- Built a manual permutation engine: concatenated all 1,000 deliveries, shuffled and re-split 5,000 times using `np.random.permutation`
- Calculated empirical two-tailed p-value as the proportion of permutations producing a difference as extreme as observed

**Key Finding:** The empirical p-value determines whether the algorithm's effect is real or attributable to random chance — without ever assuming a distribution shape.

**Strict Prohibition:** `scipy.stats.permutation_test` was not used. The permutation loop was written manually.

---

### Phase 3 – Propensity Score Matching (SwiftPass ROI)

**Problem:** The marketing team claims SwiftPass subscribers spend 300% more, and is requesting a doubled acquisition budget. This figure is contaminated by severe selection bias — high-volume power users self-select into the program to save on fees.

**Method:**
1. Calculated the Naive Simple Difference in Means (SDO): **$17.57**
2. Used `LogisticRegression` to predict each user's probability of subscribing based on pre-treatment covariates (propensity score)
3. Used `NearestNeighbors(n_neighbors=1)` to match each subscriber to the most similar non-subscriber
4. Calculated the Average Treatment Effect on the Treated (ATT) using only the matched control group: **$10.02**

**Key Finding:** The SDO overstates the true effect by **$7.55 (43%)**, which is pure selection bias. The marketing team's budget request is statistically unsound and should be scaled to reflect the true causal ATT of $10.02.

---

### Phase 4 – Love Plot (LLM-Assisted Visualization)

**Method:** Used the P.R.I.M.E. framework to prompt an LLM to generate a Love Plot (Standardized Mean Differences) visualizing covariate balance before and after PSM.

**How to Read the Plot:**
- Red dots = SMD before matching (groups were different)
- Blue dots = SMD after matching (groups are balanced)
- Green line = SMD threshold of 0.1 (standard academic benchmark)
- All blue dots falling left of 0.1 = selection bias successfully mitigated

---

## Key Results Summary

| Analysis | Raw Estimate | Causal Estimate | Bias Detected |
|---|---|---|---|
| Driver Tip Median CI | Symmetric parametric CI | Asymmetric bootstrap CI | Yes — skew ignored by CLT |
| Routing Algorithm p-value | T-test invalid | Empirical permutation p-value | Yes — outliers violated homoscedasticity |
| SwiftPass Spending Effect | SDO = $17.57 | ATT = $10.02 | Yes — $7.55 (43%) was selection bias |

---

## Academic Integrity Note

Per the **Foundations First Academic Protocol:**
- `scipy.stats.bootstrap` — **NOT USED**
- `scipy.stats.permutation_test` — **NOT USED**
- Generative AI — authorized **exclusively for Phase 4** Love Plot visualization
