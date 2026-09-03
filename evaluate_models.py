import os
import json
import joblib
import pandas as pd
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# AGRIMATE - ML MODEL EVALUATION
# ============================================================

print("\n")
print("============================================================")
print("             AGRIMATE ML MODEL EVALUATION")
print("============================================================")


# ============================================================
# 1. CROP RECOMMENDATION MODEL - RANDOM FOREST
# ============================================================

print("\n")
print("============================================================")
print("🌾 CROP RECOMMENDATION MODEL")
print("============================================================")


# Dataset
CROP_DATASET = "Crop_recommendation.csv"

data = pd.read_csv(CROP_DATASET)

X = data.drop("label", axis=1)
y = data["label"]


# Same test split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Load model
CROP_MODEL_PATH = "model/crop_recommendation_model.pkl"

crop_model = joblib.load(CROP_MODEL_PATH)


# Predictions
y_pred = crop_model.predict(X_test)


# Metrics
crop_accuracy = accuracy_score(y_test, y_pred)

crop_precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

crop_recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

crop_f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)


# Display results
print(f"\nAccuracy  : {crop_accuracy * 100:.2f}%")
print(f"Precision : {crop_precision * 100:.2f}%")
print(f"Recall    : {crop_recall * 100:.2f}%")
print(f"F1 Score  : {crop_f1 * 100:.2f}%")


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ============================================================
# 2. PLANT DISEASE CNN MODEL
# ============================================================

print("\n")
print("============================================================")
print("🌿 PLANT DISEASE CNN MODEL")
print("============================================================")


# ============================================================
# Device
# ============================================================

device = torch.device("cpu")

print("\nUsing device:", device)


# ============================================================
# Dataset
# ============================================================

DISEASE_DATASET_PATH = (
    r"C:\AgriMate\diseas_dataset\plantvillage dataset\color"
)

if not os.path.exists(DISEASE_DATASET_PATH):
    print("\nERROR: Disease dataset not found!")
    print(DISEASE_DATASET_PATH)
    exit()


# ============================================================
# Same transformation used during training
# ============================================================

transform = transforms.Compose([
    transforms.Resize((96, 96)),
    transforms.ToTensor()
])


# ============================================================
# Load full dataset
# ============================================================

full_dataset = datasets.ImageFolder(
    DISEASE_DATASET_PATH,
    transform=transform
)

print("Total images:", len(full_dataset))
print("Total classes:", len(full_dataset.classes))


# ============================================================
# Recreate same 8000-image dataset
# ============================================================

MAX_IMAGES = 8000

if len(full_dataset) > MAX_IMAGES:

    generator = torch.Generator().manual_seed(42)

    dataset, _ = random_split(
        full_dataset,
        [MAX_IMAGES, len(full_dataset) - MAX_IMAGES],
        generator=generator
    )

else:

    dataset = full_dataset


print("Images used for evaluation:", len(dataset))


# ============================================================
# Recreate same 80/20 validation split
# ============================================================

train_size = int(0.8 * len(dataset))
validation_size = len(dataset) - train_size

train_dataset, validation_dataset = random_split(
    dataset,
    [train_size, validation_size],
    generator=torch.Generator().manual_seed(42)
)


print("Training split:", len(train_dataset))
print("Validation split:", len(validation_dataset))


# ============================================================
# Validation DataLoader
# ============================================================

validation_loader = DataLoader(
    validation_dataset,
    batch_size=32,
    shuffle=False,
    num_workers=0
)


# ============================================================
# CNN MODEL
# Same architecture used during training
# ============================================================

model = nn.Sequential(

    nn.Conv2d(3, 32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),

    nn.Conv2d(32, 64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),

    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),

    nn.Flatten(),

    nn.Linear(128 * 12 * 12, 256),
    nn.ReLU(),

    nn.Dropout(0.3),

    nn.Linear(256, len(full_dataset.classes))
)


model = model.to(device)


# ============================================================
# Load trained CNN
# ============================================================

MODEL_PATH = (
    r"C:\AgriMate\disease_model\plant_disease_cnn.pth"
)

if not os.path.exists(MODEL_PATH):
    print("\nERROR: Disease CNN model not found!")
    print(MODEL_PATH)
    exit()


checkpoint = torch.load(
    MODEL_PATH,
    map_location=device
)

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model.eval()


# ============================================================
# CNN PREDICTIONS
# ============================================================

all_predictions = []
all_labels = []


print("\nRunning disease model evaluation...")

with torch.no_grad():

    for images, labels in validation_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(
            outputs,
            1
        )

        all_predictions.extend(
            predicted.cpu().numpy()
        )

        all_labels.extend(
            labels.cpu().numpy()
        )


# ============================================================
# CNN METRICS
# ============================================================

disease_accuracy = accuracy_score(
    all_labels,
    all_predictions
)

disease_precision = precision_score(
    all_labels,
    all_predictions,
    average="weighted",
    zero_division=0
)

disease_recall = recall_score(
    all_labels,
    all_predictions,
    average="weighted",
    zero_division=0
)

disease_f1 = f1_score(
    all_labels,
    all_predictions,
    average="weighted",
    zero_division=0
)


# ============================================================
# Display CNN results
# ============================================================

print("\n")
print("============================================================")
print("🌿 PLANT DISEASE CNN RESULTS")
print("============================================================")

print(
    f"\nAccuracy  : {disease_accuracy * 100:.2f}%"
)

print(
    f"Precision : {disease_precision * 100:.2f}%"
)

print(
    f"Recall    : {disease_recall * 100:.2f}%"
)

print(
    f"F1 Score  : {disease_f1 * 100:.2f}%"
)


# ============================================================
# Classification Report
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        all_labels,
        all_predictions,
        target_names=full_dataset.classes,
        zero_division=0
    )
)


# ============================================================
# Confusion Matrix
# ============================================================

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        all_labels,
        all_predictions
    )
)


# ============================================================
# COMPLETE
# ============================================================

print("\n")
print("============================================================")
print("✅ AGRIMATE MODEL EVALUATION COMPLETE")
print("============================================================")

# ============================================================
# SAVE ALL EVALUATION RESULTS
# ============================================================

crop_report_dict = classification_report(
    y_test,
    y_pred,
    output_dict=True,
    zero_division=0
)

crop_confusion = confusion_matrix(
    y_test,
    y_pred
)

disease_report_dict = classification_report(
    all_labels,
    all_predictions,
    target_names=full_dataset.classes,
    output_dict=True,
    zero_division=0
)

disease_confusion = confusion_matrix(
    all_labels,
    all_predictions
)

results = {
    "crop": {
        "accuracy": float(crop_accuracy),
        "precision": float(crop_precision),
        "recall": float(crop_recall),
        "f1": float(crop_f1),

        "classification_report": crop_report_dict,

        "confusion_matrix": crop_confusion.tolist(),

        "classes": list(crop_model.classes_)
    },

    "disease": {
        "accuracy": float(disease_accuracy),
        "precision": float(disease_precision),
        "recall": float(disease_recall),
        "f1": float(disease_f1),

        "classification_report": disease_report_dict,

        "confusion_matrix": disease_confusion.tolist(),

        "classes": list(full_dataset.classes),

        "images_used": len(dataset),
        "training_split": len(train_dataset),
        "validation_split": len(validation_dataset)
    }
}

RESULTS_PATH = "evaluation_results.json"

with open(RESULTS_PATH, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print("\n")
print("============================================================")
print("📁 EVALUATION RESULTS SAVED")
print("============================================================")
print(f"File: {os.path.abspath(RESULTS_PATH)}")
print("============================================================")