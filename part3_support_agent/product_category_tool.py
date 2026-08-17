from pathlib import Path
import joblib
import pandas as pd


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Existing Part 2 model
MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "part2_product_classifier_model.joblib"
)

# Existing dataset
DATASET_PATH = (
    PROJECT_ROOT
    / "part1_return_risk"
    / "orders_dataset.csv"
)


# Load model and dataset
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATASET_PATH)


def get_product_category(order_id):
    """
    Predict the product category for an existing order.
    """

    order = df[df["order_id"] == order_id]

    if order.empty:
        return None

    # Remove the target and order ID.
    features = order.drop(
        columns=["product_category", "order_id"]
    )

    prediction = model.predict(features)[0]

    return {
        "order_id": int(order_id),
        "product_category": str(prediction)
    }


if __name__ == "__main__":

    print("=== PRODUCT CATEGORY TOOL ===")

    test_order_id = 1

    result = get_product_category(test_order_id)

    if result is None:
        print(f"Order {test_order_id} not found.")
    else:
        print(f"Order ID: {result['order_id']}")
        print(
            f"Product Category: "
            f"{result['product_category']}"
        )