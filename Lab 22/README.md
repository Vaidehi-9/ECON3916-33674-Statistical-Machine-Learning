# Clustering World Economies with K-Means & PCA
~ Course: ECON 3916 — Data Science for Economists ~

Objective
Applied unsupervised machine learning to classify 237 national economies across 9 World Bank development indicators, revealing latent economic structure that both corroborates and challenges the World Bank's official income-group taxonomy.

Methodology

Sourced 9 World Bank WDI indicators per country via wbgapi, spanning income, health, education, inequality, CO₂ emissions, internet access, trade openness, unemployment, and urbanization
Applied StandardScaler prior to clustering to normalize feature scales — preventing GDP per capita (range: $1,105–$146,919) from dominating Euclidean distance calculations
Fit K-Means (K=4, k-means++ initialization, random_state=42) and projected the 9-dimensional feature space to 2D via PCA for visual inspection of cluster geometry
Evaluated K=2 through K=10 using the elbow method (WCSS/inertia) and mean silhouette score; elbow inflects at K=3–4 with diminishing WCSS returns beyond K=4
Cross-tabulated algorithmic cluster assignments against World Bank income classifications (Low / Lower-Middle / Upper-Middle / High) to assess alignment
Replicated the full pipeline on California Housing census tract data to validate generalizability across domains


Key Findings

K=4 produced four well-differentiated clusters with stark separation across all three headline indicators:

ClusterNAvg GDP/cap (PPP)Avg Life ExpAvg Infant Mortality032$75,52081.1 yrs4.1 per 1,000293$30,80176.1 yrs9.7 per 1,000169$12,25670.0 yrs25.8 per 1,000343$3,68761.6 yrs51.9 per 1,000

High-income (Cluster 0) and low-income (Cluster 3) economies aligned closely with World Bank classifications; the two middle clusters exhibited meaningful overlap between Lower-Middle and Upper-Middle income groups
This divergence is substantively interpretable: countries classified as Upper-Middle by GNI per capita alone may cluster with lower-income peers when health outcomes, internet penetration, and inequality are incorporated — illustrating that single-metric classifications compress genuine multidimensional heterogeneity
PC1 captured the dominant development gradient, with the four clusters well-separated along this axis and moderate overlap along PC2 among middle-income economies — consistent with the inherently fuzzy boundary between development tiers
