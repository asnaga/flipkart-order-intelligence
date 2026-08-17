import joblib
import pandas as pd


# Load trained model
model = joblib.load("models/part2_product_classifier_model.joblib")


# Create a new sample order
new_order = pd.DataFrame([
    {
        "price_inr": 24999,
        "discount_pct": 15,
        "payment_method": "Prepaid_Card",
        "customer_tenure_days": 800,
        "num_previous_orders": 12,
        "num_previous_returns": 2,
        "delivery_distance_km": 8.5,
        "delivery_days": 3,
        "is_weekend_order": 1,
        "rating_given": 4.5
    }
])


# Make prediction
prediction = model.predict(new_order)[0]


print("=== PRODUCT CATEGORY PREDICTION ===")
print("Predicted category:", prediction)