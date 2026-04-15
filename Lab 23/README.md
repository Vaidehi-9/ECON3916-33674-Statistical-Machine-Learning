# FedSpeak Analysis — NLP on FOMC Minutes
 
## Objective
Quantify shifts in Federal Reserve communication style and sentiment across two decades of FOMC meeting minutes using domain-specific NLP techniques, with a focus on detecting language regime changes around major macroeconomic shocks.
 
## Dataset
**FOMC Meeting Minutes** via HuggingFace (`gtfintechlab/fomc_communication`) — 200+ documents spanning 2000–2024, each representing a single Federal Open Market Committee meeting (avg. ~8,000 words of monetary policy deliberation).
 
## Methodology
- **Text Preprocessing** — Lowercased, stripped non-alphabetic characters, tokenized with NLTK, removed English stop words, and lemmatized to normalize inflected forms (e.g., *economies* → *economy*)
- **TF-IDF Vectorization** — Built a document-term matrix using unigrams and bigrams with `min_df=5` and `max_df=0.85` to filter noise and background terms; vocabulary capped at 5,000 features
- **Loughran-McDonald Sentiment Scoring** — Applied the finance-domain LM dictionary to compute per-document net sentiment `(positive − negative) / total` and an uncertainty score `(uncertainty words / total)`, normalized by document length to control for meeting length variation
- **Temporal Visualization** — Plotted sentiment and uncertainty time series with 12-month rolling averages; annotated key events (Lehman collapse, Taper Tantrum, COVID, 2022 tightening cycle)
- **K-Means Clustering** — Reduced TF-IDF matrix to 50 dimensions via Truncated SVD, then fit K=3 clusters to identify distinct language regimes; evaluated with silhouette score and visualized in 2D PCA space
- **Pre/Post-COVID Distributional Comparison** — Split corpus at March 2020 and compared sentiment distributions via overlaid histograms with mean markers
## Key Findings
- **Three language regimes emerged** from clustering: a pre-crisis era of stable, forward-guidance-oriented prose; a crisis/post-crisis period (2008–2015) marked by unconventional policy vocabulary; and a post-COVID tightening cycle dominated by inflation-focused language
- **FOMC minutes are structurally neutral** — mean net sentiment hovers near zero across the full sample, consistent with the Fed's institutional communication norms; the most negative documents cluster tightly around September 2008 and March 2020
- **COVID widened the variance of Fed language more than it shifted the mean** — post-2020 documents show a heavier right tail in net sentiment (recovery optimism in 2021) and elevated uncertainty scores during the 2020 emergency response and 2022–2023 tightening, rather than a clean directional shift
- **Uncertainty spiked at every major inflection point** — the 2013 Taper Tantrum, COVID shock, and 2022 rate liftoff all produced measurable jumps in hedging language, validating uncertainty scoring as a leading indicator of policy regime change
## Tools & Libraries
`Python` · `HuggingFace Datasets` · `NLTK` · `scikit-learn` · `pandas` · `matplotlib`

  
## References
Shah, A., Paturi, S., & Chava, S. (2023). Trillion Dollar Words: A New Financial Dataset, Task & Market Analysis. *ACL 2023.*
 
Loughran, T., & McDonald, B. (2011). When Is a Liability Not a Liability? *Journal of Finance, 66*(1), 35–65.
