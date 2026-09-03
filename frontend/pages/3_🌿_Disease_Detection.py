import streamlit as st
import requests
from PIL import Image


# ============================================================
# AGRIMATE - PLANT DISEASE DETECTION
# ============================================================

st.set_page_config(
    page_title="AgriMate Disease Detection",
    page_icon="🌿",
    layout="wide"
)


# ============================================================
# DISEASE API
# ============================================================

DISEASE_API_URL = "https://agrimate-api-0n4y.onrender.com"


# ============================================================
# IMAGE PROCESSING
# ============================================================

def make_small_jpeg(uploaded_file):
    """Resize and compress uploaded image."""

    from io import BytesIO

    image = Image.open(uploaded_file).convert("RGB")

    image.thumbnail(
        (768, 768),
        Image.Resampling.LANCZOS
    )

    buffer = BytesIO()

    image.save(
        buffer,
        format="JPEG",
        quality=85,
        optimize=True
    )

    return buffer.getvalue()

# ============================================================
# WAKE DISEASE API
# ============================================================

def wake_disease_api():
    try:
        response = requests.get(
            f"{DISEASE_API_URL}/health",
            timeout=90
        )

        return response.status_code == 200

    except requests.exceptions.Timeout:
        return False

    except requests.exceptions.RequestException:
        return False

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 22px;
        margin-bottom: 25px;
    }

    .result-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #dddddd;
    }

    .assistant-box {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-top: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🌿 AgriMate</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Plant Disease Detection</div>',
    unsafe_allow_html=True
)

st.write(
    "Upload a plant leaf image and AgriMate will use "
    "a CNN model to predict the possible plant condition."
)

st.divider()


# ============================================================
# IMAGE UPLOAD
# ============================================================

st.header("📷 Upload Leaf Image")

uploaded_file = st.file_uploader(
    "Choose a plant leaf image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# DISEASE INFORMATION
# ============================================================

disease_info = {

    "Corn (maize) Northern Leaf Blight": {
        "plant": "Corn (maize)",
        "condition": "Northern Leaf Blight",
        "steps": [
            "🌱 Use corn hybrids with good resistance to Northern Leaf Blight.",
            "🔍 Scout the crop regularly for new or increasing leaf lesions.",
            "🌾 Practice crop rotation where practical.",
            "🌿 Manage infected corn residue to reduce disease carryover.",
            "💧 Avoid unnecessarily prolonged leaf wetness where irrigation is used.",
            "🧪 If disease pressure is significant, consult a local agricultural expert about an appropriate foliar fungicide."
        ]
    },

    "Corn (maize) Common Rust": {
        "plant": "Corn (maize)",
        "condition": "Common Rust",
        "steps": [
            "🔍 Monitor leaves regularly for rust-colored pustules.",
            "🌱 Use resistant or tolerant hybrids where available.",
            "🌾 Maintain good crop management and field sanitation.",
            "💧 Avoid unnecessarily prolonged leaf wetness.",
            "🧪 Consult a local agricultural expert if disease pressure becomes significant."
        ]
    },

    "Potato Early Blight": {
        "plant": "Potato",
        "condition": "Early Blight",
        "steps": [
            "🔍 Inspect lower leaves regularly for dark lesions.",
            "🌱 Use healthy planting material.",
            "🌾 Practice crop rotation where practical.",
            "🌿 Remove severely infected plant material where appropriate.",
            "💧 Avoid prolonged leaf wetness.",
            "🧪 Consult a local agricultural expert for suitable disease management."
        ]
    },

    "Potato Late Blight": {
        "plant": "Potato",
        "condition": "Late Blight",
        "steps": [
            "🔍 Monitor the crop frequently for rapidly developing leaf lesions.",
            "🌱 Use healthy planting material.",
            "🌾 Remove severely infected material where appropriate.",
            "💧 Avoid unnecessary prolonged leaf wetness.",
            "🌿 Maintain good field sanitation.",
            "🧪 Seek local agricultural advice for appropriate disease-control measures."
        ]
    },

    "Tomato Early Blight": {
        "plant": "Tomato",
        "condition": "Early Blight",
        "steps": [
            "🔍 Inspect leaves regularly for dark circular lesions.",
            "🌱 Use healthy seedlings.",
            "🌾 Practice crop rotation where practical.",
            "🌿 Remove severely affected leaves where appropriate.",
            "💧 Avoid unnecessary prolonged leaf wetness.",
            "🧪 Consult a local agricultural expert for suitable treatment."
        ]
    },

    "Tomato Late Blight": {
        "plant": "Tomato",
        "condition": "Late Blight",
        "steps": [
            "🔍 Monitor plants regularly for dark water-soaked lesions.",
            "🌱 Use healthy planting material.",
            "🌿 Remove severely affected material where appropriate.",
            "💧 Improve air circulation and avoid unnecessary leaf wetness.",
            "🌾 Maintain good field sanitation.",
            "🧪 Consult a local agricultural expert for appropriate management."
        ]
    },

    "Tomato Bacterial Spot": {
        "plant": "Tomato",
        "condition": "Bacterial Spot",
        "steps": [
            "🔍 Monitor leaves and fruits for small dark spots.",
            "🌱 Use healthy certified planting material.",
            "💧 Avoid unnecessary overhead irrigation.",
            "🌿 Remove severely affected plant material where appropriate.",
            "🌾 Maintain field sanitation.",
            "👨‍🌾 Consult a local agricultural expert for confirmation and management."
        ]
    }
}


# ============================================================
# UPLOAD PROCESS
# ============================================================

if uploaded_file is not None:

    # ========================================================
    # DISPLAY IMAGE
    # ========================================================

    st.divider()

    st.header("🖼️ Uploaded Image")

    try:

        uploaded_file.seek(0)

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Selected plant leaf",
            use_container_width=True
        )

    except Exception as error:

        st.error(
            "❌ Could not open the uploaded image."
        )

        st.code(str(error))

        st.stop()


    # ========================================================
    # DETECT DISEASE BUTTON
    # ========================================================

    st.divider()

    detect_button = st.button(
        "🔍 Detect Plant Disease",
        use_container_width=True,
        type="primary"
    )


    if detect_button:

        with st.spinner(
            "Analyzing the leaf image using the CNN model..."
        ):

            try:

                # =================================================
                # PREPARE IMAGE
                # =================================================

                uploaded_file.seek(0)

                image_bytes = make_small_jpeg(
                    uploaded_file
                )


                # =================================================
                # PREPARE REQUEST
                # =================================================

                files = {
                    "file": (
                        "leaf.jpg",
                        image_bytes,
                        "image/jpeg"
                    )
                }


                # =================================================
                # WAKE RENDER BACKEND
                # =================================================

                api_awake = wake_disease_api()

                if not api_awake:
                    st.error(
                        "⏱️ The AI server is waking up. "
                        "Please click Detect Plant Disease again."
                    )
                    st.stop()


                # =================================================
                # SEND IMAGE TO FASTAPI
                # =================================================

                response = requests.post(
                    f"{DISEASE_API_URL}/predict-disease",
                    files=files,
                    timeout=90
                    )


                # =================================================
                # SUCCESS
                # =================================================

                if response.status_code == 200:

                    result = response.json()


                    # =================================================
                    # GET PREDICTION
                    # =================================================

                    prediction = result.get(
                        "prediction",
                        result.get(
                            "disease",
                            result.get(
                                "class",
                                result.get(
                                    "predicted_class",
                                    ""
                                )
                            )
                        )
                    )


                    # =================================================
                    # GET CONFIDENCE
                    # =================================================

                    confidence = result.get(
                        "confidence",
                        result.get(
                            "probability",
                            0
                        )
                    )


                    # =================================================
                    # CHECK PREDICTION
                    # =================================================

                    if not prediction:

                        st.error(
                            "❌ The disease detection API "
                            "did not return a prediction."
                        )

                        st.json(result)

                    else:

                        prediction = str(
                            prediction
                        ).strip()


                        # =================================================
                        # FORMAT DISEASE NAME
                        # =================================================

                        display_prediction = (
                            prediction
                            .replace(
                                "___",
                                " — "
                            )
                            .replace(
                                "_",
                                " "
                            )
                        )


                        # =================================================
                        # FORMAT CONFIDENCE
                        # =================================================

                        try:

                            confidence_value = float(
                                confidence
                            )

                            if confidence_value <= 1:

                                confidence_percent = (
                                    confidence_value * 100
                                )

                            else:

                                confidence_percent = (
                                    confidence_value
                                )

                        except Exception:

                            confidence_percent = 0.0


                        # =================================================
                        # SAVE RESULT
                        # =================================================

                        st.session_state[
                            "disease_prediction"
                        ] = prediction

                        st.session_state[
                            "disease_confidence"
                        ] = confidence_percent


                        # =================================================
                        # DISPLAY SUCCESS
                        # =================================================

                        st.success(
                            "✅ Disease detection completed!"
                        )

                        st.divider()

                        st.header(
                            "🌱 Prediction"
                        )

                        st.markdown(
                            f"""
                            <div class="result-box">

                            <h2>🌿 Plant Condition</h2>

                            <h1>{display_prediction}</h1>

                            <p>
                            <strong>
                            Prediction Confidence
                            </strong>
                            </p>

                            <h2>
                            {confidence_percent:.2f}%
                            </h2>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )


                        # =================================================
                        # DISEASE INFORMATION MATCHING
                        # =================================================

                        matched_info = None

                        normalized_prediction = (
                            prediction
                            .lower()
                            .replace(
                                "___",
                                " "
                            )
                            .replace(
                                "_",
                                " "
                            )
                            .replace(
                                "-",
                                " "
                            )
                            .strip()
                        )


                        prediction_words = set(
                            normalized_prediction.split()
                        )


                        for disease_name, info in disease_info.items():

                            normalized_name = (
                                disease_name
                                .lower()
                                .replace(
                                    "___",
                                    " "
                                )
                                .replace(
                                    "_",
                                    " "
                                )
                                .replace(
                                    "-",
                                    " "
                                )
                                .strip()
                            )


                            disease_words = set(
                                normalized_name.split()
                            )


                            if (
                                normalized_prediction
                                == normalized_name
                                or
                                normalized_name
                                in normalized_prediction
                                or
                                normalized_prediction
                                in normalized_name
                                or
                                disease_words.issubset(
                                    prediction_words
                                )
                            ):

                                matched_info = info

                                break


                        # =================================================
                        # KNOWN DISEASE
                        # =================================================

                        if matched_info:

                            st.divider()

                            st.header(
                                "🌱 Plant"
                            )

                            st.write(
                                f"**{matched_info['plant']}**"
                            )


                            st.header(
                                "🦠 Condition"
                            )

                            st.write(
                                f"**{matched_info['condition']}**"
                            )


                            st.success(
                                "✅ A treatment plan is available "
                                "for this detected condition."
                            )


                            # =================================================
                            # TREATMENT
                            # =================================================

                            st.divider()

                            st.header(
                                "🩺 Treatment Plan"
                            )

                            st.subheader(
                                "🌱 Recommended Management Steps"
                            )


                            for number, step in enumerate(
                                matched_info["steps"],
                                start=1
                            ):

                                st.write(
                                    f"**{number}.** {step}"
                                )

                        # =================================================
                        # UNKNOWN DISEASE
                        # =================================================

                        else:

                            st.divider()

                            st.subheader(
                                "🌱 General Management"
                            )


                            st.write(
                                "1. 🔍 Inspect the plant carefully "
                                "and confirm symptoms."
                            )

                            st.write(
                                "2. 🌿 Remove severely affected "
                                "plant material where appropriate."
                            )

                            st.write(
                                "3. 💧 Avoid unnecessary prolonged "
                                "leaf wetness."
                            )

                            st.write(
                                "4. 🌱 Maintain suitable irrigation "
                                "and plant nutrition."
                            )

                            st.write(
                                "5. 🔎 Monitor nearby plants for "
                                "similar symptoms."
                            )

                            st.write(
                                "6. 👨‍🌾 Consult a local agricultural "
                                "expert for confirmation and "
                                "specific treatment."
                            )

                # =================================================
                # API ERROR
                # =================================================

                else:

                    st.error(
                        "❌ The AgriMate disease detection API "
                        "returned an error."
                    )

                    st.code(
                        response.text
                    )


            # ====================================================
            # CONNECTION ERROR
            # ====================================================

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Cannot connect to the AgriMate backend."
                )

                st.info(
                    "Make sure the FastAPI backend is running."
                )


            # ====================================================
            # TIMEOUT
            # ====================================================

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ The AI server took too long to respond."
                )

                st.info(
                    "Please wait and try again."
                )


            # ====================================================
            # OTHER ERROR
            # ====================================================

            except Exception as error:

                st.error(
                    "❌ Error while predicting the disease."
                )

                st.code(
                    str(error)
                )


# ============================================================
# MARKETPLACE
# ============================================================

st.divider()

st.header(
    "🛒 Purchase Farming Products"
)

st.write(
    "Find seeds, fertilizers, farming tools and irrigation "
    "equipment for your farming needs."
)

if st.button(
    "🛒 Open AgriMate Marketplace",
    use_container_width=True
):

    st.switch_page(
        "pages/2_🛒_Marketplace.py"
    )


# ============================================================
# FARMING TOOLS
# ============================================================

st.divider()

st.header(
    "🛠️ Farming Tools"
)

st.write(
    "Use AgriMate farming calculators and tools."
)

if st.button(
    "🛠️ Open Farming Tools",
    use_container_width=True
):

    st.switch_page(
        "pages/4_🛠️_Farming_Tools.py"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgriMate • CNN-Based Plant Disease Detection • "
    "Smart Farming Assistant"
)