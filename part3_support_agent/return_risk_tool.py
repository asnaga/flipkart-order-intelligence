from pathlib import Path
import joblib
import pandas as pd


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Existing Part 1 model
MODEL_PATH = PROJECT_ROOT / "models" / "part1_return_risk_model.joblib"

# Existing Part 1 dataset
DATASET_PATH = PROJECT_ROOT / "part1_return_risk" / "orders_dataset.csv"


# Load model and dataset
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATASET_PATH)


def get_return_risk(order_id):
    """
    Predict return risk for an existing order.
    """

    order = df[df["order_id"] == order_id]

    if order.empty:
        return None

    # Remove target column and order ID
    features = order.drop(
        columns=["returned", "order_id"]
    )

    # Generate prediction
    prediction = model.predict(features)[0]

    # Generate probability
    probabilities = model.predict_proba(features)[0]

    classes = model.classes_

    probability_map = dict(zip(classes, probabilities))

    return {
        "order_id": int(order_id),
        "return_risk": int(prediction),
        "return_probability": float(
            probability_map.get(1, 0)
        )
    }


if __name__ == "__main__":

    print("=== RETURN RISK TOOL ===")

    test_order_id = 1

    result = get_return_risk(test_order_id)

    if result is None:
        print(f"Order {test_order_id} not found.")
    else:
        print(f"Order ID: {result['order_id']}")
        print(f"Return Risk: {result['return_risk']}")
        print(
            f"Return Probability: "
            f"{result['return_probability']:.4f}"
        )