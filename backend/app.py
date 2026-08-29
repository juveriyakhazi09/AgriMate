from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms
import io
import os


# ============================================================
# AGRIMATE API
# ============================================================

app = FastAPI(title="AgriMate API")


# ============================================================
# CROP RECOMMENDATION MODEL
# ============================================================

try:

    model = joblib.load(
        "model/crop_recommendation_model.pkl"
    )

    print("✅ Crop recommendation model loaded.")

except Exception as error:

    model = None

    print(
        "❌ Could not load crop recommendation model:"
    )

    print(error)


# ============================================================
# CROP INPUT
# ============================================================

class CropData(BaseModel):

    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


# ============================================================
# CROP PREDICTION
# ============================================================

@app.post("/predict")
def predict_crop(data: CropData):

    if model is None:

        raise HTTPException(
            status_code=500,
            detail="Crop recommendation model is not loaded."
        )

    input_data = pd.DataFrame([{

        "N": data.N,
        "P": data.P,
        "K": data.K,
        "temperature": data.temperature,
        "humidity": data.humidity,
        "ph": data.ph,
        "rainfall": data.rainfall

    }])

    prediction = model.predict(
        input_data
    )

    return {

        "recommended_crop": str(
            prediction[0]
        )

    }


# ============================================================
# PLANT DISEASE CNN
# ============================================================

class PlantDiseaseCNN(nn.Module):

    def __init__(self, num_classes=38):

        super().__init__()

        # ----------------------------------------------------
        # CNN FEATURE EXTRACTOR
        # ----------------------------------------------------

        self.features = nn.Sequential(

            # Layer 0
            nn.Conv2d(
                3,
                32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(
                kernel_size=2
            ),

            # Layer 3
            nn.Conv2d(
                32,
                64,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(
                kernel_size=2
            ),

            # Layer 6
            nn.Conv2d(
                64,
                128,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(
                kernel_size=2
            ),

            nn.Conv2d(
                128,
                256,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d(
                (6, 6)
            )

        )

        # ----------------------------------------------------
        # CLASSIFIER
        # ----------------------------------------------------

        self.classifier = nn.Sequential(

            nn.Linear(
                256 * 6 * 6,
                256
            ),

            nn.ReLU(),

            nn.Dropout(
                0.5
            ),

            nn.Linear(
                256,
                num_classes
            )

        )


    def forward(self, x):

        x = self.features(x)

        x = torch.flatten(
            x,
            1
        )

        x = self.classifier(x)

        return x


# ============================================================
# LOAD DISEASE MODEL
# ============================================================

disease_model = None
disease_classes = []


try:

    disease_model_path = (
        "disease_model/"
        "plant_disease_cnn.pth"
    )

    checkpoint = torch.load(
        disease_model_path,
        map_location="cpu"
    )

    disease_classes = checkpoint[
        "classes"
    ]

    disease_model = PlantDiseaseCNN(
        num_classes=len(
            disease_classes
        )
    )

    # --------------------------------------------------------
    # IMPORTANT
    # --------------------------------------------------------
    # The saved CNN uses numeric layer names:
    #
    # 0.weight
    # 0.bias
    # 3.weight
    # 3.bias
    # 6.weight
    # 6.bias
    # 10.weight
    # 10.bias
    # 13.weight
    # 13.bias
    #
    # So we create the model using the exact same structure.
    # --------------------------------------------------------

    saved_state = checkpoint[
        "model_state_dict"
    ]

    # Rebuild exact Sequential structure
    exact_features = nn.Sequential(

        nn.Conv2d(
            3,
            32,
            3,
            padding=1
        ),

        nn.ReLU(),

        nn.MaxPool2d(2),

        nn.Conv2d(
            32,
            64,
            3,
            padding=1
        ),

        nn.ReLU(),

        nn.MaxPool2d(2),

        nn.Conv2d(
            64,
            128,
            3,
            padding=1
        ),

        nn.ReLU(),

        nn.MaxPool2d(2),

        nn.Flatten(),

        nn.Linear(
            18432,
            256
        ),

        nn.ReLU(),

        nn.Dropout(0.5),

        nn.Linear(
            256,
            len(disease_classes)
        )

    )

    exact_features.load_state_dict(
        saved_state
    )

    disease_model = exact_features

    disease_model.eval()

    print(
        "✅ Plant disease CNN loaded."
    )

    print(
        f"✅ Disease classes: "
        f"{len(disease_classes)}"
    )


except Exception as error:

    disease_model = None

    print(
        "❌ Could not load plant disease CNN:"
    )

    print(error)


# ============================================================
# IMAGE TRANSFORMATION
# ============================================================

disease_transform = transforms.Compose([

    transforms.Resize(
        (96, 96)
    ),

    transforms.ToTensor()

])


# ============================================================
# DISEASE NAME FORMATTER
# ============================================================

def format_disease_name(
    disease_class
):

    parts = disease_class.split(
        "___"
    )

    if len(parts) == 2:

        plant = parts[0]

        disease = parts[1]

    else:

        plant = disease_class

        disease = "Unknown"


    plant = plant.replace(
        "_",
        " "
    )

    disease = disease.replace(
        "_",
        " "
    )

    disease = disease.strip()

    return plant, disease


# ============================================================
# DISEASE DETECTION
# ============================================================

@app.post("/predict-disease")
async def predict_disease(
    file: UploadFile = File(...)
):

    if disease_model is None:

        raise HTTPException(

            status_code=500,

            detail=(
                "Disease CNN model "
                "is not loaded."
            )

        )


    # --------------------------------------------------------
    # CHECK FILE
    # --------------------------------------------------------

    if not file.content_type:

        raise HTTPException(

            status_code=400,

            detail="Invalid image file."

        )


    if not file.content_type.startswith(
        "image/"
    ):

        raise HTTPException(

            status_code=400,

            detail=(
                "Please upload a "
                "valid plant leaf image."
            )

        )


    try:

        # ----------------------------------------------------
        # READ IMAGE
        # ----------------------------------------------------

        image_bytes = await file.read()

        image = Image.open(
            io.BytesIO(image_bytes)
        ).convert("RGB")


        # ----------------------------------------------------
        # TRANSFORM IMAGE
        # ----------------------------------------------------

        input_tensor = disease_transform(
            image
        )

        input_tensor = input_tensor.unsqueeze(
            0
        )


        # ----------------------------------------------------
        # CNN PREDICTION
        # ----------------------------------------------------

        with torch.no_grad():

            output = disease_model(
                input_tensor
            )

            probabilities = torch.softmax(
                output,
                dim=1
            )

            confidence, predicted_index = torch.max(
                probabilities,
                dim=1
            )


        predicted_index = (
            predicted_index.item()
        )

        confidence = (
            confidence.item()
        )


        # ----------------------------------------------------
        # GET CLASS
        # ----------------------------------------------------

        prediction = disease_classes[
            predicted_index
        ]


        # ----------------------------------------------------
        # FORMAT RESULT
        # ----------------------------------------------------

        plant, disease = format_disease_name(
            prediction
        )


        # ----------------------------------------------------
        # HEALTHY CHECK
        # ----------------------------------------------------

        is_healthy = (
            "healthy"
            in disease.lower()
        )


        return {

            "status": "success",

            "filename": file.filename,

            "prediction": prediction,

            "plant": plant,

            "condition": disease,

            "confidence": round(
                confidence * 100,
                2
            ),

            "healthy": is_healthy

        }


    except Exception as error:

        raise HTTPException(

            status_code=500,

            detail=(
                "Disease prediction failed: "
                + str(error)
            )

        )


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {

        "message":
        "Welcome to AgriMate API"

    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    return {

        "status":
        "AgriMate API is running"

    }


# ============================================================
# DISEASE MODEL STATUS
# ============================================================

@app.get("/disease-status")
def disease_status():

    return {

        "model_loaded":
        disease_model is not None,

        "classes":
        len(disease_classes)

    }