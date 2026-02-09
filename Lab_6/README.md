Lab 5: The Architecture of Bias
Overview
An investigation into the Data Generating Process (DGP) and systematic biases that compromise machine learning models before a single line of modeling code is written. This project demonstrates that sampling methodology—not model choice—is often the primary determinant of predictive validity.
Objective
To identify, measure, and mitigate three categories of sampling bias that corrupt training data: random sampling error, covariate shift, and sample ratio mismatch (SRM).
Tech Stack

Python - Core programming language
pandas - Data manipulation and analysis
numpy - Numerical computing and random sampling
scipy - Statistical hypothesis testing (Chi-Square)
sklearn - Stratified sampling implementation

Methodology
1. Simple Random Sampling Simulation
Manually implemented random train/test splits on the Titanic dataset to expose the inherent variance of uncontrolled sampling:

Used np.random.permutation() to shuffle indices
Split data 80/20 without controlling for confounding variables
Calculated delta (difference in survival rates between train/test sets)
Result: Demonstrated that random chance alone can produce non-representative samples with biased outcome distributions

2. Stratified Sampling Implementation
Eliminated covariate shift by forcing identical distributions of passenger class across train/test splits:

Implemented sklearn.model_selection.train_test_split() with stratification on pclass
Verified identical proportions using .value_counts(normalize=True)
Result: Reduced sampling bias by ensuring critical confounding variables (socioeconomic class) were equally represented in both sets

3. Sample Ratio Mismatch (SRM) Forensic Audit
Conducted statistical quality control on A/B test infrastructure:

Simulated a broken randomization system (450/550 split instead of expected 500/500)
Applied Chi-Square goodness-of-fit test to detect systematic assignment failures
Established p < 0.01 threshold for identifying engineering bugs vs. natural variance
Result: Demonstrated that 100-user deviations represent ~3 standard deviations from expected distribution, indicating infrastructure failure rather than random chance

Key Findings
Sampling Error ≠ Model Error: A model trained on biased samples will produce systematically wrong predictions regardless of algorithmic sophistication. The delta observed in uncontrolled splits represents a pre-modeling failure in data collection methodology.
SRM as Engineering Canary: When observed sample ratios deviate significantly from expected ratios (p < 0.01), the root cause is almost always infrastructure failure (load balancers, cookie assignment, timestamp-based routing) rather than statistical noise.

Theoretical Extension: Survivorship Bias in Unicorn Analysis
The Problem
Analyzing only successful unicorn startups featured on platforms like TechCrunch creates survivorship bias—a systematic exclusion of failed ventures from the observable sample. This violates the fundamental assumption of random sampling: that your dataset represents an unbiased draw from the true population.
What's missing? The selection mechanism itself is non-random. Companies appear on TechCrunch because they succeeded, creating a dataset where P(observed | success) = 1, but P(observed | failure) ≈ 0.
The Ghost Data
To correct for survivorship bias using a Heckman Selection Model, you would need data on:

The Failed Population: Complete records of startups that received initial funding but never achieved unicorn status—including:

Funding amounts and sources
Founding team characteristics
Market sector and timing
Operational metrics before failure/stagnation


The Selection Indicator: A binary variable encoding whether each startup would have been covered by TechCrunch if it had succeeded. This requires:

Pre-success characteristics that predict media coverage (team pedigree, investor networks, geographic location)
Evidence of selection mechanism independence from success factors


The Exclusion Restriction: At least one variable that affects probability of observation (media coverage) but not probability of success (unicorn status). Example candidates:

PR budget allocation
Founder's social media following
Geographic proximity to major tech news outlets



The Heckman Two-Stage Process
Stage 1 (Selection Equation): Model P(observed in dataset) using all startups (both successful and failed):
P(TechCrunch coverage) = f(PR_budget, founder_network, geography, ...)
Stage 2 (Outcome Equation): Model P(unicorn status) using only observed startups, correcting for selection bias with the inverse Mills ratio (λ) from Stage 1:
P(unicorn) = f(product_quality, market_timing, team_experience, ... , λ)
The λ term captures the correlation between unobserved factors that affect both selection and outcomes, allowing you to estimate what unicorn success factors would look like in an unbiased sample.
Why This Matters
Without the failed population data, any analysis of unicorn characteristics is fundamentally conditional on survival. You're measuring "what distinguishes successful companies among those we happened to observe" rather than "what distinguishes successful companies in the true population of all ventures."
The ghost data—the graveyard of failed startups—contains the counterfactual evidence necessary to separate genuine success factors from spurious correlations with visibility.

Deliverables

Simulation code demonstrating sampling variance in uncontrolled splits
Stratified sampling implementation with distribution verification
Chi-Square SRM diagnostic tool for A/B test quality control
Theoretical framework for correcting survivorship bias in venture analysis
