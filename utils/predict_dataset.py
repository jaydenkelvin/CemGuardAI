import pandas as pd

from utils.model_loader import model, scaler
from utils.risk_engine import analyze_prediction


def predict_dataset(df):

    df = df.copy()

    # Keep original columns
    original_df = df.copy()

    # One-hot encode machine type
    df = pd.get_dummies(df, columns=["Type"])

    # Ensure all expected columns exist
    for col in ["Type_H", "Type_L", "Type_M"]:
        if col not in df.columns:
            df[col] = 0

    # Scale numeric features
    numerical = df[
        [
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]"
        ]
    ]

    scaled = scaler.transform(numerical)

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

    X["Type_H"] = df["Type_H"].values
    X["Type_L"] = df["Type_L"].values
    X["Type_M"] = df["Type_M"].values

    # Correct feature order
    X = X[
        [
            "Air_temperature_K",
            "Process_temperature_K",
            "Rotational_speed_rpm",
            "Torque_Nm",
            "Tool_wear_min",
            "Type_H",
            "Type_L",
            "Type_M"
        ]
    ]

    # Model prediction
    probabilities = model.predict_proba(X)[:, 1]

    # Restore original dataframe
    df = original_df

    df["Failure Probability"] = probabilities

    results = [analyze_prediction(p) for p in probabilities]

    df["Risk Score"] = [r["risk_score"] for r in results]
    df["Health Score"] = [r["health_score"] for r in results]
    df["Status"] = [r["status"] for r in results]
    df["Priority"] = [r["priority"] for r in results]
    df["Recommendation"] = [r["recommendation"] for r in results]

    # Create prototype asset names
    df["Asset"] = [
        f"Asset {i:03d}"
        for i in range(1, len(df) + 1)
    ]

    return df