import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


# ============================================================
# PART 2 - PRODUCT CATEGORY CLASSIFIER
# PREPROCESSING PIPELINE
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

NUMERIC_FEATURES = [
    "price_inr",
    "discount_pct",
    "customer_tenure_days",
    "num_previous_orders",
    "num_previous_returns",
    "delivery_distance_km",
    "delivery_days",
    "is_weekend_order",
]

CATEGORICAL_FEATURES = [
    "payment_method",
]


FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES


# ------------------------------------------------------------
# Separate X and y
# ------------------------------------------------------------

X = df[FEATURES]
y = df[TARGET]


# ------------------------------------------------------------
# Numeric preprocessing
# ------------------------------------------------------------

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)


# ------------------------------------------------------------
# Categorical preprocessing
# ------------------------------------------------------------

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "onehot",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            )
        ),
    ]
)


# ------------------------------------------------------------
# Combined preprocessing pipeline
# ------------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_pipeline,
            NUMERIC_FEATURES
        ),
        (
            "categorical",
            categorical_pipeline,
            CATEGORICAL_FEATURES
        ),
    ]
)


# ------------------------------------------------------------
# Fit preprocessing
# ------------------------------------------------------------

X_processed = preprocessor.fit_transform(X)


# ------------------------------------------------------------
# Display results
# ------------------------------------------------------------

print("=== PART 2 PREPROCESSING ===")

print("Original shape:", X.shape)
print("Processed shape:", X_processed.shape)

print("\nTarget classes:")
print(sorted(y.unique()))

print("\nTarget distribution:")
print(y.value_counts())

print("\nPreprocessing completed successfully.")