from pathlib import Path
import pandas as pd


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Existing Part 1 dataset
DATASET_PATH = PROJECT_ROOT / "part1_return_risk" / "orders_dataset.csv"


# Load dataset once
df = pd.read_csv(DATASET_PATH)


def get_order(order_id):
    """
    Return order information for a given order ID.
    """

    order = df[df["order_id"] == order_id]

    if order.empty:
        return None

    return order.iloc[0].to_dict()


if __name__ == "__main__":

    print("=== ORDER LOOKUP TOOL ===")

    test_order_id = 1

    result = get_order(test_order_id)

    if result is None:
        print(f"Order {test_order_id} not found.")
    else:
        print(f"Order {test_order_id} found:")
        print(result)