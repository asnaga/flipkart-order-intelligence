import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# =========================
# 1. LOAD DATA
# =========================

df = pd.read_csv("part1_return_risk/orders_dataset.csv")

X = df.drop(columns=["returned"])
y = df["returned"]

# =========================
# 2. FEATURES
# =========================

numeric_features = [
    "price_inr",
    "discount_pct",
    "customer_tenure_days",
    "num_previous_orders",
    "num_previous_returns",
    "delivery_distance_km",
    "delivery_days",
    "rating_given"
]

categorical_features = [
    "product_category",
    "payment_method"
]

# =========================
# 3. PREPROCESSING
# =========================

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

# =========================
# 4. TRAIN / TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =========================
# 5. MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# =========================
# 6. TRAIN
# =========================

print("=== MODEL TRAINING ===")

pipeline.fit(X_train, y_train)

print("Training completed successfully.")

# =========================
# 7. PREDICTION
# =========================

y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

# =========================
# 8. EVALUATION
# =========================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
roc_auc = roc_auc_score(y_test, y_prob)

print("\n=== MODEL PERFORMANCE ===")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")

# =========================
# 9. SAVE MODEL
# =========================

joblib.dump(
    pipeline,
    "models/part1_return_risk_model.joblib"
)

print("\nModel saved successfully:")
print("models/part1_return_risk_model.joblib")