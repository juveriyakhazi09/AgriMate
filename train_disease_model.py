import os
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms, models


# ==========================================
# AgriMate - Fast Plant Disease CNN
# ==========================================

print("======================================")
print("AgriMate Plant Disease Detection")
print("======================================")


# ==========================================
# Device
# ==========================================

device = torch.device("cpu")

print("Using device:", device)


# ==========================================
# Dataset
# ==========================================

DATASET_PATH = r"C:\AgriMate\diseas_dataset\plantvillage dataset\color"

if not os.path.exists(DATASET_PATH):
    print("ERROR: Dataset not found!")
    print(DATASET_PATH)
    exit()


# ==========================================
# Image transformation
# ==========================================

transform = transforms.Compose([
    transforms.Resize((96, 96)),
    transforms.ToTensor()
])


# ==========================================
# Load dataset
# ==========================================

print("\nLoading dataset...")

full_dataset = datasets.ImageFolder(
    DATASET_PATH,
    transform=transform
)

print("Total images:", len(full_dataset))
print("Total classes:", len(full_dataset.classes))


# ==========================================
# Use a smaller dataset for fast training
# ==========================================

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


print("Images used for training:", len(dataset))


# ==========================================
# Train / Validation split
# ==========================================

train_size = int(0.8 * len(dataset))
validation_size = len(dataset) - train_size

train_dataset, validation_dataset = random_split(
    dataset,
    [train_size, validation_size],
    generator=torch.Generator().manual_seed(42)
)

print("Training images:", len(train_dataset))
print("Validation images:", len(validation_dataset))


# ==========================================
# Data loaders
# ==========================================

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True,
    num_workers=0
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=32,
    shuffle=False,
    num_workers=0
)


# ==========================================
# CNN Model
# ==========================================

print("\nCreating CNN model...")

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


# ==========================================
# Loss and optimizer
# ==========================================

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# ==========================================
# Training
# ==========================================

EPOCHS = 2

print("\n======================================")
print("Starting FAST CNN training")
print("======================================")

for epoch in range(EPOCHS):

    model.train()

    running_loss = 0
    correct = 0
    total = 0

    for batch_index, (images, labels) in enumerate(train_loader):

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

        if (batch_index + 1) % 50 == 0:

            print(
                f"Epoch {epoch + 1}/{EPOCHS} "
                f"- Batch {batch_index + 1}/{len(train_loader)}"
            )


    train_accuracy = 100 * correct / total


    # ======================================
    # Validation
    # ======================================

    model.eval()

    validation_correct = 0
    validation_total = 0

    with torch.no_grad():

        for images, labels in validation_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            validation_total += labels.size(0)

            validation_correct += (
                predicted == labels
            ).sum().item()


    validation_accuracy = (
        100 * validation_correct / validation_total
    )


    print(
        f"\nEpoch [{epoch + 1}/{EPOCHS}]"
    )

    print(
        f"Training Accuracy: {train_accuracy:.2f}%"
    )

    print(
        f"Validation Accuracy: {validation_accuracy:.2f}%"
    )


# ==========================================
# Save model
# ==========================================

os.makedirs(
    r"C:\AgriMate\disease_model",
    exist_ok=True
)


MODEL_PATH = (
    r"C:\AgriMate\disease_model"
    r"\plant_disease_cnn.pth"
)


torch.save(
    {
        "model_state_dict": model.state_dict(),
        "classes": full_dataset.classes
    },
    MODEL_PATH
)


print("\n======================================")
print("CNN TRAINING COMPLETE!")
print("======================================")

print(
    "Model saved at:"
)

print(MODEL_PATH)