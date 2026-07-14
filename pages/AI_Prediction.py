import streamlit as st
import pandas as pd

from utils.model_loader import model, scaler
from utils.risk_engine import analyze_prediction

st.set_page_config(page_title="AI Prediction", layout="wide")

st.title("🤖 AI Failure Prediction")

st.markdown("Enter current equipment sensor readings.")

col1, col2 = st.columns(2)

with col1:

    air = st.number_input(
        "Air Temperature (K)",
        value=300.0
    )

    process = st.number_input(
        "Process Temperature (K)",
        value=310.0
    )

    rpm = st.number_input(
        "Rotational Speed (rpm)",
        value=1500
    )

with col2:

    torque = st.number_input(
        "Torque (Nm)",
        value=40.0
    )

    wear = st.number_input(
        "Tool Wear (min)",
        value=100
    )

    machine = st.selectbox(
        "Machine Type",
        ["L","M","H"]
    )

if st.button("Predict"):

    df = pd.DataFrame({

        "Air temperature [K]":[air],

        "Process temperature [K]":[process],

        "Rotational speed [rpm]":[rpm],

        "Torque [Nm]":[torque],

        "Tool wear [min]":[wear]

    })

    scaled = scaler.transform(df)

    X = pd.DataFrame(

        scaled,

        columns=[

            "Air_temperature_K",

            "Process_temperature_K",

            "Rotational_speed_rpm",

            "Torque_Nm",

            "Tool_wear_min"

        ]

    )

    X["Type_H"] = 1 if machine=="H" else 0
    X["Type_L"] = 1 if machine=="L" else 0
    X["Type_M"] = 1 if machine=="M" else 0

    probability = model.predict_proba(X)[0][1]

    result = analyze_prediction(probability)

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Failure Probability",
        f"{probability*100:.2f}%"
    )

    c2.metric(
        "Risk Score",
        result["risk_score"]
    )

    c3.metric(
        "Health Score",
        result["health_score"]
    )

    if result["status"]=="Critical":

        st.error(result["recommendation"])

    elif result["status"]=="Warning":

        st.warning(result["recommendation"])

    else:

        st.success(result["recommendation"])