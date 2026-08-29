import streamlit as st
import pandas as pd
import os
import requests

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AgriMate - Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# PATH
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "Crop_recommendation.csv"
)

# ============================================================
# CROP INFORMATION
# ============================================================

crop_info = {

    "rice": {
        "display": "Rice",
        "planting": "Rice seeds / seedlings",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Compost",
        "tools": "Hand Hoe + Farming Tools Set",
        "irrigation": "Flood irrigation or controlled irrigation",
        "water": "High",
        "fym_min": 15,
        "fym_max": 20,
        "management": [
            "Prepare and level the field properly.",
            "Use healthy seeds or seedlings.",
            "Maintain suitable water levels.",
            "Apply fertilizer according to soil and crop requirements.",
            "Monitor weeds, insects and diseases regularly."
        ]
    },

    "maize": {
        "display": "Maize",
        "planting": "Maize seeds",
        "fertilizers": "NPK Fertilizer + Urea Fertilizer + Organic Fertilizer",
        "tools": "Hand Hoe + Farming Tools Set",
        "irrigation": "Drip irrigation or sprinkler irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Prepare well-drained soil before planting.",
            "Use healthy and good-quality maize seeds.",
            "Maintain proper spacing between plants.",
            "Apply nitrogen and other nutrients according to soil needs.",
            "Control weeds and monitor pests regularly."
        ]
    },

    "cotton": {
        "display": "Cotton",
        "planting": "Cotton seeds",
        "fertilizers": "NPK Fertilizer + Urea Fertilizer + Organic Fertilizer",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Drip irrigation or controlled irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Prepare loose and well-drained soil.",
            "Use suitable quality cotton seeds.",
            "Maintain recommended plant spacing.",
            "Apply nutrients according to soil requirements.",
            "Monitor cotton pests and diseases regularly."
        ]
    },

    "banana": {
        "display": "Banana",
        "planting": "Banana suckers / healthy planting material",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Compost",
        "tools": "Hand Hoe + Spade",
        "irrigation": "Drip irrigation",
        "water": "High",
        "fym_min": 15,
        "fym_max": 20,
        "management": [
            "Select healthy planting material.",
            "Prepare fertile and well-drained soil.",
            "Provide regular irrigation.",
            "Apply organic manure and fertilizers as required.",
            "Remove damaged leaves and monitor pests."
        ]
    },

    "apple": {
        "display": "Apple",
        "planting": "Healthy apple saplings / grafted plants",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Compost",
        "tools": "Pruning Shears + Hand Hoe",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 20,
        "management": [
            "Select healthy and suitable planting material.",
            "Prepare fertile, well-drained soil.",
            "Provide irrigation according to weather and soil moisture.",
            "Prune plants appropriately.",
            "Monitor pests and diseases throughout the season."
        ]
    },

    "grapes": {
        "display": "Grapes",
        "planting": "Healthy grape cuttings / plants",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Vermicompost",
        "tools": "Pruning Shears + Farming Tools Set",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Use healthy planting material.",
            "Prepare fertile and well-drained soil.",
            "Install suitable support or trellis systems.",
            "Manage irrigation carefully.",
            "Prune and monitor plants for pests and diseases."
        ]
    },

    "mango": {
        "display": "Mango",
        "planting": "Grafted mango plants / healthy saplings",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Compost",
        "tools": "Pruning Shears + Hand Hoe",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 15,
        "fym_max": 20,
        "management": [
            "Plant healthy grafted saplings.",
            "Prepare well-drained soil.",
            "Provide irrigation during establishment and dry periods.",
            "Apply organic manure and fertilizers appropriately.",
            "Prune and monitor trees for pests and diseases."
        ]
    },

    "papaya": {
        "display": "Papaya",
        "planting": "Healthy papaya seedlings",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Vermicompost",
        "tools": "Hand Hoe + Spade",
        "irrigation": "Drip irrigation",
        "water": "Medium to High",
        "fym_min": 15,
        "fym_max": 20,
        "management": [
            "Use healthy papaya seedlings.",
            "Prepare fertile and well-drained soil.",
            "Avoid prolonged waterlogging.",
            "Apply nutrients according to soil and crop requirements.",
            "Monitor plants for pests and diseases."
        ]
    },

    "coconut": {
        "display": "Coconut",
        "planting": "Healthy coconut seedlings",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Compost",
        "tools": "Spade + Farming Tools Set",
        "irrigation": "Drip irrigation or basin irrigation",
        "water": "High",
        "fym_min": 15,
        "fym_max": 20,
        "management": [
            "Select healthy coconut seedlings.",
            "Prepare large planting pits with suitable soil.",
            "Provide regular irrigation during dry periods.",
            "Apply organic manure and fertilizers.",
            "Monitor palms for pests and diseases."
        ]
    },

    "coffee": {
        "display": "Coffee",
        "planting": "Healthy coffee seedlings",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Compost",
        "tools": "Hand Hoe + Pruning Shears",
        "irrigation": "Drip irrigation or controlled irrigation",
        "water": "Medium to High",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Use healthy coffee seedlings.",
            "Prepare fertile and well-drained soil.",
            "Maintain suitable soil moisture.",
            "Apply organic manure and fertilizers.",
            "Monitor coffee plants for pests and diseases."
        ]
    },

    "chickpea": {
        "display": "Chickpea",
        "planting": "Chickpea seeds",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Compost",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Controlled irrigation",
        "water": "Low to Medium",
        "fym_min": 8,
        "fym_max": 12,
        "management": [
            "Prepare well-drained soil.",
            "Use healthy chickpea seeds.",
            "Avoid excessive irrigation.",
            "Apply nutrients according to soil requirements.",
            "Monitor weeds and pod pests."
        ]
    },

    "kidneybeans": {
        "display": "Kidney Beans",
        "planting": "Kidney bean seeds",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Compost",
        "tools": "Hand Hoe + Farming Tools Set",
        "irrigation": "Drip irrigation or controlled irrigation",
        "water": "Medium",
        "fym_min": 8,
        "fym_max": 12,
        "management": [
            "Prepare loose and well-drained soil.",
            "Use quality seeds.",
            "Maintain proper plant spacing.",
            "Provide irrigation according to soil moisture.",
            "Control weeds and monitor diseases."
        ]
    },

    "lentil": {
        "display": "Lentil",
        "planting": "Lentil seeds",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Controlled irrigation",
        "water": "Low to Medium",
        "fym_min": 8,
        "fym_max": 12,
        "management": [
            "Prepare well-drained soil.",
            "Use healthy lentil seeds.",
            "Avoid excessive irrigation.",
            "Apply nutrients according to soil condition.",
            "Monitor weeds and diseases."
        ]
    },

    "blackgram": {
        "display": "Black Gram",
        "planting": "Black gram seeds",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Controlled irrigation",
        "water": "Low to Medium",
        "fym_min": 8,
        "fym_max": 12,
        "management": [
            "Prepare well-drained soil.",
            "Use good-quality seeds.",
            "Maintain suitable plant spacing.",
            "Avoid excessive watering.",
            "Monitor weeds, insects and diseases."
        ]
    },

    "mungbean": {
        "display": "Mung Bean",
        "planting": "Mung bean seeds",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Controlled irrigation",
        "water": "Low to Medium",
        "fym_min": 8,
        "fym_max": 12,
        "management": [
            "Prepare fertile and well-drained soil.",
            "Use healthy mung bean seeds.",
            "Maintain proper plant spacing.",
            "Provide irrigation based on soil moisture.",
            "Monitor weeds and pests."
        ]
    },

    "mothbeans": {
        "display": "Moth Beans",
        "planting": "Moth bean seeds",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Limited / controlled irrigation",
        "water": "Low",
        "fym_min": 5,
        "fym_max": 10,
        "management": [
            "Prepare suitable well-drained soil.",
            "Use quality seeds.",
            "Avoid excessive irrigation.",
            "Apply organic manure where required.",
            "Monitor weeds and pests."
        ]
    },

    "pigeonpeas": {
        "display": "Pigeon Peas",
        "planting": "Pigeon pea seeds",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Compost",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Controlled irrigation",
        "water": "Medium",
        "fym_min": 8,
        "fym_max": 12,
        "management": [
            "Prepare well-drained soil.",
            "Use healthy pigeon pea seeds.",
            "Maintain recommended spacing.",
            "Provide irrigation during critical growth periods.",
            "Monitor pests and diseases."
        ]
    },

    "jute": {
        "display": "Jute",
        "planting": "Jute seeds",
        "fertilizers": "NPK Fertilizer + Urea Fertilizer + Organic Fertilizer",
        "tools": "Hand Hoe + Agricultural Sickle",
        "irrigation": "Controlled irrigation",
        "water": "Medium to High",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Prepare fine soil for seed sowing.",
            "Use good-quality jute seeds.",
            "Maintain suitable soil moisture.",
            "Apply nutrients according to soil requirements.",
            "Control weeds during early growth."
        ]
    },

    "muskmelon": {
        "display": "Muskmelon",
        "planting": "Muskmelon seeds",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Vermicompost",
        "tools": "Hand Hoe + Hand Trowel",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Prepare fertile and well-drained soil.",
            "Use healthy seeds.",
            "Provide regular but controlled irrigation.",
            "Apply organic manure and fertilizers.",
            "Monitor fruits and plants for pests and diseases."
        ]
    },

    "watermelon": {
        "display": "Watermelon",
        "planting": "Watermelon seeds",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Vermicompost",
        "tools": "Hand Hoe + Hand Trowel",
        "irrigation": "Drip irrigation",
        "water": "Medium to High",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Prepare fertile, loose and well-drained soil.",
            "Use healthy watermelon seeds.",
            "Provide regular irrigation during growth.",
            "Reduce excessive watering near maturity.",
            "Monitor plants for pests and diseases."
        ]
    },

    "orange": {
        "display": "Orange",
        "planting": "Healthy orange grafted plants",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Compost",
        "tools": "Pruning Shears + Hand Hoe",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 20,
        "management": [
            "Use healthy grafted planting material.",
            "Prepare well-drained soil.",
            "Provide irrigation according to soil moisture.",
            "Apply organic manure and fertilizers.",
            "Monitor trees for pests and diseases."
        ]
    },

    "pomegranate": {
        "display": "Pomegranate",
        "planting": "Healthy pomegranate plants",
        "fertilizers": "Organic Fertilizer + NPK Fertilizer + Compost",
        "tools": "Pruning Shears + Hand Hoe",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 20,
        "management": [
            "Select healthy planting material.",
            "Prepare well-drained soil.",
            "Use controlled irrigation.",
            "Apply organic manure and fertilizers.",
            "Prune plants and monitor for pests and diseases."
        ]
    },

    "grapes": {
        "display": "Grapes",
        "planting": "Healthy grape cuttings / plants",
        "fertilizers": "NPK Fertilizer + Organic Fertilizer + Vermicompost",
        "tools": "Pruning Shears + Farming Tools Set",
        "irrigation": "Drip irrigation",
        "water": "Medium",
        "fym_min": 10,
        "fym_max": 15,
        "management": [
            "Use healthy planting material.",
            "Prepare fertile and well-drained soil.",
            "Provide proper support or trellis.",
            "Manage irrigation carefully.",
            "Prune plants and monitor diseases."
        ]
    }
}

# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_dataset():

    if not os.path.exists(DATASET_PATH):
        return None

    try:
        return pd.read_csv(DATASET_PATH)
    except Exception:
        return None


df = load_dataset()

# ============================================================
# CROP RECOMMENDATION FUNCTION
# ============================================================

def recommend_crop_from_dataset():

    if df is None:
        return None

    required_columns = [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall",
        "label"
    ]

    for column in required_columns:
        if column not in df.columns:
            return None

    # Find closest row in the dataset.
    values = df[
        [
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    ].copy()

    user_values = pd.DataFrame([[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        soil_ph,
        rainfall
    ]], columns=values.columns)

    # Normalize each feature so one measurement does not dominate.
    minimum = values.min()
    maximum = values.max()

    denominator = maximum - minimum
    denominator = denominator.replace(0, 1)

    normalized_values = (values - minimum) / denominator
    normalized_user = (user_values - minimum) / denominator

    distances = (
        (normalized_values - normalized_user.iloc[0]) ** 2
    ).sum(axis=1)

    nearest_index = distances.idxmin()

    return str(
        df.loc[nearest_index, "label"]
    ).strip().lower()


# ============================================================
# HEADER
# ============================================================

st.title("🌱 AgriMate")

st.subheader(
    "Smart Crop Recommendation & Farmer Assistant"
)

st.write(
    "Enter your soil and weather conditions. "
    "AgriMate will recommend a suitable crop and "
    "provide farming guidance."
)

st.divider()

# ============================================================
# SOIL AND WEATHER
# ============================================================

st.header("🌾 Soil & Weather Conditions")

col1, col2, col3 = st.columns(3)

with col1:

    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=200.0,
        value=50.0,
        step=1.0
    )

with col2:

    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=200.0,
        value=50.0,
        step=1.0
    )

with col3:

    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=250.0,
        value=50.0,
        step=1.0
    )

col1, col2, col3, col4 = st.columns(4)

with col1:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=25.0,
        step=0.5
    )

with col2:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

with col3:

    soil_ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1
    )

with col4:

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=1.0
    )

# ============================================================
# FARM INFORMATION
# ============================================================

st.divider()

st.header("📏 Farm Information")

area = st.number_input(
    "Field Area (hectares)",
    min_value=0.1,
    value=1.0,
    step=0.1
)

# ============================================================
# RECOMMEND BUTTON
# ============================================================

st.divider()

if st.button(
    "🌱 Recommend Best Crop",
    use_container_width=True,
    type="primary"
):

    with st.spinner(
        "Analyzing soil and weather conditions..."
    ):

        recommended_crop = recommend_crop_from_dataset()

        if recommended_crop is not None:

            st.session_state["recommended_crop"] = (
                recommended_crop
            )

            st.success(
                "Crop recommendation completed!"
            )

        else:

            st.error(
                "Unable to read Crop_recommendation.csv. "
                "Please check that the dataset is available."
            )

# ============================================================
# SHOW RECOMMENDATION
# ============================================================

if "recommended_crop" in st.session_state:

    crop_name = st.session_state["recommended_crop"]

    display_name = crop_name.title()

    st.divider()

    st.header("🌱 Recommended Crop")

    st.success(
        f"## 🌾 {display_name}"
    )

    st.write(
        "Based on the soil and weather conditions provided, "
        "this crop was recommended by the AgriMate Machine "
        "Learning model."
    )

    # ========================================================
    # FARMER ASSISTANT
    # ========================================================

    if crop_name in crop_info:

        info = crop_info[crop_name]

        st.divider()

        st.header("👨‍🌾 Farmer Assistant")

        st.write(
            f"Personalized farming guidance for **{display_name}**."
        )

        # ====================================================
        # WHAT CAN YOU GROW?
        # ====================================================

        st.subheader("🌱 What can you grow?")

        st.markdown(
            f"### 🌾 Recommended Crop"
        )

        st.markdown(
            f"## {info['display']}"
        )

        st.write(
            "This is the crop recommended by the "
            "AgriMate ML model."
        )

        # ====================================================
        # PLANTING OPTION
        # ====================================================

        st.subheader("🌱 Planting Option")

        st.markdown(
            f"### {info['planting']}"
        )

        st.write(
            "Depending on the crop, farmers may use seeds, "
            "seedlings or other suitable planting material."
        )

        # ====================================================
        # WHAT SHOULD YOU PURCHASE?
        # ====================================================

        st.subheader("🛒 What should you purchase?")

        purchase_col1, purchase_col2, purchase_col3 = st.columns(3)

        with purchase_col1:

            st.markdown("### 🌱 Seeds / Plants")

            st.write(
                f"**{info['planting']}**"
            )

        with purchase_col2:

            st.markdown("### 🧪 Fertilizer")

            st.write(
                f"**{info['fertilizers']}**"
            )

        with purchase_col3:

            st.markdown("### 🛠️ Farming Tools")

            st.write(
                f"**{info['tools']}**"
            )

        # ====================================================
        # FYM / GOBAR
        # ====================================================

        st.divider()

        st.subheader(
            "🐄 Gobar / FYM Requirement"
        )

        fym_min_total = info["fym_min"] * area
        fym_max_total = info["fym_max"] * area

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Field Area",
                f"{area:.1f} ha"
            )

        with col2:

            st.metric(
                "Minimum FYM",
                f"{fym_min_total:.1f} tonnes"
            )

        with col3:

            st.metric(
                "Maximum FYM",
                f"{fym_max_total:.1f} tonnes"
            )

        st.info(
            "This is an approximate planning estimate for "
            "farmyard manure (FYM/gobar). Actual requirements "
            "depend on soil condition, crop variety, farming "
            "method and local agricultural recommendations."
        )

        # ====================================================
        # IRRIGATION
        # ====================================================

        st.divider()

        st.subheader(
            "💧 Irrigation Recommendation"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Water Requirement",
                info["water"]
            )

        with col2:

            st.write(
                "**Recommended method:**"
            )

            st.write(
                info["irrigation"]
            )

        # ====================================================
        # CROP MANAGEMENT
        # ====================================================

        st.divider()

        st.subheader(
            "📋 Crop Management Plan"
        )

        for number, step in enumerate(
            info["management"],
            start=1
        ):

            st.write(
                f"**{number}.** {step}"
            )

        # ====================================================
        # MARKETPLACE
        # ====================================================

        st.divider()

        st.subheader(
            "🛒 Purchase Recommended Products"
        )

        st.write(
            f"Find products suitable for **{display_name}** "
            "including seeds, fertilizers, tools and "
            "irrigation equipment."
        )

        if st.button(
            "🛒 Open AgriMate Marketplace",
            use_container_width=True,
            key="open_marketplace"
        ):

            st.switch_page(
                "pages/2_🛒_Marketplace.py"
            )

    else:

        st.warning(
            f"Detailed Farmer Assistant information for "
            f"**{display_name}** has not yet been added."
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgriMate • Smart Farming Assistant • "
    "Machine Learning Based Crop Recommendation"
)