import joblib
import xgboost as xgb

# Load model
model = xgb.XGBClassifier()
model.load_model("models/xgboost_model.json")

# Load scaler
scaler = joblib.load("models/scaler.pkl")