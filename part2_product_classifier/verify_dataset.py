import pandas as pd

# Load the dataset
df = pd.read_csv("part1_return_risk/orders_dataset.csv")

print("=== PART 2 DATASET VERIFICATION ===")

# Basic dataset information
print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\n=== COLUMNS ===")
print(df.columns.tolist())

# Target distribution
print("\n=== PRODUCT CATEGORY DISTRIBUTION ===")
print(df["product_category"].value_counts())

print("\n=== PRODUCT CATEGORY DISTRIBUTION (%) ===")
print(
    (df["product_category"].value_counts(normalize=True) * 100)
    .round(2)
)

# Missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Data types
print("\n=== DATA TYPES ===")
print(df.dtypes)

# Unique values for categorical columns
print("\n=== PAYMENT METHOD DISTRIBUTION ===")
print(df["payment_method"].value_counts())

print("\n=== WEEKEND ORDER DISTRIBUTION ===")
print(df["is_weekend_order"].value_counts())

# Target validation
print("\n=== TARGET VALIDATION ===")
print("Unique product categories:", df["product_category"].nunique())
print(
    "Categories:",
    sorted(df["product_category"].unique())
)