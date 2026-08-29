import streamlit as st
import json
import os

# ============================================================
# AGRIMATE - FARMER DASHBOARD
# ============================================================

st.set_page_config(
    page_title="AgriMate Dashboard",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# USER DATA
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

USERS_FILE = os.path.join(
    BASE_DIR,
    "users.json"
)


def load_users():

    if not os.path.exists(USERS_FILE):
        return {}

    try:

        with open(
            USERS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return {}


# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "cart" not in st.session_state:
    st.session_state.cart = []


# ============================================================
# CHECK LOGIN
# ============================================================

if not st.session_state.logged_in:

    st.warning(
        "🔐 Please login to access the Farmer Dashboard."
    )

    if st.button(
        "🔐 Go to Login",
        use_container_width=True
    ):

        st.switch_page(
            "pages/5_🔐_Login.py"
        )

    st.stop()


# ============================================================
# GET CURRENT USER
# ============================================================

users = load_users()

email = st.session_state.user_email

if email in users:

    user = users[email]

else:

    st.error(
        "❌ User account could not be found."
    )

    st.session_state.logged_in = False
    st.session_state.user_email = ""

    st.stop()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .dashboard-title {
        text-align: center;
        font-size: 46px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .dashboard-subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 25px;
    }

    .welcome-box {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">🌱 AgriMate</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Smart Farming Assistant Dashboard'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# WELCOME
# ============================================================

st.markdown(
    f"""
    <div class="welcome-box">

    <h2>👨‍🌾 Welcome, {user['name']}!</h2>

    <p>
    Your AgriMate farming assistant is ready to help you
    with crop selection, plant disease detection,
    agricultural products and farming calculations.
    </p>

    <p>
    📧 <b>{email}</b>
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# QUICK STATISTICS
# ============================================================

st.header("📊 Your AgriMate Overview")

stat1, stat2, stat3, stat4 = st.columns(4)


with stat1:

    st.metric(
        "🌾 Crop AI",
        "Available"
    )


with stat2:

    st.metric(
        "🌿 Disease CNN",
        "Available"
    )


with stat3:

    st.metric(
        "🛒 Cart Items",
        len(st.session_state.cart)
    )


with stat4:

    st.metric(
        "🛠️ Farming Tools",
        "4"
    )


st.divider()


# ============================================================
# AGRIMATE SERVICES
# ============================================================

st.header("🌾 AgriMate Services")

col1, col2 = st.columns(2)


# ============================================================
# CROP RECOMMENDATION
# ============================================================

with col1:

    st.subheader("🌱 Crop Recommendation")

    st.write(
        "Use soil nutrients, temperature, humidity, "
        "pH and rainfall to find a suitable crop."
    )

    if st.button(
        "🌱 Open Crop Recommendation",
        use_container_width=True,
        key="dashboard_crop"
    ):

        st.switch_page(
            "pages/1_🌾_Crop_Recommendation.py"
        )


# ============================================================
# DISEASE DETECTION
# ============================================================

with col2:

    st.subheader("🌿 Plant Disease Detection")

    st.write(
        "Upload a plant leaf image and use the CNN "
        "model to detect a possible plant condition."
    )

    if st.button(
        "🌿 Open Disease Detection",
        use_container_width=True,
        key="dashboard_disease"
    ):

        st.switch_page(
            "pages/3_🌿_Disease_Detection.py"
        )


st.write("")


col3, col4 = st.columns(2)


# ============================================================
# MARKETPLACE
# ============================================================

with col3:

    st.subheader("🛒 AgriMate Marketplace")

    st.write(
        "Find seeds, plants, fertilizers, farming tools "
        "and irrigation equipment."
    )

    if st.button(
        "🛒 Open Marketplace",
        use_container_width=True,
        key="dashboard_marketplace"
    ):

        st.switch_page(
            "pages/2_🛒_Marketplace.py"
        )


# ============================================================
# FARMING TOOLS
# ============================================================

with col4:

    st.subheader("🛠️ Farming Tools")

    st.write(
        "Calculate land area, irrigation water, "
        "fertilizer requirements and crop profit."
    )

    if st.button(
        "🛠️ Open Farming Tools",
        use_container_width=True,
        key="dashboard_tools"
    ):

        st.switch_page(
            "pages/4_🛠️_Farming_Tools.py"
        )


# ============================================================
# CART SUMMARY
# ============================================================

st.divider()

st.header("🛒 Your Shopping Cart")

if len(st.session_state.cart) == 0:

    st.info(
        "Your cart is currently empty."
    )

else:

    total = 0

    for item in st.session_state.cart:

        total += item["price"]

        st.write(
            f"🌱 **{item['name']}** — "
            f"₹{item['price']}"
        )

    st.divider()

    st.subheader(
        f"💰 Cart Total: ₹{total:,.2f}"
    )

    if st.button(
        "🛒 Open Marketplace",
        use_container_width=True,
        key="dashboard_cart"
    ):

        st.switch_page(
            "pages/2_🛒_Marketplace.py"
        )


# ============================================================
# FARMING AI INFORMATION
# ============================================================

st.divider()

st.header("🧠 AI Technology")

ai1, ai2, ai3 = st.columns(3)


with ai1:

    st.subheader("🌾 Machine Learning")

    st.write(
        "Random Forest is used for crop recommendation "
        "based on soil and weather conditions."
    )


with ai2:

    st.subheader("🌿 Deep Learning")

    st.write(
        "CNN technology is used for plant disease "
        "image classification."
    )


with ai3:

    st.subheader("⚡ FastAPI")

    st.write(
        "FastAPI provides the backend API services "
        "for AgriMate machine learning predictions."
    )


# ============================================================
# PROJECT STATUS
# ============================================================

st.divider()

st.header("✅ AgriMate System Status")

status1, status2 = st.columns(2)


with status1:

    st.write(
        "🟢 **Crop Recommendation** — Working"
    )

    st.write(
        "🟢 **Plant Disease Detection** — Working"
    )

    st.write(
        "🟢 **Disease Management Guidance** — Working"
    )


with status2:

    st.write(
        "🟢 **Marketplace** — Working"
    )

    st.write(
        "🟢 **Farming Tools** — Working"
    )

    st.write(
        "🟢 **Login / Signup** — Working"
    )


# ============================================================
# QUICK NAVIGATION
# ============================================================

st.divider()

st.header("🧭 Quick Navigation")

nav1, nav2, nav3, nav4 = st.columns(4)


with nav1:

    if st.button(
        "🌱 Crop",
        use_container_width=True,
        key="nav_crop"
    ):

        st.switch_page(
            "pages/1_🌾_Crop_Recommendation.py"
        )


with nav2:

    if st.button(
        "🌿 Disease",
        use_container_width=True,
        key="nav_disease"
    ):

        st.switch_page(
            "pages/3_🌿_Disease_Detection.py"
        )


with nav3:

    if st.button(
        "🛒 Marketplace",
        use_container_width=True,
        key="nav_marketplace"
    ):

        st.switch_page(
            "pages/2_🛒_Marketplace.py"
        )


with nav4:

    if st.button(
        "🛠️ Tools",
        use_container_width=True,
        key="nav_tools"
    ):

        st.switch_page(
            "pages/4_🛠️_Farming_Tools.py"
        )


# ============================================================
# LOGOUT
# ============================================================

st.divider()

if st.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state.logged_in = False
    st.session_state.user_email = ""

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgriMate • Smart Farming Assistant • "
    "Machine Learning + Deep Learning"
)