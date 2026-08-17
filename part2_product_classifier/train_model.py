import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load dataset
df = pd.read_csv("part1_return_risk/orders_dataset.csv")


print("=== PART 2 MODEL TRAINING ===")


# Features and target
X = df.drop(columns=["product_category", "order_id"])
y = df["product_category"]


# Identify categorical and numerical features
categorical_features = ["payment_method"]

numerical_features = [
    "price_inr",
    "discount_pct",
    "customer_tenure_days",
    "num_previous_orders",
    "num_previous_returns",
    "delivery_distance_km",
    "delivery_days",
    "is_weekend_order",
    "rating_given"
]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("Training rows:", len(X_train))
print("Test rows:", len(X_test))


# Random Forest classifier
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)


# Complete ML pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("model", model)
    ]
)


# Train only on training data
pipeline.fit(X_train, y_train)


print("\n=== MODEL TRAINING COMPLETE ===")


# Predictions
y_pred = pipeline.predict(X_test)


# Model evaluation
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)


print("\n=== MODEL PERFORMANCE ===")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")


print("\n=== CLASS DISTRIBUTION ===")
print(y_test.value_counts())


print("\n=== BASELINE COMPARISON ===")
print("Baseline Accuracy:  0.3300")
print("Baseline Macro F1:  0.0992")
print(f"Model Accuracy:     {accuracy:.4f}")
print(f"Model Macro F1:     {f1:.4f}")


if accuracy > 0.3300 and f1 > 0.0992:
    print("\nModel performs better than the baseline.")
else:
    print("\nModel does not clearly outperform the baseline yet.")
    
# Save trained model pipeline
joblib.dump(
    pipeline,
    "models/part2_product_classifier_model.joblib"
)

print("\nModel saved successfully:")
print("models/part2_product_classifier_model.joblib")