import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/part1_return_risk_model.joblib")

# Sample new order
new_order = pd.DataFrame([{
    "price_inr": 25000,
    "discount_pct": 20,
    "customer_tenure_days": 180,
    "num_previous_orders": 5,
    "num_previous_returns": 1,
    "delivery_distance_km": 120,
    "delivery_days": 4,
    "rating_given": 4.0,
    "product_category": "Electronics",
    "payment_method": "Prepaid_Card"
}])

# Predict
prediction = model.predict(new_order)[0]
probability = model.predict_proba(new_order)[0][1]

print("=== RETURN RISK PREDICTION ===")
print("Predicted return:", int(prediction))
print(f"Return probability: {probability:.4f}")

if probability >= 0.5:
    print("Risk level: HIGH")
else:
    print("Risk level: LOW")