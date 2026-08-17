import pandas as pd

df = pd.read_csv("part1_return_risk/orders_dataset.csv")

print("=== DATASET SUMMARY ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Overall return rate:", round(df["returned"].mean(), 4))
print(
    "Missing rating_given:",
    round(df["rating_given"].isna().mean(), 4)
)

print("\n=== RETURN RATE BY PRODUCT CATEGORY ===")
category_summary = (
    df.groupby("product_category")["returned"]
    .agg(["count", "mean"])
    .rename(columns={"mean": "return_rate"})
)
category_summary["return_rate"] = (
    category_summary["return_rate"] * 100
).round(2)
print(category_summary)

print("\n=== RETURN RATE BY PAYMENT METHOD ===")
payment_summary = (
    df.groupby("payment_method")["returned"]
    .agg(["count", "mean"])
    .rename(columns={"mean": "return_rate"})
)
payment_summary["return_rate"] = (
    payment_summary["return_rate"] * 100
).round(2)
print(payment_summary)

print("\n=== MISSING RATING BY PAYMENT METHOD ===")
missing_by_payment = (
    df.groupby("payment_method")["rating_given"]
    .apply(lambda x: x.isna().mean() * 100)
    .round(2)
)
print(missing_by_payment)

cod_missing = df.loc[
    df["payment_method"] == "COD",
    "rating_given"
].isna().mean() * 100

non_cod_missing = df.loc[
    df["payment_method"] != "COD",
    "rating_given"
].isna().mean() * 100

print("\n=== MISSINGNESS CLASSIFICATION ===")
print(f"COD missing: {cod_missing:.2f}%")
print(f"Non-COD missing: {non_cod_missing:.2f}%")
print(
    "Classification: MAR — missingness depends on the observed "
    "payment_method column."
)