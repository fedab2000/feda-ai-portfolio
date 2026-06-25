import streamlit as st

st.set_page_config(
    page_title="Feda Bashbishi Portfolio",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("Feda Bashbishi")

st.subheader("AI Governance • Analytics Leadership • Machine Learning")

st.markdown("""
**MBA | M.Sc. Engineering | MDSAI (University of Waterloo)**  
📧 fbashbis@uwaterloo.ca

Experienced analytics leader with expertise in AI governance, machine learning,
business intelligence, predictive analytics, data strategy, and executive decision support.

This portfolio showcases interactive applications developed using Python, SQL, Streamlit,
Scikit-learn, XGBoost, NetworkX, Graph Analytics, and Power BI.

The applications presented in this portfolio are intended for educational and
demonstration purposes only. All data used within the applications is synthetic
and does not represent real individuals, organizations, or events.

Students, machine learning practitioners, software developers, QA professionals,
and anyone interested in AI and machine learning development are welcome to visit my
GitHub profile (fedab2000) to explore, download, and learn from these projects.
""")

st.markdown("---")

# =====================================================
# FEATURED PROJECT
# =====================================================

st.header("⭐ Featured Project")

st.subheader("Responsible AI Governance Dashboard")

st.info("""
Executive-level platform for AI governance, risk management, ethics assessment,
compliance monitoring, and AI portfolio oversight.

Built to demonstrate how organizations can operationalize Responsible AI principles
through measurable KPIs, risk scoring, maturity assessments, and executive dashboards.
""")

st.link_button(
    "Launch Responsible AI Governance Dashboard",
    "https://responsible-ai-governance-dashboard-8kubjqifjdvwxkjfvnuvuj.streamlit.app/"
)

st.markdown("---")

# =====================================================
# EXECUTIVE ANALYTICS PROJECTS
# =====================================================

st.header("Executive Analytics & Decision Support")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ontario University Policy Analytics Platform")
    st.write("""
    Executive decision-support platform simulating how universities and sector
    organizations can use analytics for strategic planning, policy analysis,
    enrolment forecasting, and funding sustainability assessments.
    """)
    st.link_button(
        "Open App",
        "https://ontariouniversitypolicyanalytics-nxxbrmx7m4varszyi4qqno.streamlit.app/"
    )

with col2:
    st.subheader("Insurance Fraud Ring Detection & Network Analytics")
    st.write("""
    Standalone graph analytics and unsupervised learning platform for detecting
    suspicious insurance fraud networks using connected components, network
    centrality, K-Means clustering, entity relationship analysis, and SIU
    prioritization scoring.
    """)
    st.link_button(
        "Open App",
        "PASTE_YOUR_FRAUD_RING_STREAMLIT_LINK_HERE"
    )

col3, col4 = st.columns(2)

with col3:
    st.subheader("Auto Insurance Fraud Detection")
    st.write("""
    End-to-end machine learning solution for detecting potentially fraudulent
    automobile insurance claims using feature selection, predictive modeling,
    model evaluation, and fraud risk scoring.
    """)
    st.link_button(
        "Open App",
        "https://autofrauddetectionapp-ndkyh8svzhdyvyuvmybmmq.streamlit.app/"
    )

with col4:
    st.subheader("Insurance Pricing AI")
    st.write("""
    Predictive insurance pricing application using frequency and severity
    modeling techniques to support pricing analytics and risk assessment.
    """)
    st.link_button(
        "Open App",
        "https://insurance-pricing-ai-myxjhrl3vaeyahw8kkrmc6.streamlit.app/"
    )

col5, col6 = st.columns(2)

with col5:
    st.subheader("Healthcare Readmission Predictor")
    st.write("""
    XGBoost-based healthcare risk prediction model for patient readmission
    analysis, risk stratification, and predictive healthcare analytics.
    """)
    st.link_button(
        "Open App",
        "https://healthcare-readmission-xgboost-spg4bqhqnmlxjiemckkmlg.streamlit.app/"
    )

with col6:
    st.subheader("Responsible AI Governance Dashboard")
    st.write("""
    Executive-level platform for AI governance, risk management, ethics assessment,
    compliance monitoring, and AI portfolio oversight.
    """)
    st.link_button(
        "Open App",
        "https://responsible-ai-governance-dashboard-8kubjqifjdvwxkjfvnuvuj.streamlit.app/"
    )

st.markdown("---")

# =====================================================
# ADDITIONAL ML PROJECTS
# =====================================================

st.header("Additional Machine Learning Applications")

col7, col8 = st.columns(2)

with col7:
    st.subheader("Dental Recommendation AI")
    st.write("""
    AI-powered recommendation and analytics prototype for dental patient insights,
    treatment planning, and patient engagement.
    """)
    st.link_button(
        "Open App",
        "https://dentalpatientanalyticsrecommendation-ai-h3ry9agfcmqhpupbvakrz9.streamlit.app/"
    )

with col8:
    st.subheader("Regularized Regression Comparison")
    st.write("""
    Interactive comparison of Ridge, Lasso, and Elastic Net regression models
    for feature selection, regularization, and model optimization.
    """)
    st.link_button(
        "Open App",
        "https://penaltymodelselection-ftkmcdpmz52soaxswu52cj.streamlit.app/"
    )

st.markdown("---")

# =====================================================
# CORE COMPETENCIES
# =====================================================

st.header("Core Competencies")

col9, col10, col11 = st.columns(3)

with col9:
    st.markdown("""
    **Leadership & Strategy**
    - AI Governance
    - Responsible AI
    - Data Strategy
    - Analytics Leadership
    - KPI Development
    - Executive Reporting
    - Fraud Analytics
    """)

with col10:
    st.markdown("""
    **Analytics & Data Science**
    - Python
    - SQL
    - Machine Learning
    - Scikit-learn
    - XGBoost
    - Statistical Learning
    - Network Analytics
    - Graph Analytics
    """)

with col11:
    st.markdown("""
    **Visualization & BI**
    - Power BI
    - Streamlit
    - Dashboard Development
    - Data Visualization
    - Predictive Analytics
    - Data Storytelling
    - Executive Dashboards
    """)

st.markdown("---")

st.caption(
    "Feda Bashbishi | AI Governance, Fraud Analytics, Business Intelligence & Machine Learning Portfolio"
)
