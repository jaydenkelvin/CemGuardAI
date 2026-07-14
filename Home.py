import streamlit as st

st.set_page_config(
    page_title="CemGuard AI",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 CemGuard AI")

st.subheader("Predictive Maintenance & Reliability Early Warning System")

st.markdown("""
### Overview

CemGuard AI is an AI-powered predictive maintenance prototype developed for the **Dangote Cement Plc University Engineering Challenge**.

The system analyses industrial equipment sensor data to:

- Predict equipment failure
- Estimate failure probability
- Calculate risk score
- Prioritise maintenance
- Support reliability engineering decisions

---

### Prototype Workflow

Equipment Sensors

↓

Data Processing

↓

Machine Learning Prediction

↓

Risk Scoring

↓

Maintenance Recommendation

↓

Operations Dashboard

---

### Navigate

Use the sidebar to open:

- 🏭 Dashboard
- 🤖 AI Prediction
- 📖 About
""")

st.info(
    "This prototype uses the AI4I Predictive Maintenance Dataset as representative industrial equipment data."
)