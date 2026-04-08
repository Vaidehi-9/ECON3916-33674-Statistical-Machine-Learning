Tree-Based Models — Random Forests
Objective
Evaluate the predictive gains of ensemble tree methods over linear baselines on the California Housing dataset, quantify feature-level drivers of home prices using two importance paradigms, and extend the framework to binary classification.

Data

Source: California Housing dataset (sklearn)
Observations: 20,640 → 16,512 train / 4,128 test (80/20 split)
Features: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
Targets: Median house value (regression); above/below median price (classification)


Methodology

Model comparison: Benchmarked an unrestricted Decision Tree, Ridge Regression (α = 1.0), and a 100-tree Random Forest on RMSE and R² across train/test splits to characterise the bias-variance profile of each approach
Hyperparameter tuning: Conducted an exhaustive grid search (GridSearchCV, 5-fold CV) over n_estimators ∈ {50, 100, 200}, max_depth ∈ {10, 20, None}, and max_features ∈ {sqrt, 0.5, None}, optimising for negative MSE
Feature importance: Compared Mean Decrease in Impurity (MDI) against permutation importance on the held-out test set to assess stability and potential bias toward high-cardinality features
Classification extension: Binarised the target at the median price threshold and evaluated a 200-tree RF classifier against Logistic Regression using ROC-AUC


Key Findings
ModelTest RMSETest R²Single Decision Tree0.70370.6221Ridge Regression0.74550.5759Random Forest (default)0.50530.8051Random Forest (tuned)[your value][your value]

The unrestricted Decision Tree achieved a perfect training R² (1.000) but generalised poorly, confirming high-variance overfitting in the absence of regularisation
The Random Forest reduced test RMSE by ~28% relative to Ridge, indicating substantial non-linearity in the feature–price relationship that linear models cannot recover
MedInc ranked as the dominant predictor under both importance methods; MDI inflated the apparent importance of Latitude and Longitude relative to permutation estimates, consistent with known bias toward continuous high-cardinality features
On the classification task, the RF classifier achieved AUC ≈ 0.92–0.93 vs. ≈ 0.87–0.88 for Logistic Regression — a practically meaningful gap attributable to the model's capacity to capture interaction effects


Causal caveat: MedInc is the strongest predictive feature, but feature importance does not imply causality. Confounding via neighbourhood-level socioeconomic factors precludes any direct causal interpretation without experimental or instrumental-variable identification.


Tools & Libraries
scikit-learn · pandas · numpy · matplotlib · plotly · ipywidgets
