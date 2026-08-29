import streamlit as st

# ============================================================
# AGRIMATE - MARKETPLACE
# ============================================================

st.set_page_config(
    page_title="AgriMate Marketplace",
    page_icon="🛒",
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

.product-card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #dddddd;
    margin-bottom: 15px;
    min-height: 300px;
}

.price {
    font-size: 25px;
    font-weight: bold;
}

.rating {
    font-size: 18px;
}

.stock {
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PRODUCT DATABASE
# ============================================================

products = [

    # ========================================================
    # SEEDS
    # ========================================================

    {
        "name": "Rice Seeds",
        "category": "Seeds",
        "description": "Quality rice seeds for farming.",
        "price": 180
    },

    {
        "name": "Wheat Seeds",
        "category": "Seeds",
        "description": "Quality wheat seeds suitable for cultivation.",
        "price": 200
    },

    {
        "name": "Maize Seeds",
        "category": "Seeds",
        "description": "Healthy maize seeds for good crop production.",
        "price": 160
    },

    {
        "name": "Chickpea Seeds",
        "category": "Seeds",
        "description": "Quality chickpea seeds for cultivation.",
        "price": 180
    },

    {
        "name": "Kidney Bean Seeds",
        "category": "Seeds",
        "description": "Quality kidney bean seeds.",
        "price": 190
    },

    {
        "name": "Pigeon Pea Seeds",
        "category": "Seeds",
        "description": "Healthy pigeon pea seeds.",
        "price": 180
    },

    {
        "name": "Moth Bean Seeds",
        "category": "Seeds",
        "description": "Quality moth bean seeds.",
        "price": 170
    },

    {
        "name": "Mung Bean Seeds",
        "category": "Seeds",
        "description": "Quality mung bean seeds.",
        "price": 170
    },

    {
        "name": "Black Gram Seeds",
        "category": "Seeds",
        "description": "Quality black gram seeds.",
        "price": 175
    },

    {
        "name": "Lentil Seeds",
        "category": "Seeds",
        "description": "Quality lentil seeds.",
        "price": 180
    },

    {
        "name": "Cotton Seeds",
        "category": "Seeds",
        "description": "Quality cotton seeds for commercial cultivation.",
        "price": 350
    },

    {
        "name": "Jute Seeds",
        "category": "Seeds",
        "description": "Quality jute seeds.",
        "price": 160
    },

    {
        "name": "Watermelon Seeds",
        "category": "Seeds",
        "description": "Quality watermelon seeds.",
        "price": 150
    },

    {
        "name": "Muskmelon Seeds",
        "category": "Seeds",
        "description": "Quality muskmelon seeds.",
        "price": 150
    },

    # ========================================================
    # PLANTS
    # ========================================================

    {
        "name": "Apple Plants",
        "category": "Plants",
        "description": "Grafted apple planting material.",
        "price": 250
    },

    {
        "name": "Banana Plants",
        "category": "Plants",
        "description": "Healthy banana planting material.",
        "price": 80
    },

    {
        "name": "Mango Plants",
        "category": "Plants",
        "description": "Grafted mango planting material.",
        "price": 300
    },

    {
        "name": "Orange Plants",
        "category": "Plants",
        "description": "Grafted orange planting material.",
        "price": 250
    },

    {
        "name": "Papaya Plants",
        "category": "Plants",
        "description": "Healthy papaya seedlings.",
        "price": 60
    },

    {
        "name": "Pomegranate Plants",
        "category": "Plants",
        "description": "Healthy pomegranate planting material.",
        "price": 250
    },

    {
        "name": "Coconut Plants",
        "category": "Plants",
        "description": "Healthy coconut seedlings.",
        "price": 200
    },

    {
        "name": "Coffee Plants",
        "category": "Plants",
        "description": "Healthy coffee seedlings.",
        "price": 120
    },

    {
        "name": "Grape Plants",
        "category": "Plants",
        "description": "Healthy grape planting material.",
        "price": 180
    },

    # ========================================================
    # FERTILIZERS
    # ========================================================

    {
        "name": "Organic Fertilizer",
        "category": "Fertilizers",
        "description": "Organic fertilizer for healthy crop growth.",
        "price": 450
    },

    {
        "name": "NPK Fertilizer",
        "category": "Fertilizers",
        "description": "Balanced NPK fertilizer for crop nutrition.",
        "price": 550
    },

    {
        "name": "Urea Fertilizer",
        "category": "Fertilizers",
        "description": "Nitrogen-rich fertilizer supporting plant growth.",
        "price": 320
    },

    {
        "name": "DAP Fertilizer",
        "category": "Fertilizers",
        "description": "DAP fertilizer providing nitrogen and phosphorus.",
        "price": 600
    },

    {
        "name": "Compost",
        "category": "Fertilizers",
        "description": "Natural compost for improving soil quality.",
        "price": 300
    },

    {
        "name": "Vermicompost",
        "category": "Fertilizers",
        "description": "Nutrient-rich organic fertilizer.",
        "price": 380
    },

    {
        "name": "Potash Fertilizer",
        "category": "Fertilizers",
        "description": "Potassium fertilizer supporting crop strength.",
        "price": 500
    },

    {
        "name": "Neem Cake Fertilizer",
        "category": "Fertilizers",
        "description": "Organic fertilizer for soil improvement.",
        "price": 350
    },

    # ========================================================
    # FARMING TOOLS
    # ========================================================

    {
        "name": "Farming Tools Set",
        "category": "Farming Tools",
        "description": "Essential tools for everyday farming.",
        "price": 750
    },

    {
        "name": "Hand Hoe",
        "category": "Farming Tools",
        "description": "Durable hand hoe for soil preparation.",
        "price": 350
    },

    {
        "name": "Spade",
        "category": "Farming Tools",
        "description": "Strong spade for digging and soil preparation.",
        "price": 450
    },

    {
        "name": "Hand Cultivator",
        "category": "Farming Tools",
        "description": "Useful tool for loosening soil.",
        "price": 280
    },

    {
        "name": "Pruning Shears",
        "category": "Farming Tools",
        "description": "Sharp pruning shears for trimming plants.",
        "price": 300
    },

    {
        "name": "Garden Rake",
        "category": "Farming Tools",
        "description": "Rake for collecting leaves and preparing soil.",
        "price": 400
    },

    {
        "name": "Agricultural Sickle",
        "category": "Farming Tools",
        "description": "Traditional tool for harvesting crops.",
        "price": 250
    },

    {
        "name": "Hand Trowel",
        "category": "Farming Tools",
        "description": "Small tool for planting and soil work.",
        "price": 180
    },

    {
        "name": "Garden Fork",
        "category": "Farming Tools",
        "description": "Strong fork for turning and loosening soil.",
        "price": 420
    },

    {
        "name": "Weeding Tool",
        "category": "Farming Tools",
        "description": "Tool designed for removing weeds.",
        "price": 220
    },

    # ========================================================
    # IRRIGATION
    # ========================================================

    {
        "name": "Drip Irrigation Kit",
        "category": "Irrigation",
        "description": "Efficient irrigation system for saving water.",
        "price": 1200
    },

    {
        "name": "Water Sprinkler",
        "category": "Irrigation",
        "description": "Sprinkler system for efficient watering.",
        "price": 850
    },

    {
        "name": "Drip Irrigation Pipe",
        "category": "Irrigation",
        "description": "Durable pipe for drip irrigation.",
        "price": 950
    },

    {
        "name": "Water Pump",
        "category": "Irrigation",
        "description": "Water pump for agricultural irrigation.",
        "price": 4500
    },

    {
        "name": "Sprinkler Pipe Set",
        "category": "Irrigation",
        "description": "Pipe set for sprinkler irrigation.",
        "price": 1400
    },

    {
        "name": "Water Storage Tank",
        "category": "Irrigation",
        "description": "Storage tank for irrigation water.",
        "price": 3500
    },

    {
        "name": "Drip Emitter Set",
        "category": "Irrigation",
        "description": "Emitters for controlled water delivery.",
        "price": 600
    },

    {
        "name": "Irrigation Filter",
        "category": "Irrigation",
        "description": "Filter for irrigation systems.",
        "price": 700
    },

    {
        "name": "Garden Hose",
        "category": "Irrigation",
        "description": "Flexible hose for watering.",
        "price": 500
    },

    {
        "name": "Spray Nozzle",
        "category": "Irrigation",
        "description": "Adjustable nozzle for water spraying.",
        "price": 250
    }
]


# ============================================================
# ADD DEFAULT MARKETPLACE DETAILS
# ============================================================

for product in products:

    product["rating"] = 4.5
    product["stock"] = 50


# ============================================================
# CROP PRODUCT RECOMMENDATIONS
# ============================================================

crop_products = {

    "rice": {
        "Seeds": ["Rice Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Water Pump",
            "Water Sprinkler"
        ]
    },

    "wheat": {
        "Seeds": ["Wheat Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Urea Fertilizer",
            "DAP Fertilizer"
        ],
        "Farming Tools": [
            "Farming Tools Set",
            "Agricultural Sickle"
        ],
        "Irrigation": [
            "Water Pump",
            "Drip Irrigation Kit"
        ]
    },

    "maize": {
        "Seeds": ["Maize Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Urea Fertilizer",
            "Organic Fertilizer"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Sprinkler"
        ]
    },

    "chickpea": {
        "Seeds": ["Chickpea Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Water Sprinkler",
            "Water Pump"
        ]
    },

    "kidneybeans": {
        "Seeds": ["Kidney Bean Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Sprinkler"
        ]
    },

    "pigeonpeas": {
        "Seeds": ["Pigeon Pea Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Water Pump",
            "Water Sprinkler"
        ]
    },

    "mothbeans": {
        "Seeds": ["Moth Bean Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Water Sprinkler",
            "Water Pump"
        ]
    },

    "mungbean": {
        "Seeds": ["Mung Bean Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Weeding Tool"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Sprinkler"
        ]
    },

    "blackgram": {
        "Seeds": ["Black Gram Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Weeding Tool"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Sprinkler"
        ]
    },

    "lentil": {
        "Seeds": ["Lentil Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Agricultural Sickle"
        ],
        "Irrigation": [
            "Water Sprinkler",
            "Water Pump"
        ]
    },

    "pomegranate": {
        "Seeds": [],
        "Plants": ["Pomegranate Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Vermicompost"
        ],
        "Farming Tools": [
            "Pruning Shears",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Drip Irrigation Pipe"
        ]
    },

    "banana": {
        "Seeds": [],
        "Plants": ["Banana Plants"],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Vermicompost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "mango": {
        "Seeds": [],
        "Plants": ["Mango Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Pruning Shears",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "grapes": {
        "Seeds": [],
        "Plants": ["Grape Plants"],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Vermicompost"
        ],
        "Farming Tools": [
            "Pruning Shears",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Drip Irrigation Pipe"
        ]
    },

    "watermelon": {
        "Seeds": ["Watermelon Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Weeding Tool"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Sprinkler"
        ]
    },

    "muskmelon": {
        "Seeds": ["Muskmelon Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Organic Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Weeding Tool"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Sprinkler"
        ]
    },

    "apple": {
        "Seeds": [],
        "Plants": ["Apple Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Pruning Shears",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "orange": {
        "Seeds": [],
        "Plants": ["Orange Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Vermicompost"
        ],
        "Farming Tools": [
            "Pruning Shears",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "papaya": {
        "Seeds": [],
        "Plants": ["Papaya Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Vermicompost"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "coconut": {
        "Seeds": [],
        "Plants": ["Coconut Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Farming Tools Set",
            "Hand Hoe"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "cotton": {
        "Seeds": ["Cotton Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Urea Fertilizer",
            "Organic Fertilizer"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Agricultural Sickle"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    },

    "jute": {
        "Seeds": ["Jute Seeds"],
        "Plants": [],
        "Fertilizers": [
            "NPK Fertilizer",
            "Urea Fertilizer",
            "Organic Fertilizer"
        ],
        "Farming Tools": [
            "Hand Hoe",
            "Agricultural Sickle"
        ],
        "Irrigation": [
            "Water Pump",
            "Water Sprinkler"
        ]
    },

    "coffee": {
        "Seeds": [],
        "Plants": ["Coffee Plants"],
        "Fertilizers": [
            "Organic Fertilizer",
            "NPK Fertilizer",
            "Compost"
        ],
        "Farming Tools": [
            "Pruning Shears",
            "Farming Tools Set"
        ],
        "Irrigation": [
            "Drip Irrigation Kit",
            "Water Pump"
        ]
    }
}


# ============================================================
# CART
# ============================================================

if "cart" not in st.session_state:
    st.session_state.cart = []


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🛒 AgriMate Marketplace</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Farming Marketplace</div>',
    unsafe_allow_html=True
)

st.write(
    "Find seeds, plants, fertilizers, farming tools and "
    "irrigation equipment for your farming needs."
)

st.divider()


# ============================================================
# CART SUMMARY
# ============================================================

cart_count = len(st.session_state.cart)

cart_total = sum(
    item["price"] for item in st.session_state.cart
)

cart_col1, cart_col2 = st.columns(2)

with cart_col1:

    st.metric(
        "🛒 Cart Items",
        cart_count
    )

with cart_col2:

    st.metric(
        "💰 Cart Value",
        f"₹{cart_total:,.2f}"
    )


# ============================================================
# GET RECOMMENDED CROP
# ============================================================

recommended_crop = st.session_state.get(
    "recommended_crop",
    None
)


# ============================================================
# RECOMMENDED PRODUCTS
# ============================================================

if recommended_crop:

    crop_name = str(
        recommended_crop
    ).strip().lower()

    crop_name = crop_name.replace(
        "___",
        " "
    )

    crop_name = crop_name.replace(
        "_",
        " "
    )

    crop_aliases = {

        "kidney beans": "kidneybeans",

        "kidney bean": "kidneybeans",

        "pigeon pea": "pigeonpeas",

        "pigeon peas": "pigeonpeas",

        "mung bean": "mungbean",

        "mung beans": "mungbean",

        "black gram": "blackgram",

        "black grams": "blackgram",

        "moth bean": "mothbeans",

        "moth beans": "mothbeans"
    }

    crop_key = crop_aliases.get(
        crop_name,
        crop_name
    )

    if crop_key in crop_products:

        recommendations = crop_products[
            crop_key
        ]

        display_crop = crop_key.title()

        st.divider()

        st.header(
            f"🌱 Recommended Products for {display_crop}"
        )

        st.success(
            f"AgriMate recommended **{display_crop}** "
            "for your farming conditions."
        )


        # ====================================================
        # SEEDS / PLANTS
        # ====================================================

        recommended_items = (
            recommendations["Seeds"]
            + recommendations["Plants"]
        )

        if recommended_items:

            st.subheader(
                "🌱 Seeds / Plants"
            )

            cols = st.columns(3)

            for index, product_name in enumerate(
                recommended_items
            ):

                for product in products:

                    if product["name"] == product_name:

                        with cols[index % 3]:

                            st.markdown(
                                '<div class="product-card">',
                                unsafe_allow_html=True
                            )

                            st.subheader(
                                f"🌱 {product['name']}"
                            )

                            st.write(
                                product["description"]
                            )

                            st.write(
                                f"⭐ {product['rating']}/5"
                            )

                            st.markdown(
                                f"### ₹{product['price']}"
                            )

                            st.write(
                                f"📦 Stock: {product['stock']}"
                            )

                            if st.button(
                                "🛒 Add to Cart",
                                key=f"recommended_seed_{index}_{product_name}",
                                use_container_width=True
                            ):

                                st.session_state.cart.append(
                                    product
                                )

                                st.success(
                                    "Added to cart!"
                                )

                            st.markdown(
                                "</div>",
                                unsafe_allow_html=True
                            )


        # ====================================================
        # FERTILIZERS
        # ====================================================

        st.subheader(
            "🧪 Fertilizers"
        )

        cols = st.columns(3)

        for index, product_name in enumerate(
            recommendations["Fertilizers"]
        ):

            for product in products:

                if product["name"] == product_name:

                    with cols[index % 3]:

                        st.markdown(
                            '<div class="product-card">',
                            unsafe_allow_html=True
                        )

                        st.subheader(
                            f"🧪 {product['name']}"
                        )

                        st.write(
                            product["description"]
                        )

                        st.write(
                            f"⭐ {product['rating']}/5"
                        )

                        st.markdown(
                            f"### ₹{product['price']}"
                        )

                        st.write(
                            f"📦 Stock: {product['stock']}"
                        )

                        if st.button(
                            "🛒 Add to Cart",
                            key=f"recommended_fertilizer_{index}",
                            use_container_width=True
                        ):

                            st.session_state.cart.append(
                                product
                            )

                            st.success(
                                "Added to cart!"
                            )

                        st.markdown(
                            "</div>",
                            unsafe_allow_html=True
                        )


        # ====================================================
        # FARMING TOOLS
        # ====================================================

        st.subheader(
            "🛠️ Farming Tools"
        )

        cols = st.columns(3)

        for index, product_name in enumerate(
            recommendations["Farming Tools"]
        ):

            for product in products:

                if product["name"] == product_name:

                    with cols[index % 3]:

                        st.markdown(
                            '<div class="product-card">',
                            unsafe_allow_html=True
                        )

                        st.subheader(
                            f"🛠️ {product['name']}"
                        )

                        st.write(
                            product["description"]
                        )

                        st.write(
                            f"⭐ {product['rating']}/5"
                        )

                        st.markdown(
                            f"### ₹{product['price']}"
                        )

                        st.write(
                            f"📦 Stock: {product['stock']}"
                        )

                        if st.button(
                            "🛒 Add to Cart",
                            key=f"recommended_tool_{index}",
                            use_container_width=True
                        ):

                            st.session_state.cart.append(
                                product
                            )

                            st.success(
                                "Added to cart!"
                            )

                        st.markdown(
                            "</div>",
                            unsafe_allow_html=True
                        )


        # ====================================================
        # IRRIGATION
        # ====================================================

        st.subheader(
            "💧 Irrigation Equipment"
        )

        cols = st.columns(3)

        for index, product_name in enumerate(
            recommendations["Irrigation"]
        ):

            for product in products:

                if product["name"] == product_name:

                    with cols[index % 3]:

                        st.markdown(
                            '<div class="product-card">',
                            unsafe_allow_html=True
                        )

                        st.subheader(
                            f"💧 {product['name']}"
                        )

                        st.write(
                            product["description"]
                        )

                        st.write(
                            f"⭐ {product['rating']}/5"
                        )

                        st.markdown(
                            f"### ₹{product['price']}"
                        )

                        st.write(
                            f"📦 Stock: {product['stock']}"
                        )

                        if st.button(
                            "🛒 Add to Cart",
                            key=f"recommended_irrigation_{index}",
                            use_container_width=True
                        ):

                            st.session_state.cart.append(
                                product
                            )

                            st.success(
                                "Added to cart!"
                            )

                        st.markdown(
                            "</div>",
                            unsafe_allow_html=True
                        )


# ============================================================
# SEARCH PRODUCTS
# ============================================================

st.divider()

st.header(
    "🔍 Find Products"
)

search = st.text_input(
    "Search products",
    placeholder=(
        "Search rice, wheat, maize, fertilizer, "
        "tools, irrigation..."
    )
)


# ============================================================
# CATEGORY FILTER
# ============================================================

categories = [
    "All",
    "Seeds",
    "Plants",
    "Fertilizers",
    "Farming Tools",
    "Irrigation"
]

selected_category = st.selectbox(
    "🌾 Select Category",
    categories
)


# ============================================================
# FILTER PRODUCTS
# ============================================================

search_text = search.strip().lower()

filtered_products = []

for product in products:

    name = product["name"].lower()

    category = product["category"].lower()

    description = product["description"].lower()

    search_match = (
        search_text == ""
        or search_text in name
        or search_text in category
        or search_text in description
    )

    category_match = (
        selected_category == "All"
        or product["category"] == selected_category
    )

    if search_match and category_match:

        filtered_products.append(
            product
        )


# ============================================================
# PRODUCT DISPLAY
# ============================================================

st.divider()

st.header(
    "⭐ Products"
)

st.write(
    f"Showing {len(filtered_products)} product(s)"
)


if len(filtered_products) == 0:

    st.warning(
        "No products found. Try another search "
        "or select All."
    )

else:

    for i in range(
        0,
        len(filtered_products),
        3
    ):

        cols = st.columns(3)

        for j in range(3):

            index = i + j

            if index >= len(filtered_products):
                break

            product = filtered_products[index]

            with cols[j]:

                st.markdown(
                    '<div class="product-card">',
                    unsafe_allow_html=True
                )

                # Product icon

                if product["category"] == "Seeds":

                    st.markdown(
                        "## 🌱"
                    )

                elif product["category"] == "Plants":

                    st.markdown(
                        "## 🌳"
                    )

                elif product["category"] == "Fertilizers":

                    st.markdown(
                        "## 🧪"
                    )

                elif product["category"] == "Farming Tools":

                    st.markdown(
                        "## 🛠️"
                    )

                else:

                    st.markdown(
                        "## 💧"
                    )


                st.subheader(
                    product["name"]
                )

                st.write(
                    "**Category:** "
                    + product["category"]
                )

                st.write(
                    product["description"]
                )

                st.write(
                    f"⭐ {product['rating']}/5"
                )

                st.markdown(
                    f"### ₹{product['price']}"
                )

                if product["stock"] > 0:

                    st.write(
                        f"📦 In Stock ({product['stock']})"
                    )

                else:

                    st.error(
                        "Out of Stock"
                    )


                if product["stock"] > 0:

                    if st.button(
                        "🛒 Add to Cart",
                        key=f"search_add_{index}",
                        use_container_width=True
                    ):

                        st.session_state.cart.append(
                            product
                        )

                        st.success(
                            product["name"]
                            + " added to cart!"
                        )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )


# ============================================================
# SHOPPING CART
# ============================================================

st.divider()

st.header(
    "🛒 Your Cart"
)


if len(st.session_state.cart) == 0:

    st.info(
        "Your cart is empty."
    )

else:

    # --------------------------------------------------------
    # GROUP CART ITEMS
    # --------------------------------------------------------

    cart_items = {}

    for item in st.session_state.cart:

        name = item["name"]

        if name not in cart_items:

            cart_items[name] = {
                "product": item,
                "quantity": 0
            }

        cart_items[name]["quantity"] += 1


    # --------------------------------------------------------
    # DISPLAY CART
    # --------------------------------------------------------

    total = 0

    for name, cart_item in cart_items.items():

        item = cart_item["product"]

        quantity = cart_item["quantity"]

        item_total = (
            item["price"]
            * quantity
        )

        total += item_total

        col1, col2, col3, col4 = st.columns(
            [4, 2, 2, 1]
        )

        with col1:

            st.write(
                f"🌱 **{item['name']}**"
            )

        with col2:

            st.write(
                f"₹{item['price']} each"
            )

        with col3:

            st.write(
                f"Quantity: **{quantity}**"
            )

        with col4:

            if st.button(
                "❌",
                key=f"remove_{name}"
            ):

                for i, cart_product in enumerate(
                    st.session_state.cart
                ):

                    if cart_product["name"] == name:

                        st.session_state.cart.pop(i)

                        break

                st.rerun()


        st.write(
            f"Item Total: ₹{item_total:,.2f}"
        )

        st.divider()


    # --------------------------------------------------------
    # CART TOTAL
    # --------------------------------------------------------

    st.subheader(
        f"💰 Cart Total: ₹{total:,.2f}"
    )


    # --------------------------------------------------------
    # CLEAR CART
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear Cart",
        use_container_width=True
    ):

        st.session_state.cart.clear()

        st.rerun()


# ============================================================
# NAVIGATION
# ============================================================

st.divider()

nav1, nav2 = st.columns(2)

with nav1:

    if st.button(
        "🌱 Crop Recommendation",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_🌾_Crop_Recommendation.py"
        )


with nav2:

    if st.button(
        "🛠️ Farming Tools",
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
    "AgriMate • Smart Agricultural Marketplace • "
    "Crop-based farming recommendations"
)