import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Student Pass Predictor",
    page_icon="🎓",
    layout="wide"
)

# ── Load + train model (cached so it only runs once) ─────────
@st.cache_resource
def load_model():
    df_raw = pd.read_csv(
        'https://quantdev.ssri.psu.edu/sites/qdev/files/student-mat.csv',
        sep=';'
    )
    df = df_raw.drop(columns=['G1', 'G2']).copy()
    df['pass'] = (df['G3'] >= 10).astype(int)
    df = df.drop(columns=['G3'])

    df_enc = df.copy()
    encoders = {}
    for col in df_enc.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df_enc[col] = le.fit_transform(df_enc[col])
        encoders[col] = le

    X = df_enc.drop(columns=['pass'])
    y = df_enc['pass']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)

    return rf, X.columns.tolist(), encoders

model, feature_cols, encoders = load_model()

# ── Header ───────────────────────────────────────────────────
st.title("🎓 Student Pass Predictor")
st.markdown(
    "Predicts the probability that a student will **pass** their final math exam "
    "(score ≥ 10/20) using enrollment-time information — no prior grades needed."
)
st.markdown("---")

# ── Sidebar inputs ───────────────────────────────────────────
st.sidebar.header("Student Profile")
st.sidebar.markdown("Adjust the sliders to describe the student.")

studytime  = st.sidebar.slider("Weekly study time", 1, 4, 2,
    help="1=<2h, 2=2–5h, 3=5–10h, 4=>10h")
failures   = st.sidebar.slider("Past class failures", 0, 3, 0)
absences   = st.sidebar.slider("Number of school absences", 0, 75, 4)
goout      = st.sidebar.slider("Going out with friends (1–5)", 1, 5, 3)
Dalc       = st.sidebar.slider("Workday alcohol consumption (1–5)", 1, 5, 1)
Walc       = st.sidebar.slider("Weekend alcohol consumption (1–5)", 1, 5, 2)
Medu       = st.sidebar.slider("Mother's education (0–4)", 0, 4, 2,
    help="0=none, 1=primary, 2=middle, 3=secondary, 4=higher")
Fedu       = st.sidebar.slider("Father's education (0–4)", 0, 4, 2)
famrel     = st.sidebar.slider("Family relationship quality (1–5)", 1, 5, 4)
health     = st.sidebar.slider("Current health status (1–5)", 1, 5, 3)
age        = st.sidebar.slider("Age", 15, 22, 17)

sex        = st.sidebar.selectbox("Sex", ["F", "M"])
address    = st.sidebar.selectbox("Home address", ["U (Urban)", "R (Rural)"])
Pstatus    = st.sidebar.selectbox("Parents' cohabitation", ["T (Together)", "A (Apart)"])
schoolsup  = st.sidebar.selectbox("Extra school support", ["no", "yes"])
famsup     = st.sidebar.selectbox("Family educational support", ["yes", "no"])
higher     = st.sidebar.selectbox("Wants higher education", ["yes", "no"])
internet   = st.sidebar.selectbox("Internet access at home", ["yes", "no"])
romantic   = st.sidebar.selectbox("In a romantic relationship", ["no", "yes"])
activities = st.sidebar.selectbox("Extra-curricular activities", ["no", "yes"])

# ── Build input row ──────────────────────────────────────────
def make_input():
    row = {
        'school': 0,           # GP default
        'sex': 0 if sex == "F" else 1,
        'age': age,
        'address': 1 if address.startswith("U") else 0,
        'famsize': 0,          # GT3 default
        'Pstatus': 1 if Pstatus.startswith("T") else 0,
        'Medu': Medu,
        'Fedu': Fedu,
        'Mjob': 0,
        'Fjob': 0,
        'reason': 0,
        'guardian': 1,         # mother default
        'traveltime': 1,
        'studytime': studytime,
        'failures': failures,
        'schoolsup': 1 if schoolsup == "yes" else 0,
        'famsup': 1 if famsup == "yes" else 0,
        'paid': 0,
        'activities': 1 if activities == "yes" else 0,
        'nursery': 1,
        'higher': 1 if higher == "yes" else 0,
        'internet': 1 if internet == "yes" else 0,
        'romantic': 1 if romantic == "yes" else 0,
        'famrel': famrel,
        'freetime': 3,
        'goout': goout,
        'Dalc': Dalc,
        'Walc': Walc,
        'health': health,
        'absences': absences,
    }
    return pd.DataFrame([row])[feature_cols]

input_df = make_input()

# ── Prediction ───────────────────────────────────────────────
proba      = model.predict_proba(input_df)[0]
pass_prob  = proba[1]
fail_prob  = proba[0]
prediction = "PASS" if pass_prob >= 0.5 else "FAIL"

# Bootstrap uncertainty estimate
tree_preds = np.array([tree.predict_proba(input_df)[0][1]
                        for tree in model.estimators_])
ci_low  = np.percentile(tree_preds, 5)
ci_high = np.percentile(tree_preds, 95)

# ── Results layout ───────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    color = "#1D9E75" if prediction == "PASS" else "#E24B4A"
    st.markdown(
        f"<div style='background:{color}20; border:2px solid {color}; "
        f"border-radius:12px; padding:20px; text-align:center;'>"
        f"<p style='font-size:14px; color:{color}; margin:0;'>Prediction</p>"
        f"<p style='font-size:42px; font-weight:700; color:{color}; margin:0;'>{prediction}</p>"
        f"</div>",
        unsafe_allow_html=True
    )

with col2:
    st.metric("Pass probability", f"{pass_prob:.1%}")
    st.caption(f"90% confidence interval: {ci_low:.1%} – {ci_high:.1%}")

with col3:
    st.metric("Fail probability", f"{fail_prob:.1%}")
    st.caption("Based on 200-tree Random Forest")

st.markdown("---")

# ── Probability gauge chart ───────────────────────────────────
st.subheader("Pass probability")

fig, ax = plt.subplots(figsize=(8, 1.2))
ax.barh(0, 1, color="#f0f0f0", height=0.5)
ax.barh(0, pass_prob, color="#1D9E75" if pass_prob >= 0.5 else "#E24B4A", height=0.5)
ax.axvline(0.5, color="#888", linestyle="--", linewidth=1)
ax.set_xlim(0, 1)
ax.set_yticks([])
ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
ax.set_xlabel("Predicted pass probability")
# CI shading
ax.barh(0, ci_high - ci_low, left=ci_low,
        color="#1D9E75" if pass_prob >= 0.5 else "#E24B4A",
        height=0.5, alpha=0.25, label="90% CI")
ax.legend(loc="upper left", fontsize=9)
ax.spines[['top','right','left']].set_visible(False)
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.caption(
    "⚠️ Predictive model only — feature importance does not imply causal effect. "
    "Use as a screening tool alongside counselor judgment."
)

st.markdown("---")

# ── Feature importance chart ──────────────────────────────────
st.subheader("What drives this prediction?")
st.caption("Top 10 most predictive features — predictive importance, not causal effect.")

importances = pd.Series(model.feature_importances_, index=feature_cols).sort_values()
top10 = importances.tail(10)

fig2, ax2 = plt.subplots(figsize=(8, 4))
colors = ["#378ADD" if f not in ['studytime','failures','absences','Medu','Fedu']
          else "#1D9E75" for f in top10.index]
top10.plot(kind='barh', ax=ax2, color=colors)
ax2.set_xlabel("Mean decrease in impurity")
ax2.set_title("Feature importance (Random Forest)\n⚠ Predictive importance, not causal effect",
              fontsize=11)
ax2.spines[['top','right']].set_visible(False)
plt.tight_layout()
st.pyplot(fig2)
plt.close()

# ── About ─────────────────────────────────────────────────────
with st.expander("About this model"):
    st.markdown("""
**Dataset:** UCI Student Performance (Math), Cortez & Silva 2008  
**Model:** Random Forest (200 trees, random_state=42)  
**Training:** 80/20 stratified train/test split  
**Features:** 30 demographic, social, and behavioral features — G1 and G2 (prior period grades) deliberately excluded to simulate enrollment-time prediction  
**Target:** Binary pass/fail derived from G3 ≥ 10  

**Limitations:**
- Trained on two Portuguese schools from 2008 — may not generalize broadly
- Class imbalance (~67% pass) means recall for fail class is prioritized over overall accuracy
- This is a screening tool, not a decision rule — counselor judgment should always be applied
""")
