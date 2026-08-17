import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split


# Load dataset
df = pd.read_csv("part1_return_risk/orders_dataset.csv")

# Target
X = df.drop(columns=["order_id", "returned"])
y = df["returned"]

# Feature groups
numeric_features = [
    "price_inr",
    "discount_pct",
    "customer_tenure_days",
    "num_previous_orders",
    "num_previous_returns",
    "delivery_distance_km",
    "delivery_days",
    "rating_given",
]

categorical_features = [
    "product_category",
    "payment_method",
]

# Numeric preprocessing
numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

# Categorical preprocessing
categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

# Combined preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numeric_features),
        ("cat", categorical_pipeline, categorical_features),
    ]
)

# Stratified 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42,
)

# Fit preprocessing ONLY on training data
X_train_processed = preprocessor.fit_transform(X_train)

# Transform test data using the already-fitted preprocessing
X_test_processed = preprocessor.transform(X_test)

print("=== PREPROCESSING COMPLETE ===")
print("Training rows:", len(X_train))
print("Test rows:", len(X_test))
print("Training processed shape:", X_train_processed.shape)
print("Test processed shape:", X_test_processed.shape)
print("Training return rate:", round(y_train.mean(), 4))
print("Test return rate:", round(y_test.mean(), 4))
print("Pipeline fitted only on training data: YES")