import streamlit as st

st.set_page_config(
    page_title="Feda Bashbishi AI Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.title("Feda Bashbishi - AI & Data Science Portfolio")

st.markdown("""
MBA, M.Sc. Eng., MDSAI  
University of Waterloo

This portfolio showcases machine learning, predictive analytics,
and AI applications developed using Python, Scikit-learn,
XGBoost, and Streamlit.
""")

st.markdown("---")

# =====================================================
# FIRST ROW OF PROJECTS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Insurance Pricing AI")

    st.write("""
    Predictive insurance pricing application using
    frequency and severity modeling techniques.
    """)

    st.link_button(
        "Open App",
        "https://insurance-pricing-ai-myxjhrl3vaeyahw8kkrmc6.streamlit.app/"
    )

with col2:

    st.subheader("Healthcare Readmission Predictor")

    st.write("""
    XGBoost-based healthcare risk prediction model
    for patient readmission analysis.
    """)

    st.link_button(
        "Open App",
        "https://healthcare-readmission-xgboost-spg4bqhqnmlxjiemckkmlg.streamlit.app/"
    )

with col3:

    st.subheader("Auto Insurance Fraud Detection")

    st.write("""
    End-to-end machine learning solution for detecting
    potentially fraudulent automobile insurance claims
    using feature selection, predictive modeling,
    confusion matrix analysis, and fraud risk scoring.
    """)

    st.link_button(
        "Open App",
        "https://autofrauddetectionapp-hnsvzpa8ft3daymuve23al.streamlit.app/"
    )

st.markdown("---")

# =====================================================
# SECOND ROW OF PROJECTS
# =====================================================

col4, col5, col6 = st.columns(3)

with col4:

    st.subheader("Regularized Regression Comparison")

    st.write("""
    Interactive comparison of Ridge, Lasso,
    and Elastic Net regression models.
    """)

    st.link_button(
        "Open App",
        "https://penaltymodelselection-ftkmcdpmz52soaxswu52cj.streamlit.app/"
    )

with col5:

    st.subheader("Dental Recommendation AI")

    st.write("""
    AI-powered recommendation and analytics
    prototype for dental patient insights.
    """)

    st.link_button(
        "Open App",
        "https://dentalpatientanalyticsrecommendation-ai-h3ry9agfcmqhpupbvakrz9.streamlit.app/"
    )

with col6:

    st.subheader("Ontario University Policy Analytics Platform")

    st.write("""
    The Ontario University Policy Analytics Platform is a synthetic
    higher education analytics project designed to simulate how
    Ontario universities and sector organizations can use data to
    support strategic planning, policy analysis, and executive
    decision-making.
    """)

    st.link_button(
        "Open App",
        "https://ontariouniversitypolicyanalytics-nxxbrmx7m4varszyi4qqno.streamlit.app/"
    )

st.markdown("---")

# =====================================================
# TECHNICAL SKILLS
# =====================================================

st.subheader("Technical Skills")

st.markdown("""
- Python
- Machine Learning
- Scikit-learn
- XGBoost
- Streamlit
- Power BI
- SQL
- Predictive Analytics
- Data Visualization
- Statistical Learning
- Feature Selection (LASSO, Ridge, Elastic Net)
- Fraud Detection Analytics
- Insurance Analytics
- Model Evaluation & Explainability
""")

st.markdown("---")

st.caption(
    "Author: Feda Bashbishi | University of Waterloo"
)
```
