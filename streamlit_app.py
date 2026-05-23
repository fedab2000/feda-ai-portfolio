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

col1, col2 = st.columns(2)

with col1:

    st.subheader("Insurance Pricing AI")

    st.write("""
    Predictive insurance pricing application using
    frequency and severity modeling techniques.
    """)

    st.link_button(
        "Open App",
        "PASTE_YOUR_INSURANCE_APP_URL_HERE"
    )

with col2:

    st.subheader("Healthcare Readmission Predictor")

    st.write("""
    XGBoost-based healthcare risk prediction model
    for patient readmission analysis.
    """)

    st.link_button(
        "Open App",
        "PASTE_YOUR_HEALTHCARE_APP_URL_HERE"
    )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    st.subheader("Regularized Regression Comparison")

    st.write("""
    Interactive comparison of Ridge, Lasso,
    and Elastic Net regression models.
    """)

    st.link_button(
        "Open App",
        "PASTE_YOUR_REGRESSION_APP_URL_HERE"
    )

with col4:

    st.subheader("Dental Recommendation AI")

    st.write("""
    AI-powered recommendation and analytics
    prototype for dental patient insights.
    """)

    st.link_button(
        "Open App",
        "PASTE_YOUR_DENTAL_APP_URL_HERE"
    )

st.markdown("---")

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
""")

st.markdown("---")

st.caption(
    "Author: Feda Bashbishi | University of Waterloo"
)