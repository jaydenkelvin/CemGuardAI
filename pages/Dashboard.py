import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.predict_dataset import predict_dataset

st.set_page_config(
    page_title="CemGuard AI Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 CemGuard AI")
st.subheader("Predictive Maintenance & Reliability Early Warning System")

st.markdown("""
This prototype analyses industrial equipment sensor readings using an
XGBoost machine learning model to identify high-risk assets before failure.
""")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = load_data()
df = predict_dataset(df)

# ---------------------------------------------------
# KPIs
# ---------------------------------------------------

avg_risk = df["Risk Score"].mean()
plant_health = 100 - avg_risk

critical_assets = len(df[df["Failure Probability"] >= 0.80])

warning_assets = len(
    df[
        (df["Failure Probability"] >= 0.50)
        &
        (df["Failure Probability"] < 0.80)
    ]
)

average_failure = df["Failure Probability"].mean() * 100

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Plant Health",
    f"{plant_health:.1f}%"
)

c2.metric(
    "Critical Assets",
    critical_assets
)

c3.metric(
    "Warning Assets",
    warning_assets
)

c4.metric(
    "Average Failure Probability",
    f"{average_failure:.1f}%"
)

st.divider()

# ---------------------------------------------------
# EARLY WARNING TABLE
# ---------------------------------------------------

st.header("🚨 Early Warning")

top10 = df.sort_values(
    "Failure Probability",
    ascending=False
).head(10)

st.dataframe(

    top10[
        [
            "Asset",
            "Failure Probability",
            "Risk Score",
            "Status",
            "Recommendation"
        ]
    ],

    hide_index=True,
    use_container_width=True

)

st.divider()

# ---------------------------------------------------
# FAILURE PROBABILITY
# ---------------------------------------------------

st.header("📈 Failure Probability Distribution")

chart = df[
    [
        "Asset",
        "Failure Probability"
    ]
].head(100)

chart = chart.set_index("Asset")

st.bar_chart(chart)

st.divider()

# ---------------------------------------------------
# FAILURE MODES
# ---------------------------------------------------

st.header("⚙ Failure Mode Distribution")

failure_modes = pd.DataFrame({

    "Failure Mode":[
        "Tool Wear",
        "Heat Dissipation",
        "Power Failure",
        "Overstrain",
        "Random Failure"
    ],

    "Count":[

        df["TWF"].sum(),
        df["HDF"].sum(),
        df["PWF"].sum(),
        df["OSF"].sum(),
        df["RNF"].sum()

    ]

})

failure_modes = failure_modes.set_index("Failure Mode")

st.bar_chart(failure_modes)

st.divider()

# ---------------------------------------------------
# SUMMARY
# ---------------------------------------------------

st.header("📋 AI Reliability Summary")

st.success(f"""

The AI model analysed **{len(df):,} equipment observations**.

• Average Plant Health: **{plant_health:.1f}%**

• Average Failure Probability: **{average_failure:.1f}%**

• Critical Assets Identified: **{critical_assets}**

• Warning Assets: **{warning_assets}**

The system recommends prioritising inspection and preventive maintenance
for assets with the highest predicted failure probability.

""")

st.divider()

with st.expander("View Analysed Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )