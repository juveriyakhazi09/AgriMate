import streamlit as st


# ============================================================
# AGRIMATE - ENTRY POINT
# ============================================================

st.set_page_config(
    page_title="AgriMate",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ============================================================
# OPEN AGRIMATE
# ============================================================

if not st.session_state.logged_in:

    st.switch_page(
        "pages/5_🔐_Login.py"
    )

else:

    st.switch_page(
        "pages/6_📊_Farmer_Dashboard.py"
    )