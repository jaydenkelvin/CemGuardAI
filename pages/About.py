import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="📘",
    layout="wide"
)

st.title("📘 Methodology & Implementation")

st.markdown("""
# CemGuard AI

An AI-powered Predictive Maintenance & Reliability Early Warning System developed for the

**Dangote Cement Plc University Engineering Challenge 2026**
""")

st.divider()

# --------------------------------------------------------
# Problem
# --------------------------------------------------------

st.header("🏭 Problem Statement")

st.write("""
Critical equipment such as crushers, raw mills, coal mills, rotary kilns,
cement mills and packing machines experience unexpected failures that
reduce plant reliability, increase maintenance cost and cause production losses.

Traditional maintenance is often reactive or scheduled, making it difficult
to detect failures early.

CemGuard AI provides an intelligent early-warning system that predicts
equipment failure before breakdown occurs.
""")

st.divider()

# --------------------------------------------------------
# Framework
# --------------------------------------------------------

st.header("⚙ Reliability Early Warning Framework")

st.markdown("""

Equipment Sensors

⬇

Sensor Data Collection

⬇

Data Preprocessing

⬇

XGBoost Machine Learning Model

⬇

Failure Probability Prediction

⬇

Risk Score Calculation

⬇

Maintenance Recommendation

⬇

Operations Dashboard

""")

st.divider()

# --------------------------------------------------------
# Risk Model
# --------------------------------------------------------

st.header("📊 Risk Scoring Model")

st.write("""

Risk Score = Failure Probability × 100

Health Score = 100 − Risk Score

""")

st.table({

"Failure Probability":[

"< 50%",

"50% - 79%",

"80% - 100%"

],

"Status":[

"Healthy",

"Warning",

"Critical"

],

"Priority":[

"Low",

"Medium",

"High"

]

})

st.divider()

# --------------------------------------------------------
# Workflow
# --------------------------------------------------------

st.header("🔧 Maintenance Escalation Workflow")

st.markdown("""

Sensor Reading

⬇

AI Prediction

⬇

Risk Score

⬇

Is Risk > 80% ?

⬇

YES

⬇

Notify Maintenance Supervisor

⬇

Inspect Equipment

⬇

Repair / Replace Component

⬇

Return Equipment to Service

⬇

Continuous Monitoring

""")

st.divider()

# --------------------------------------------------------
# Roadmap
# --------------------------------------------------------

st.header("🛣 Implementation Roadmap")

st.table({

"Phase":[

"Pilot",

"Integration",

"Training",

"Deployment"

],

"Timeline":[

"Month 1",

"Month 2",

"Month 3",

"Month 4"

],

"Activity":[

"Deploy prototype on selected production line",

"Integrate with PLC/SCADA systems",

"Train maintenance & operations staff",

"Full plant-wide deployment"

]

})

st.divider()

# --------------------------------------------------------
# Assumptions
# --------------------------------------------------------

st.header("📌 Assumptions & Data Limitations")

st.write("""

• The AI4I Predictive Maintenance Dataset was used as representative industrial equipment data.

• Proprietary Dangote Cement operational data was not publicly available.

• In a production deployment, live sensor readings would be collected from PLCs,
SCADA systems or Industrial IoT devices.

• The prototype demonstrates the predictive maintenance workflow rather than
a live operational deployment.

""")

st.divider()

# --------------------------------------------------------
# Benefits
# --------------------------------------------------------

st.header("✅ Expected Benefits")

st.markdown("""

- Reduce unplanned equipment downtime

- Improve maintenance planning

- Increase equipment availability

- Support root-cause analysis

- Improve production reliability

- Reduce maintenance cost

- Improve safety by identifying high-risk equipment early

""")