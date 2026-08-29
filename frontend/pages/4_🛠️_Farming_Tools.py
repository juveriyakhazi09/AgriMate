import streamlit as st

# ============================================================
# AgriMate - Farming Tools
# ============================================================

st.set_page_config(
    page_title="AgriMate Farming Tools",
    page_icon="🛠️",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 25px;
    }

    .result-box {
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
    '<div class="title">🛠️ AgriMate Farming Tools</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart calculators for everyday farming decisions'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Use these tools to estimate field area, irrigation, "
    "fertilizer requirements and crop profitability."
)

st.divider()

# ============================================================
# TOOL SELECTION
# ============================================================

st.header("🌾 Select a Farming Tool")

tool = st.selectbox(
    "Choose a tool",
    [
        "📐 Land Area Calculator",
        "💧 Irrigation Water Calculator",
        "🧪 Fertilizer Calculator",
        "💰 Crop Profit Calculator"
    ]
)

st.divider()

# ============================================================
# 1. LAND AREA CALCULATOR
# ============================================================

if tool == "📐 Land Area Calculator":

    st.header("📐 Land Area Calculator")

    st.write(
        "Calculate your field area using length and width."
    )

    col1, col2 = st.columns(2)

    with col1:

        length = st.number_input(
            "Length (metres)",
            min_value=0.0,
            value=100.0,
            step=1.0
        )

    with col2:

        width = st.number_input(
            "Width (metres)",
            min_value=0.0,
            value=50.0,
            step=1.0
        )

    area_sq_m = length * width

    area_hectares = area_sq_m / 10000

    area_acres = area_sq_m / 4046.8564224

    st.subheader("📊 Result")

    result1, result2, result3 = st.columns(3)

    with result1:

        st.metric(
            "Square Metres",
            f"{area_sq_m:,.2f} m²"
        )

    with result2:

        st.metric(
            "Hectares",
            f"{area_hectares:.4f} ha"
        )

    with result3:

        st.metric(
            "Acres",
            f"{area_acres:.4f} acres"
        )

# ============================================================
# 2. IRRIGATION WATER CALCULATOR
# ============================================================

elif tool == "💧 Irrigation Water Calculator":

    st.header("💧 Irrigation Water Calculator")

    st.write(
        "Estimate the amount of water required for your field."
    )

    col1, col2 = st.columns(2)

    with col1:

        field_area = st.number_input(
            "Field Area (hectares)",
            min_value=0.01,
            value=1.0,
            step=0.1
        )

    with col2:

        water_depth = st.number_input(
            "Water Requirement (mm)",
            min_value=0.0,
            value=25.0,
            step=1.0
        )

    # 1 mm over 1 hectare = 10,000 litres

    water_litres = (
        field_area *
        water_depth *
        10000
    )

    water_cubic_m = water_litres / 1000

    st.subheader("📊 Irrigation Result")

    result1, result2 = st.columns(2)

    with result1:

        st.metric(
            "Water Required",
            f"{water_litres:,.0f} litres"
        )

    with result2:

        st.metric(
            "Water Required",
            f"{water_cubic_m:,.2f} m³"
        )

    st.info(
        "💧 Calculation used: "
        "1 mm water over 1 hectare ≈ 10,000 litres."
    )

# ============================================================
# 3. FERTILIZER CALCULATOR
# ============================================================

elif tool == "🧪 Fertilizer Calculator":

    st.header("🧪 Fertilizer Calculator")

    st.write(
        "Estimate fertilizer quantity based on application "
        "rate and field area."
    )

    col1, col2 = st.columns(2)

    with col1:

        fertilizer_area = st.number_input(
            "Field Area (hectares)",
            min_value=0.01,
            value=1.0,
            step=0.1
        )

    with col2:

        fertilizer_rate = st.number_input(
            "Fertilizer Rate (kg/hectare)",
            min_value=0.0,
            value=50.0,
            step=1.0
        )

    fertilizer_quantity = (
        fertilizer_area *
        fertilizer_rate
    )

    st.subheader("📊 Fertilizer Requirement")

    st.metric(
        "Total Fertilizer",
        f"{fertilizer_quantity:,.2f} kg"
    )

    st.info(
        "🧪 Use soil-test information and crop-specific "
        "recommendations whenever possible."
    )

# ============================================================
# 4. CROP PROFIT CALCULATOR
# ============================================================

elif tool == "💰 Crop Profit Calculator":

    st.header("💰 Crop Profit Calculator")

    st.write(
        "Estimate revenue, total cost and approximate profit."
    )

    col1, col2 = st.columns(2)

    with col1:

        profit_area = st.number_input(
            "Field Area (hectares)",
            min_value=0.01,
            value=1.0,
            step=0.1
        )

        yield_per_hectare = st.number_input(
            "Expected Yield (kg/hectare)",
            min_value=0.0,
            value=2500.0,
            step=100.0
        )

        selling_price = st.number_input(
            "Selling Price (₹/kg)",
            min_value=0.0,
            value=25.0,
            step=1.0
        )

    with col2:

        seed_cost = st.number_input(
            "Seed Cost (₹)",
            min_value=0.0,
            value=5000.0,
            step=500.0
        )

        fertilizer_cost = st.number_input(
            "Fertilizer Cost (₹)",
            min_value=0.0,
            value=8000.0,
            step=500.0
        )

        labour_cost = st.number_input(
            "Labour Cost (₹)",
            min_value=0.0,
            value=10000.0,
            step=500.0
        )

        irrigation_cost = st.number_input(
            "Irrigation Cost (₹)",
            min_value=0.0,
            value=5000.0,
            step=500.0
        )

        other_cost = st.number_input(
            "Other Costs (₹)",
            min_value=0.0,
            value=3000.0,
            step=500.0
        )

    # --------------------------------------------------------
    # CALCULATIONS
    # --------------------------------------------------------

    total_yield = (
        profit_area *
        yield_per_hectare
    )

    revenue = (
        total_yield *
        selling_price
    )

    total_cost = (
        seed_cost +
        fertilizer_cost +
        labour_cost +
        irrigation_cost +
        other_cost
    )

    profit = revenue - total_cost

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    st.subheader("📊 Profit Estimate")

    result1, result2, result3 = st.columns(3)

    with result1:

        st.metric(
            "Expected Yield",
            f"{total_yield:,.0f} kg"
        )

    with result2:

        st.metric(
            "Estimated Revenue",
            f"₹{revenue:,.2f}"
        )

    with result3:

        st.metric(
            "Total Cost",
            f"₹{total_cost:,.2f}"
        )

    st.divider()

    if profit > 0:

        st.success(
            f"💰 Estimated Profit: ₹{profit:,.2f}"
        )

    elif profit < 0:

        st.error(
            f"📉 Estimated Loss: ₹{abs(profit):,.2f}"
        )

    else:

        st.info(
            "⚖️ Estimated profit is ₹0."
        )

    st.info(
        "Profit = Revenue − Total Cost"
    )

# ============================================================
# QUICK FARMING REFERENCE
# ============================================================

st.divider()

st.header("📚 Quick Farming Reference")

ref1, ref2, ref3, ref4 = st.columns(4)

with ref1:

    st.subheader("📐 Area")

    st.write(
        "1 hectare = 10,000 square metres"
    )

    st.write(
        "1 hectare ≈ 2.47 acres"
    )

with ref2:

    st.subheader("💧 Water")

    st.write(
        "1 mm water over 1 hectare "
        "≈ 10,000 litres"
    )

with ref3:

    st.subheader("🧪 Fertilizer")

    st.write(
        "Use soil-test information whenever "
        "possible."
    )

with ref4:

    st.subheader("💰 Profit")

    st.write(
        "Profit = Revenue − Total Cost"
    )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgriMate • Smart Farming Tools • "
    "Agricultural Planning & Calculators"
)