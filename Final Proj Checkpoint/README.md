# Predicting Student Math Failure
### ECON 3916: Statistical Machine Learning — Final Project, Spring 2026
**Author:** Vaidehi Pundeer
 
---
 
## Overview
 
This project builds an early-warning classification model to predict whether a secondary school student will fail their final math exam, using only demographic, social, and behavioral information available at the start of the school year — before any grades are issued.
 
**Prediction question:** Can we predict whether a student will score below 10/20 on their final math exam using enrollment-time data alone?
 
**Stakeholder:** School counselors who want to identify at-risk students early enough to offer proactive support.
 
**Models:** Logistic Regression (baseline) vs. Random Forest (200 trees)
 
**Best model:** Random Forest — CV F1 = 0.81 ± 0.03
 
**Live app:** https://econ3916-33674-statistical-machine-learning-pr2nb63lb39rxrbtjg.streamlit.app/
 
---
 
## Repository Structure
 
```
├── econ3916_final.ipynb       # Main analysis notebook (EDA, models, results)
├── app.py                     # Streamlit dashboard
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```
 
Data is loaded directly from a hosted URL inside the notebook and app — no local data file needed.
 
---
 
## Reproducing the Analysis
 
### 1. Clone the repository
 
```bash
git clone https://github.com/Vaidehi-9/econ3916-33674-statistical-machine-learning.git
cd econ3916-33674-statistical-machine-learning
```
 
### 2. Set up the environment
 
Python 3.10+ recommended. Install dependencies:
 
```bash
pip install -r requirements.txt
```
 
Or create a virtual environment first:
 
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```
 
### 3. Run the notebook
 
Open `econ3916_final.ipynb` in Jupyter or Google Colab and run all cells top to bottom.
 
**In Colab:**
1. Go to https://colab.research.google.com
2. File → Open notebook → GitHub → paste the repo URL
3. Runtime → Run all
No local data download is needed. The notebook loads the dataset directly from:
```
https://quantdev.ssri.psu.edu/sites/qdev/files/student-mat.csv
```
(Mirror of UCI Student Performance Dataset — original DOI: https://doi.org/10.24432/C5TG7T)
 
### 4. Run the Streamlit app locally
 
```bash
streamlit run app.py
```
 
The app will open at `http://localhost:8501`. Use the sidebar sliders to input a student profile and view the predicted pass probability with confidence interval.
 
---
 
## Dataset
 
- **Name:** UCI Student Performance Dataset (Math subset)
- **Source:** Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T
- **License:** CC BY 4.0
- **Size:** 395 observations, 33 original features
- **Features used:** 30 (G1 and G2 excluded by design — see notebook for rationale)
- **Target:** Binary pass/fail derived from G3 ≥ 10
---
 
## Dependencies
 
```
streamlit>=1.31.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.4.0
matplotlib>=3.7.0
```
 
---
 
## Reproducibility Notes
 
- All random operations use `random_state=42`
- Train/test split is 80/20 stratified
- Cross-validation uses 5 stratified folds
- The app trains the model live from the data URL on first load (cached for the session)
 
