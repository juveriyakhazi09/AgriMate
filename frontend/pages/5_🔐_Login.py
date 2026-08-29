import streamlit as st
import json
import os
import re

# ============================================================
# AGRIMATE - LOGIN / SIGNUP
# ============================================================

st.set_page_config(
    page_title="AgriMate Login",
    page_icon="🔐",
    layout="centered"
)

# ============================================================
# USERS FILE
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

# ============================================================
# LOAD USERS
# ============================================================

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
# SAVE USERS
# ============================================================

def save_users(users):
    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            users,
            file,
            indent=4
        )


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
# HEADER
# ============================================================

st.title("🌱 AgriMate")

st.subheader("🔐 Farmer Login & Account")

st.write(
    "Login to access your AgriMate farming services."
)

st.divider()


# ============================================================
# LOGGED-IN USER
# ============================================================

if st.session_state.logged_in:

    users = load_users()

    email = st.session_state.user_email

    if email in users:

        user = users[email]

        st.success(
            f"Welcome back, {user['name']}! 👨‍🌾"
        )

        st.write(
            f"📧 Email: {email}"
        )

        st.divider()

        # ====================================================
        # AGRIMATE SERVICES
        # ====================================================

        st.header("🌾 AgriMate Services")

        st.write(
            "Choose a service to continue."
        )

        st.write("")

        # ====================================================
        # FARMER DASHBOARD
        # ====================================================

        if st.button(
            "📊 Farmer Dashboard",
            use_container_width=True,
            key="login_dashboard_button"
        ):

            st.switch_page(
                "pages/6_📊_Farmer_Dashboard.py"
            )

        st.write("")

        # ====================================================
        # TWO COLUMNS
        # ====================================================

        col1, col2 = st.columns(2)

        # ====================================================
        # LEFT COLUMN
        # ====================================================

        with col1:

            # ------------------------------------------------
            # CROP RECOMMENDATION
            # ------------------------------------------------

            if st.button(
                "🌱 Crop Recommendation",
                use_container_width=True,
                key="login_crop_button"
            ):

                st.switch_page(
                    "pages/1_🌾_Crop_Recommendation.py"
                )

            # ------------------------------------------------
            # DISEASE DETECTION
            # ------------------------------------------------

            if st.button(
                "🌿 Disease Detection",
                use_container_width=True,
                key="login_disease_button"
            ):

                st.switch_page(
                    "pages/3_🌿_Disease_Detection.py"
                )

        # ====================================================
        # RIGHT COLUMN
        # ====================================================

        with col2:

            # ------------------------------------------------
            # MARKETPLACE
            # ------------------------------------------------

            if st.button(
                "🛒 Marketplace",
                use_container_width=True,
                key="login_marketplace_button"
            ):

                st.switch_page(
                    "pages/2_🛒_Marketplace.py"
                )

            # ------------------------------------------------
            # FARMING TOOLS
            # ------------------------------------------------

            if st.button(
                "🛠️ Farming Tools",
                use_container_width=True,
                key="login_tools_button"
            ):

                st.switch_page(
                    "pages/4_🛠️_Farming_Tools.py"
                )

        # ====================================================
        # LOGOUT
        # ====================================================

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True,
            key="logout_button"
        ):

            st.session_state.logged_in = False
            st.session_state.user_email = ""

            st.rerun()

    else:

        st.error(
            "❌ User account could not be found."
        )

        st.session_state.logged_in = False
        st.session_state.user_email = ""

        st.rerun()


# ============================================================
# LOGIN / SIGNUP
# ============================================================

else:

    option = st.radio(
        "Select an option",
        [
            "🔐 Login",
            "📝 Sign Up"
        ],
        horizontal=True
    )

    # ========================================================
    # LOGIN
    # ========================================================

    if option == "🔐 Login":

        st.header("🔐 Login")

        email = st.text_input(
            "📧 Email",
            placeholder="example@gmail.com",
            key="login_email"
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        if st.button(
            "🔐 Login",
            use_container_width=True,
            key="login_button"
        ):

            email = email.strip().lower()

            # Reload latest users.json
            users = load_users()

            # ------------------------------------------------
            # VALIDATION
            # ------------------------------------------------

            if email == "":

                st.warning(
                    "⚠️ Please enter your email."
                )

            elif password == "":

                st.warning(
                    "⚠️ Please enter your password."
                )

            elif email not in users:

                st.error(
                    "❌ Account not found. "
                    "Please create an account first."
                )

            elif users[email]["password"] != password:

                st.error(
                    "❌ Incorrect password."
                )

            else:

                st.session_state.logged_in = True
                st.session_state.user_email = email

                st.success(
                    "✅ Login successful!"
                )

                st.rerun()

    # ========================================================
    # SIGN UP
    # ========================================================

    else:

        st.header("📝 Create Farmer Account")

        name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your full name",
            key="signup_name"
        )

        email = st.text_input(
            "📧 Email",
            placeholder="example@gmail.com",
            key="signup_email"
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Create a password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "🔑 Confirm Password",
            type="password",
            placeholder="Re-enter your password",
            key="signup_confirm_password"
        )

        if st.button(
            "📝 Create Account",
            use_container_width=True,
            key="signup_button"
        ):

            name = name.strip()
            email = email.strip().lower()

            # Reload latest database
            users = load_users()

            # ------------------------------------------------
            # VALIDATION
            # ------------------------------------------------

            if name == "":

                st.warning(
                    "⚠️ Please enter your name."
                )

            elif email == "":

                st.warning(
                    "⚠️ Please enter your email."
                )

            elif not re.match(
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
                email
            ):

                st.warning(
                    "⚠️ Please enter a valid email address."
                )

            elif password == "":

                st.warning(
                    "⚠️ Please create a password."
                )

            elif len(password) < 4:

                st.warning(
                    "⚠️ Password must contain at least 4 characters."
                )

            elif password != confirm_password:

                st.error(
                    "❌ Passwords do not match."
                )

            elif email in users:

                st.error(
                    "❌ This account already exists. "
                    "Please login instead."
                )

            else:

                # ------------------------------------------------
                # SAVE NEW USER
                # ------------------------------------------------

                users[email] = {
                    "name": name,
                    "password": password
                }

                save_users(users)

                # ------------------------------------------------
                # VERIFY SAVE
                # ------------------------------------------------

                saved_users = load_users()

                if email in saved_users:

                    st.success(
                        "✅ Account created successfully!"
                    )

                    st.info(
                        "Your account has been saved. "
                        "Select 🔐 Login and sign in."
                    )

                else:

                    st.error(
                        "❌ Account could not be saved."
                    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgriMate • Smart Farming Assistant • "
    "Machine Learning + Deep Learning"
)