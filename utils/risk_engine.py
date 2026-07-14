def analyze_prediction(probability):

    probability = float(probability)

    risk_score = round(probability * 100, 2)
    health_score = round(100 - risk_score, 2)

    if probability >= 0.80:
        status = "Critical"
        priority = "High"
        recommendation = (
            "Immediate inspection required. Schedule maintenance immediately."
        )

    elif probability >= 0.50:
        status = "Warning"
        priority = "Medium"
        recommendation = (
            "Plan preventive maintenance during the next maintenance window."
        )

    else:
        status = "Healthy"
        priority = "Low"
        recommendation = (
            "Continue normal operation and routine monitoring."
        )

    return {
        "probability": probability,
        "risk_score": risk_score,
        "health_score": health_score,
        "status": status,
        "priority": priority,
        "recommendation": recommendation
    }