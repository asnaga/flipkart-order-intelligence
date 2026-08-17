import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


# Load dataset
df = pd.read_csv("part1_return_risk/orders_dataset.csv")

# Features and target
X = df.drop(columns=["order_id", "returned"])
y = df["returned"]

# Stratified 80/20 split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42,
)

# Dummy baseline
model = DummyClassifier(
    strategy="most_frequent"
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, pos_label=1)

print("=== DUMMY CLASSIFIER BASELINE ===")
print("Strategy: most_frequent")
print("Accuracy:", round(accuracy, 4))
print("F1-score (returned=1):", round(f1, 4))

print("\n=== CLASS DISTRIBUTION ===")
print(y_test.value_counts())

print("\n=== BASELINE INTERPRETATION ===")
print(
    "The DummyClassifier always predicts the majority class (returned=0). "
    "Therefore, its accuracy can appear reasonably high because most orders "
    "are not returned. However, it has zero recall and zero F1-score for "
    "the returned=1 class, making it useless for identifying risky orders."
)