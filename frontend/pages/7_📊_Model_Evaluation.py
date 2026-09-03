import streamlit as st
import pandas as pd
import json
from pathlib import Path
import matplotlib.pyplot as plt


# ============================================================
# AGRIMATE - MODEL EVALUATION
# ============================================================

st.set_page_config(
    page_title="Model Evaluation | AgriMate",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD EVALUATION RESULTS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESULTS_PATH = PROJECT_ROOT / "evaluation_results.json"


if not RESULTS_PATH.exists():
    st.error("❌ Evaluation results file not found.")

    st.info(
        "Run this command from C:\\AgriMate first:\n\n"
        "python evaluate_models.py"
    )

    st.stop()


with open(RESULTS_PATH, "r", encoding="utf-8") as file:
    results = json.load(file)


crop = results["crop"]
disease = results["disease"]


# ============================================================
# HEADER
# ============================================================

st.title("📊 AgriMate ML Model Evaluation")

st.markdown(
    """
    This page presents the performance evaluation of the machine
    learning models used in **AgriMate**.
    """
)

st.divider()


# ============================================================
# MODEL COMPARISON
# ============================================================

st.subheader("🤖 Model Performance Comparison")


comparison = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],

    "🌾 Crop Recommendation": [
        crop["accuracy"],
        crop["precision"],
        crop["recall"],
        crop["f1"]
    ],

    "🌿 Plant Disease Detection": [
        disease["accuracy"],
        disease["precision"],
        disease["recall"],
        disease["f1"]
    ]
})


display_comparison = comparison.copy()

display_comparison["🌾 Crop Recommendation"] = (
    display_comparison["🌾 Crop Recommendation"] * 100
).round(2).astype(str) + "%"

display_comparison["🌿 Plant Disease Detection"] = (
    display_comparison["🌿 Plant Disease Detection"] * 100
).round(2).astype(str) + "%"


st.dataframe(
    display_comparison,
    use_container_width=True,
    hide_index=True
)


st.divider()


# ============================================================
# CROP RECOMMENDATION MODEL
# ============================================================

st.header("🌾 Crop Recommendation Model")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{crop['accuracy'] * 100:.2f}%"
)

col2.metric(
    "Precision",
    f"{crop['precision'] * 100:.2f}%"
)

col3.metric(
    "Recall",
    f"{crop['recall'] * 100:.2f}%"
)

col4.metric(
    "F1 Score",
    f"{crop['f1'] * 100:.2f}%"
)


st.subheader("📋 Classification Report")

crop_report_data = {
    key: value
    for key, value in crop["classification_report"].items()
    if isinstance(value, dict)
}

crop_report = pd.DataFrame.from_dict(
    crop_report_data,
    orient="index"
)

crop_report = crop_report.round(3)

st.dataframe(
    crop_report,
    use_container_width=True
)


# ============================================================
# CROP CONFUSION MATRIX
# ============================================================

st.subheader("🔲 Confusion Matrix")

crop_cm = crop["confusion_matrix"]
crop_classes = crop["classes"]

fig, ax = plt.subplots(
    figsize=(12, 10)
)

image = ax.imshow(crop_cm)

ax.set_title("Crop Recommendation Confusion Matrix")

ax.set_xlabel("Predicted Class")
ax.set_ylabel("Actual Class")

ax.set_xticks(range(len(crop_classes)))
ax.set_yticks(range(len(crop_classes)))

ax.set_xticklabels(
    crop_classes,
    rotation=90,
    fontsize=8
)

ax.set_yticklabels(
    crop_classes,
    fontsize=8
)

fig.colorbar(image, ax=ax)

st.pyplot(fig)

plt.close(fig)


st.divider()


# ============================================================
# DISEASE DETECTION MODEL
# ============================================================

st.header("🌿 Plant Disease Detection CNN")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{disease['accuracy'] * 100:.2f}%"
)

col2.metric(
    "Precision",
    f"{disease['precision'] * 100:.2f}%"
)

col3.metric(
    "Recall",
    f"{disease['recall'] * 100:.2f}%"
)

col4.metric(
    "F1 Score",
    f"{disease['f1'] * 100:.2f}%"
)


# ============================================================
# DISEASE DATASET INFORMATION
# ============================================================

st.subheader("📚 Evaluation Dataset")

d1, d2, d3, d4 = st.columns(4)

d1.metric(
    "Total Dataset Images",
    "54,305"
)

d2.metric(
    "Images Evaluated",
    disease["images_used"]
)

d3.metric(
    "Training Images",
    disease["training_split"]
)

d4.metric(
    "Validation Images",
    disease["validation_split"]
)


st.subheader("📋 Classification Report")

disease_report_data = {
    key: value
    for key, value in disease["classification_report"].items()
    if isinstance(value, dict)
}

disease_report = pd.DataFrame.from_dict(
    disease_report_data,
    orient="index"
)

disease_report = disease_report.round(3)

st.dataframe(
    disease_report,
    use_container_width=True
)


# ============================================================
# DISEASE CONFUSION MATRIX
# ============================================================

st.subheader("🔲 Disease Detection Confusion Matrix")

disease_cm = disease["confusion_matrix"]
disease_classes = disease["classes"]

fig, ax = plt.subplots(
    figsize=(16, 14)
)

image = ax.imshow(disease_cm)

ax.set_title(
    "Plant Disease Detection Confusion Matrix"
)

ax.set_xlabel("Predicted Class")
ax.set_ylabel("Actual Class")

ax.set_xticks(range(len(disease_classes)))
ax.set_yticks(range(len(disease_classes)))

ax.set_xticklabels(
    disease_classes,
    rotation=90,
    fontsize=7
)

ax.set_yticklabels(
    disease_classes,
    fontsize=7
)

fig.colorbar(image, ax=ax)

st.pyplot(fig)

plt.close(fig)


# ============================================================
# INTERPRETATION
# ============================================================

st.divider()

st.header("📌 Evaluation Summary")

st.markdown(
    f"""
    ### 🌾 Crop Recommendation

    The Crop Recommendation model achieved an accuracy of
    **{crop['accuracy'] * 100:.2f}%**, with a weighted F1 score of
    **{crop['f1'] * 100:.2f}%** on the evaluation set.

    ### 🌿 Plant Disease Detection

    The Plant Disease Detection CNN achieved an accuracy of
    **{disease['accuracy'] * 100:.2f}%** and a weighted F1 score of
    **{disease['f1'] * 100:.2f}%**.

    The disease model has noticeably different performance across
    individual disease classes, so its overall accuracy should not
    be interpreted as equal reliability for every disease.
    """
)

st.success("✅ AgriMate model evaluation loaded successfully.")