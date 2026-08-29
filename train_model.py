import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Separate input and output
X = df.drop("label", axis=1)
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("AgriMate Model Training Complete!")
print("----------------------------------")
print("Dataset size:", df.shape)
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Accuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100, "%")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save trained model
import os

os.makedirs("model", exist_ok=True)

with open("model/crop_recommendation_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
print("Location: model/crop_recommendation_model.pkl")