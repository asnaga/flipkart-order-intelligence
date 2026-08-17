import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score


# ============================================================
# PART 2 - PRODUCT CATEGORY CLASSIFIER
# MAJORITY CLASS BASELINE
# ============================================================

# Load dataset
df = pd.read_csv("part1_return_risk/orders_dataset.csv")


# ------------------------------------------------------------
# Target
# ------------------------------------------------------------

TARGET = "product_category"


# ------------------------------------------------------------
# Features
# ------------------------------------------------------------

FEATURES = [
    "price_inr",
    "discount_pct",
    "payment_method",
    "customer_tenure_days",
    "num_previous_orders",
    "num_previous_returns",
    "delivery_distance_km",
    "delivery_days",
    "is_weekend_order",
]


X = df[FEATURES]
y = df[TARGET]


# ------------------------------------------------------------
# Train / Test split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


# ------------------------------------------------------------
# Dummy classifier
# ------------------------------------------------------------

baseline = DummyClassifier(
    strategy="most_frequent"
)

baseline.fit(X_train, y_train)


# ------------------------------------------------------------
# Predictions
# ------------------------------------------------------------

y_pred = baseline.predict(X_test)


# ------------------------------------------------------------
# Evaluation
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

f1_macro = f1_score(
    y_test,
    y_pred,
    average="macro"
)


# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=== PART 2 BASELINE CLASSIFIER ===")

print("Strategy: most_frequent")

print(f"Accuracy: {accuracy:.4f}")

print(f"Macro F1 Score: {f1_macro:.4f}")


print("\n=== BASELINE PREDICTION ===")

print(
    "The baseline always predicts:",
    baseline.classes_[baseline.class_prior_.argmax()]
)


print("\n=== CLASS DISTRIBUTION ===")

print(y.value_counts())


print("\n=== BASELINE INTERPRETATION ===")

print(
    "The baseline always predicts the most common "
    "product category. The real ML model should "
    "perform better than this baseline."
)