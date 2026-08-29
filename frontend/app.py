import streamlit as st

# ============================================================
# AgriMate - Home Page
# ============================================================

st.set_page_config(
    page_title="AgriMate",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.hero {
    text-align: center;
    padding: 30px 10px 20px 10px;
}

.hero-title {
    font-size: 55px;
    font-weight: bold;
}

.hero-subtitle {
    font-size: 24px;
    margin-top: 10px;
}

.feature-box {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #dddddd;
    min-height: 230px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🌱 AgriMate
</div>

<div class="hero-subtitle">
Smart Farming Assistant
</div>

</div>
""", unsafe_allow_html=True)


st.write(
    "AgriMate helps farmers make smarter decisions using "
    "Machine Learning, Artificial Intelligence and digital farming tools."
)

st.divider()


# ============================================================
# WELCOME
# ============================================================

st.header("👨‍🌾 Welcome to AgriMate")

st.write(
    "Choose a service below to get started."
)

st.divider()


# ============================================================
# FEATURES
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# CROP RECOMMENDATION
# ------------------------------------------------------------

with col1:

    st.markdown("""
    <div class="feature-box">

    <h2>🌾 Crop Recommendation</h2>

    <p>
    Enter soil and weather conditions and let AgriMate
    recommend a suitable crop using Machine Learning.
    </p>

    </div>
    """, unsafe_allow_html=True)

if st.button(
    "🌱 Open Crop Recommendation",
    use_container_width=True
):

    st.switch_page(
        "pages/1_🌾_Crop_Recommendation.py"
    )


# ------------------------------------------------------------
# DISEASE DETECTION
# ------------------------------------------------------------

with col2:

    st.markdown("""
    <div class="feature-box">

    <h2>🌿 Plant Disease Detection</h2>

    <p>
    Upload a plant leaf image and use our CNN model
    to detect possible plant diseases and view a treatment plan.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "📷 Open Disease Detection",
        use_container_width=True
    ):

        st.switch_page(
            "pages/3_🌿_Disease_Detection.py"
        )


st.write("")


col3, col4 = st.columns(2)


# ------------------------------------------------------------
# MARKETPLACE
# ------------------------------------------------------------

with col3:

    st.markdown("""
    <div class="feature-box">

    <h2>🛒 AgriMate Marketplace</h2>

    <p>
    Browse agricultural products including seeds,
    fertilizers, farming tools and irrigation equipment.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🛒 Open Marketplace",
        use_container_width=True
    ):

        st.switch_page(
            "pages/2_🛒_Marketplace.py"
        )


# ------------------------------------------------------------
# FARMING TOOLS
# ------------------------------------------------------------

with col4:

    st.markdown("""
    <div class="feature-box">

    <h2>🛠️ Farming Tools</h2>

    <p>
    Useful digital tools and resources for
    modern farming.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
    "🛠️ Open Farming Tools",
    use_container_width=True):

     st.switch_page(
        "pages/4_🛠️_Farming_Tools.py"
    )

# ============================================================
# PROJECT TECHNOLOGY
# ============================================================

st.divider()

st.header("🧠 Technology Behind AgriMate")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:

    st.metric(
        "🌾 Crop Model",
        "Random Forest"
    )

with tech2:

    st.metric(
        "🌿 Disease Model",
        "CNN"
    )

with tech3:

    st.metric(
        "⚡ Backend",
        "FastAPI"
    )

with tech4:

    st.metric(
        "🖥️ Frontend",
        "Streamlit"
    )


# ============================================================
# HOW AGRIMATE WORKS
# ============================================================

st.divider()

st.header("⚙️ How AgriMate Works")

step1, step2, step3 = st.columns(3)

with step1:

    st.markdown("""
    ### 1️⃣ Enter / Upload

    Enter soil and weather information
    or upload a plant leaf image.
    """)

with step2:

    st.markdown("""
    ### 2️⃣ AI Analysis

    AgriMate processes the information
    using Machine Learning and CNN models.
    """)

with step3:

    st.markdown("""
    ### 3️⃣ Get Results

    Receive crop recommendations,
    disease detection and treatment guidance.
    """)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgriMate • Smart Farming Assistant • "
    "Machine Learning & Deep Learning Based Agriculture Platform"
)