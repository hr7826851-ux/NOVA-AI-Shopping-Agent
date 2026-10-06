import streamlit as st
import pandas as pd
import re
import random
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NOVA — Premium Shopping",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "Home",
    "cart": [],
    "saved": [],
    "compare": [],
    "orders": [],
    "history": [],
    "query": "",
    "category": "All",
    "results": None,
    "last_order": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value.copy() if isinstance(value, list) else value


# ============================================================
# PREMIUM DESIGN
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --navy: #080d18;
    --navy2: #10182a;
    --violet: #7c5cff;
    --violet2: #9b86ff;
    --text: #172033;
    --muted: #697386;
    --border: #e5e8ef;
    --background: #f5f6fa;
    --white: #ffffff;
}

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 80% 0%,
            rgba(124,92,255,0.08),
            transparent 25%
        ),
        #f5f6fa;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #070c17 0%,
            #0d1424 55%,
            #10182a 100%
        );
    border-right: 1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] * {
    color: #eef1f7 !important;
}

.sidebar-logo {
    margin-top: 8px;
    margin-bottom: 35px;
}

.logo-mark {
    width: 44px;
    height: 44px;
    border-radius: 13px;
    background: linear-gradient(
        135deg,
        #7c5cff,
        #a88cff
    );
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: white !important;
    font-size: 24px;
    font-weight: 700;
    box-shadow:
        0 10px 30px rgba(124,92,255,0.35);
}

.logo-name {
    display: inline-block;
    margin-left: 10px;
    font-size: 25px;
    font-weight: 700;
    letter-spacing: 2px;
    vertical-align: middle;
    color: white !important;
}

.logo-sub {
    margin-top: 8px;
    color: #8995aa !important;
    font-size: 11px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.sidebar-heading {
    color: #747f95 !important;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin: 22px 0 8px;
}

/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: 1px solid transparent !important;
    color: #dce2ed !important;
    text-align: left !important;
    border-radius: 12px !important;
    min-height: 42px !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(124,92,255,0.12) !important;
    border-color: rgba(124,92,255,0.25) !important;
    color: white !important;
}

/* =========================================================
   MAIN AREA
   ========================================================= */

.block-container {
    max-width: 1450px;
    padding-top: 25px;
    padding-bottom: 60px;
}

/* Main text */

[data-testid="stAppViewContainer"] h1,
[data-testid="stAppViewContainer"] h2,
[data-testid="stAppViewContainer"] h3,
[data-testid="stAppViewContainer"] h4 {
    color: #172033 !important;
}

[data-testid="stMarkdownContainer"] {
    color: #172033 !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #4f5c70 !important;
}

[data-testid="stMarkdownContainer"] strong {
    color: #172033 !important;
}

/* =========================================================
   TOP BRAND
   ========================================================= */

.top-brand {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.top-brand-name {
    color: #172033 !important;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.top-brand-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #7c5cff;
    margin-right: 8px;
}

/* =========================================================
   HERO
   ========================================================= */

.premium-hero {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(157,132,255,0.28),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #080d18,
            #121d35 60%,
            #211846
        );
    border-radius: 30px;
    padding: 55px;
    min-height: 350px;
    color: white;
    box-shadow:
        0 25px 70px rgba(12,18,35,0.18);
}

.premium-hero:after {
    content: "✦";
    position: absolute;
    right: 70px;
    top: 40px;
    font-size: 150px;
    color: rgba(255,255,255,0.035);
}

.hero-kicker {
    color: #a997ff !important;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.hero-title {
    color: white !important;
    font-family: 'Playfair Display', serif;
    font-size: 50px;
    line-height: 1.05;
    max-width: 720px;
    margin: 18px 0;
}

.hero-description {
    color: #c7cfdf !important;
    font-size: 15px;
    line-height: 1.7;
    max-width: 650px;
}

/* =========================================================
   SEARCH
   ========================================================= */

.search-shell {
    background: white;
    border: 1px solid #e4e7ee;
    border-radius: 17px;
    padding: 7px;
    box-shadow: 0 12px 35px rgba(20,30,50,0.06);
    margin-top: -30px;
    position: relative;
    z-index: 3;
}

/* =========================================================
   STAT CARDS
   ========================================================= */

.stat-card {
    background: white;
    border: 1px solid #e5e8ef;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 7px 25px rgba(20,30,50,0.04);
}

.stat-number {
    font-size: 25px;
    font-weight: 700;
    color: #172033 !important;
}

.stat-label {
    color: #7a8496 !important;
    font-size: 12px;
    margin-top: 4px;
}

/* =========================================================
   PRODUCT CARDS
   ========================================================= */

.product-shell {
    background: white;
    border: 1px solid #e3e6ed;
    border-radius: 22px;
    padding: 16px;
    box-shadow:
        0 8px 30px rgba(20,30,50,0.055);
    transition: 0.2s ease;
}

.product-shell:hover {
    border-color: #c9c0ff;
    box-shadow:
        0 15px 40px rgba(80,60,160,0.10);
}

.product-category {
    color: #7c5cff !important;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
}

.product-name {
    color: #172033 !important;
    font-size: 18px;
    font-weight: 700;
    line-height: 1.25;
    margin-top: 7px;
}

.product-brand {
    color: #7a8496 !important;
    font-size: 12px;
}

.product-price {
    color: #172033 !important;
    font-size: 25px;
    font-weight: 800;
    margin-top: 10px;
}

.product-rating {
    color: #59657a !important;
    font-size: 12px;
}

.match-pill {
    display: inline-block;
    background: #eaf9f1;
    color: #168253 !important;
    border-radius: 20px;
    padding: 6px 10px;
    font-size: 10px;
    font-weight: 700;
    margin: 9px 0;
}

/* =========================================================
   CHECKOUT
   ========================================================= */

.checkout-banner {
    background: white;
    border: 1px solid #e4e7ee;
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 25px;
}

.checkout-step {
    text-align: center;
    font-size: 11px;
    font-weight: 700;
    padding: 10px 5px;
    border-radius: 10px;
}

.checkout-active {
    background: #7c5cff;
    color: white !important;
}

.checkout-done {
    background: #e9f8f1;
    color: #158153 !important;
}

.checkout-pending {
    background: #eef1f6;
    color: #7c8799 !important;
}

/* =========================================================
   SUMMARY
   ========================================================= */

.dark-summary {
    background:
        linear-gradient(
            145deg,
            #0b1220,
            #17233d
        );
    color: white;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 15px 45px rgba(10,18,35,0.15);
}

.dark-summary h3,
.dark-summary p,
.dark-summary strong {
    color: white !important;
}

/* =========================================================
   FOOTER
   ========================================================= */

.premium-footer {
    text-align: center;
    color: #8993a5 !important;
    font-size: 11px;
    letter-spacing: 0.4px;
    padding-top: 35px;
}

</style>
""")


# ============================================================
# LOAD DATABASE
# ============================================================

@st.cache_data
def load_products():

    df = pd.read_csv("products.csv")

    required = [
        "id",
        "name",
        "category",
        "brand",
        "price",
        "rating",
        "description",
        "features"
    ]

    for column in required:
        if column not in df.columns:
            df[column] = ""

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    ).fillna(0)

    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce"
    ).fillna(4.0)

    return df


try:
    products = load_products()
except Exception as e:
    st.error("products.csv could not be loaded.")
    st.code(str(e))
    st.stop()


# ============================================================
# HELPERS
# ============================================================

def money(value):
    return f"₹{float(value):,.0f}"


def get_categories():
    return ["All"] + sorted(
        products["category"]
        .astype(str)
        .unique()
        .tolist()
    )


def get_product(pid):

    data = products[
        products["id"].astype(str) == str(pid)
    ]

    if data.empty:
        return None

    return data.iloc[0].to_dict()


def cart_count():

    return sum(
        item["quantity"]
        for item in st.session_state.cart
    )


def cart_subtotal():

    return sum(
        item["price"] * item["quantity"]
        for item in st.session_state.cart
    )


def delivery_charge():

    if cart_subtotal() == 0:
        return 0

    return 0 if cart_subtotal() >= 999 else 49


def cart_total():

    return cart_subtotal() + delivery_charge()


# ============================================================
# CART FUNCTIONS
# ============================================================

def add_to_cart(product):

    pid = str(product["id"])

    for item in st.session_state.cart:

        if str(item["id"]) == pid:
            item["quantity"] += 1
            return

    st.session_state.cart.append({
        "id": pid,
        "name": str(product["name"]),
        "brand": str(product["brand"]),
        "price": float(product["price"]),
        "rating": float(product["rating"]),
        "quantity": 1
    })


def remove_from_cart(pid):

    st.session_state.cart = [
        item
        for item in st.session_state.cart
        if str(item["id"]) != str(pid)
    ]


def change_quantity(pid, amount):

    for item in st.session_state.cart:

        if str(item["id"]) == str(pid):

            item["quantity"] += amount

            if item["quantity"] <= 0:
                remove_from_cart(pid)

            return


# ============================================================
# PRODUCT IMAGE
# ============================================================

IMAGE_DIR = Path("nova_images")
IMAGE_DIR.mkdir(exist_ok=True)


def category_symbol(category):

    symbols = {
        "Electronics": "PHONE",
        "Gaming": "PLAY",
        "Audio": "AUDIO",
        "Fashion": "STYLE",
        "Beauty": "BEAUTY",
        "Books": "BOOK",
        "Home": "HOME",
        "Accessories": "NOVA"
    }

    return symbols.get(
        category,
        "NOVA"
    )


@st.cache_data
def make_product_visual(
    product_id,
    category,
    name
):

    path = IMAGE_DIR / f"{product_id}.png"

    if path.exists():
        return str(path)

    width = 900
    height = 560

    image = Image.new(
        "RGB",
        (width, height),
        (241, 243, 249)
    )

    draw = ImageDraw.Draw(image)

    # premium gradient bands

    for y in range(height):

        ratio = y / height

        r = int(241 - ratio * 8)
        g = int(243 - ratio * 9)
        b = int(249 - ratio * 2)

        draw.line(
            [(0, y), (width, y)],
            fill=(r, g, b)
        )

    # Decorative circles

    draw.ellipse(
        (590, -80, 950, 280),
        fill=(225, 219, 255)
    )

    draw.ellipse(
        (-120, 360, 260, 720),
        fill=(232, 235, 255)
    )

    # Product mockup

    if category == "Electronics":

        draw.rounded_rectangle(
            (315, 100, 585, 390),
            radius=35,
            fill=(30, 35, 50)
        )

        draw.rounded_rectangle(
            (335, 120, 565, 370),
            radius=25,
            fill=(80, 76, 120)
        )

        draw.ellipse(
            (390, 145, 510, 265),
            fill=(18, 22, 34)
        )

        draw.ellipse(
            (420, 175, 480, 235),
            fill=(100, 85, 180)
        )

    elif category == "Gaming":

        draw.rounded_rectangle(
            (250, 190, 650, 350),
            radius=55,
            fill=(28, 31, 43)
        )

        draw.ellipse(
            (300, 225, 365, 290),
            fill=(124, 92, 255)
        )

        draw.ellipse(
            (535, 225, 600, 290),
            fill=(124, 92, 255)
        )

        draw.rectangle(
            (405, 220, 495, 240),
            fill=(180, 170, 255)
        )

    elif category == "Audio":

        draw.ellipse(
            (270, 110, 630, 470),
            fill=(31, 36, 51)
        )

        draw.ellipse(
            (320, 160, 580, 420),
            fill=(103, 86, 170)
        )

        draw.arc(
            (250, 55, 650, 500),
            180,
            360,
            fill=(20, 24, 35),
            width=35
        )

    elif category == "Fashion":

        draw.polygon(
            [
                (380, 120),
                (520, 120),
                (610, 210),
                (545, 270),
                (500, 220),
                (500, 410),
                (400, 410),
                (400, 220),
                (355, 270),
                (290, 210)
            ],
            fill=(89, 78, 135)
        )

    elif category == "Beauty":

        draw.rounded_rectangle(
            (355, 100, 545, 400),
            radius=30,
            fill=(220, 200, 225)
        )

        draw.rectangle(
            (390, 70, 510, 125),
            fill=(45, 43, 60)
        )

        draw.rounded_rectangle(
            (390, 215, 510, 255),
            radius=10,
            fill=(124, 92, 255)
        )

    elif category == "Books":

        draw.polygon(
            [
                (280, 130),
                (450, 165),
                (620, 130),
                (620, 410),
                (450, 450),
                (280, 410)
            ],
            fill=(64, 65, 95)
        )

        draw.line(
            (450, 165, 450, 450),
            fill=(220, 220, 235),
            width=6
        )

    elif category == "Home":

        draw.rectangle(
            (290, 210, 610, 390),
            fill=(105, 93, 140)
        )

        draw.polygon(
            [
                (250, 220),
                (450, 70),
                (650, 220)
            ],
            fill=(48, 52, 70)
        )

        draw.rectangle(
            (420, 280, 480, 390),
            fill=(40, 42, 55)
        )

    else:

        draw.ellipse(
            (290, 100, 610, 420),
            fill=(95, 80, 150)
        )

        draw.text(
            (380, 225),
            "N",
            fill="white"
        )

    # Category label

    try:
        font = ImageFont.truetype(
            "arial.ttf",
            26
        )
    except:
        font = ImageFont.load_default()

    label = category_symbol(category)

    draw.text(
        (35, 35),
        label,
        fill=(75, 80, 100),
        font=font
    )

    image.save(
        path,
        "PNG"
    )

    return str(path)


# ============================================================
# SEARCH
# ============================================================

def extract_budget(query):

    query = query.lower().replace(",", "")

    patterns = [
        r"(?:under|below|less than|upto|up to|max)\s*(?:₹|rs\.?|inr)?\s*(\d+)",
        r"(?:₹|rs\.?|inr)\s*(\d+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            query
        )

        if match:
            return float(match.group(1))

    return None


def detect_category(query):

    query = query.lower()

    mapping = {

        "Electronics": [
            "phone",
            "mobile",
            "smartphone",
            "laptop",
            "tablet",
            "monitor",
            "tv"
        ],

        "Gaming": [
            "gaming",
            "game",
            "controller",
            "xbox",
            "playstation",
            "mouse",
            "keyboard"
        ],

        "Audio": [
            "headphone",
            "earphone",
            "earbuds",
            "speaker",
            "audio"
        ],

        "Fashion": [
            "shirt",
            "tshirt",
            "jeans",
            "shoe",
            "dress",
            "jacket"
        ],

        "Beauty": [
            "beauty",
            "cream",
            "makeup",
            "perfume",
            "skin"
        ],

        "Books": [
            "book",
            "novel",
            "programming"
        ],

        "Home": [
            "home",
            "chair",
            "table",
            "lamp",
            "kitchen"
        ],

        "Accessories": [
            "watch",
            "wallet",
            "bag",
            "accessory"
        ]
    }

    for category, words in mapping.items():

        if any(
            word in query
            for word in words
        ):
            return category

    return "All"


def search_products(
    query,
    category="All",
    budget=None
):

    df = products.copy()

    if category != "All":

        df = df[
            df["category"].astype(str).str.lower()
            == category.lower()
        ]

    if budget is not None:

        df = df[
            df["price"] <= budget
        ]

    if not query.strip():

        return df.head(30)

    words = re.findall(
        r"[a-zA-Z0-9]+",
        query.lower()
    )

    scores = []

    for _, row in df.iterrows():

        name = str(row["name"]).lower()
        brand = str(row["brand"]).lower()
        cat = str(row["category"]).lower()
        description = str(row["description"]).lower()
        features = str(row["features"]).lower()

        text = (
            name + " "
            + brand + " "
            + cat + " "
            + description + " "
            + features
        )

        score = 0

        for word in words:

            if word in name:
                score += 10

            if word in brand:
                score += 7

            if word in cat:
                score += 6

            if word in text:
                score += 2

        score += float(row["rating"])

        scores.append(score)

    df["score"] = scores

    return df.sort_values(
        "score",
        ascending=False
    ).head(30)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-logo">

        <span class="logo-mark">✦</span>
        <span class="logo-name">NOVA</span>

        <div class="logo-sub">
            Premium intelligent shopping
        </div>

    </div>
    """)

    st.html(
        '<div class="sidebar-heading">DISCOVER</div>'
    )

    if st.button(
        "⌂   Home",
        use_container_width=True
    ):
        st.session_state.page = "Home"
        st.rerun()

    if st.button(
        "⌕   Find Products",
        use_container_width=True
    ):
        st.session_state.page = "Find Products"
        st.rerun()

    st.html(
        '<div class="sidebar-heading">YOUR NOVA</div>'
    )

    if st.button(
        f"🛒   Cart  ({cart_count()})",
        use_container_width=True
    ):
        st.session_state.page = "Cart"
        st.rerun()

    if st.button(
        "💳   Checkout",
        use_container_width=True
    ):

        if cart_count():
            st.session_state.page = "Checkout"
        else:
            st.session_state.page = "Cart"

        st.rerun()

    if st.button(
        "📦   Orders",
        use_container_width=True
    ):
        st.session_state.page = "Orders"
        st.rerun()

    if st.button(
        "♡   Saved",
        use_container_width=True
    ):
        st.session_state.page = "Saved"
        st.rerun()

    if st.button(
        "⚖   Compare",
        use_container_width=True
    ):
        st.session_state.page = "Compare"
        st.rerun()

    if st.button(
        "◷   History",
        use_container_width=True
    ):
        st.session_state.page = "History"
        st.rerun()

    st.html(
        '<div class="sidebar-heading">CATEGORIES</div>'
    )

    for cat in get_categories():

        if st.button(
            cat,
            key=f"side_cat_{cat}",
            use_container_width=True
        ):

            st.session_state.category = cat
            st.session_state.query = ""
            st.session_state.results = None
            st.session_state.page = "Find Products"

            st.rerun()

    st.divider()

    st.caption(
        f"{cart_count()} items in cart"
    )

    st.caption(
        f"Cart value • {money(cart_total())}"
    )


# ============================================================
# TOP BRAND
# ============================================================

st.html("""
<div class="top-brand">

    <div class="top-brand-name">
        <span class="top-brand-dot"></span>
        NOVA PREMIUM SHOPPING
    </div>

    <div class="top-brand-name">
        800+ PRODUCTS &nbsp; • &nbsp; 8 CATEGORIES
    </div>

</div>
""")


# ============================================================
# PRODUCT CARD
# ============================================================

def product_card(row, number):

    product = row.to_dict()

    pid = str(product["id"])
    name = str(product["name"])
    brand = str(product["brand"])
    category = str(product["category"])
    price = float(product["price"])
    rating = float(product["rating"])

    image_path = make_product_visual(
        pid,
        category,
        name
    )

    st.image(
        image_path,
        use_container_width=True
    )

    st.html(
        f"""
        <div class="product-category">
            {category}
        </div>

        <div class="product-name">
            {name}
        </div>

        <div class="product-brand">
            {brand}
        </div>

        <div class="product-price">
            {money(price)}
        </div>

        <div class="product-rating">
            ★ {rating:.1f} / 5
        </div>

        <div class="match-pill">
            {min(99, int(82 + rating * 4))}% MATCH
        </div>
        """
    )

    saved = pid in [
        str(x)
        for x in st.session_state.saved
    ]

    compared = pid in [
        str(x)
        for x in st.session_state.compare
    ]

    a, b = st.columns(2)

    with a:

        if st.button(
            "♥ Saved" if saved else "♡ Save",
            key=f"save_{pid}_{number}",
            use_container_width=True
        ):

            if pid in [
                str(x)
                for x in st.session_state.saved
            ]:

                st.session_state.saved = [
                    x
                    for x in st.session_state.saved
                    if str(x) != pid
                ]

            else:

                st.session_state.saved.append(pid)

            st.rerun()

    with b:

        if st.button(
            "✓ Compared" if compared else "+ Compare",
            key=f"compare_{pid}_{number}",
            use_container_width=True
        ):

            current = [
                str(x)
                for x in st.session_state.compare
            ]

            if pid in current:

                st.session_state.compare = [
                    x
                    for x in st.session_state.compare
                    if str(x) != pid
                ]

            elif len(current) < 4:

                st.session_state.compare.append(pid)

            st.rerun()

    a, b = st.columns(2)

    with a:

        if st.button(
            "🛒 Add to Cart",
            key=f"cart_{pid}_{number}",
            use_container_width=True
        ):

            add_to_cart(product)

            st.toast(
                "Added to your NOVA cart"
            )

            st.rerun()

    with b:

        if st.button(
            "⚡ Buy Now",
            key=f"buy_{pid}_{number}",
            type="primary",
            use_container_width=True
        ):

            st.session_state.cart = []

            add_to_cart(product)

            st.session_state.page = "Checkout"

            st.rerun()

    with st.expander(
        "Product details"
    ):

        st.write(
            product.get(
                "description",
                ""
            )
        )

        st.write(
            product.get(
                "features",
                ""
            )
        )


# ============================================================
# HOME
# ============================================================

def home_page():

    st.html("""
    <div class="premium-hero">

        <div class="hero-kicker">
            ✦ THE NOVA EXPERIENCE
        </div>

        <div class="hero-title">
            Find something<br>
            worth owning.
        </div>

        <div class="hero-description">
            A smarter way to discover products.
            Search naturally, compare choices,
            save favourites and checkout effortlessly.
        </div>

    </div>
    """)

    st.markdown("")

    a, b = st.columns(
        [5, 1]
    )

    with a:

        query = st.text_input(
            "Search NOVA",
            placeholder="Try: smartphone under ₹30000",
            label_visibility="collapsed"
        )

    with b:

        search = st.button(
            "Search  ✦",
            type="primary",
            use_container_width=True
        )

    if search and query.strip():

        category = detect_category(query)
        budget = extract_budget(query)

        st.session_state.query = query
        st.session_state.category = category

        st.session_state.results = search_products(
            query,
            category,
            budget
        )

        st.session_state.history.append({
            "query": query,
            "time": datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )
        })

        st.session_state.page = "Find Products"

        st.rerun()

    st.markdown("##")

    st.html("""
    <div style="
        font-size:11px;
        font-weight:700;
        letter-spacing:1.8px;
        color:#7c5cff;
        margin-bottom:12px;
    ">
        NOVA COLLECTION
    </div>
    """)

    cols = st.columns(4)

    stats = [
        ("800+", "Curated products"),
        ("8", "Categories"),
        ("Smart", "Product matching"),
        (str(cart_count()), "Cart items")
    ]

    for col, (number, label) in zip(
        cols,
        stats
    ):

        with col:

            st.html(
                f"""
                <div class="stat-card">

                    <div class="stat-number">
                        {number}
                    </div>

                    <div class="stat-label">
                        {label}
                    </div>

                </div>
                """
            )

    st.markdown("##")

    st.subheader(
        "Explore by intent"
    )

    examples = [
        "Gaming laptop under ₹70000",
        "Smartphone under ₹30000",
        "Wireless earbuds",
        "Premium headphones",
        "Fashion essentials",
        "Programming books"
    ]

    cols = st.columns(3)

    for i, example in enumerate(examples):

        with cols[i % 3]:

            if st.button(
                example,
                key=f"home_example_{i}",
                use_container_width=True
            ):

                category = detect_category(
                    example
                )

                budget = extract_budget(
                    example
                )

                st.session_state.query = example
                st.session_state.category = category

                st.session_state.results = search_products(
                    example,
                    category,
                    budget
                )

                st.session_state.history.append({
                    "query": example,
                    "time": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    )
                })

                st.session_state.page = "Find Products"

                st.rerun()


# ============================================================
# FIND PRODUCTS
# ============================================================

def find_products_page():

    st.title(
        "Find Products"
    )

    st.caption(
        "Tell NOVA what you are looking for."
    )

    a, b, c = st.columns(
        [4, 1.5, 1]
    )

    with a:

        query = st.text_input(
            "Search",
            value=st.session_state.query,
            placeholder="Example: gaming laptop under ₹70000"
        )

    with b:

        cats = get_categories()

        selected_category = (
            st.session_state.category
            if st.session_state.category in cats
            else "All"
        )

        category = st.selectbox(
            "Category",
            cats,
            index=cats.index(
                selected_category
            )
        )

    with c:

        st.write("")

        search = st.button(
            "Search",
            type="primary",
            use_container_width=True
        )

    if search:

        budget = extract_budget(
            query
        )

        st.session_state.query = query
        st.session_state.category = category

        st.session_state.results = search_products(
            query,
            category,
            budget
        )

        if query.strip():

            st.session_state.history.append({
                "query": query,
                "time": datetime.now().strftime(
                    "%d %b %Y, %I:%M %p"
                )
            })

        st.rerun()

    if st.session_state.results is not None:

        result_df = st.session_state.results

    else:

        if category == "All":

            result_df = products.head(30)

        else:

            result_df = products[
                products["category"].astype(str)
                == category
            ].head(30)

    st.markdown(
        f"### {len(result_df)} products found"
    )

    if cart_count() > 0:

        st.info(
            f"🛒 {cart_count()} item(s) in cart • "
            f"{money(cart_total())}"
        )

        if st.button(
            "View Cart →",
            type="primary"
        ):

            st.session_state.page = "Cart"
            st.rerun()

    for start in range(
        0,
        len(result_df),
        3
    ):

        cols = st.columns(3)

        batch = result_df.iloc[
            start:start + 3
        ]

        for pos, (_, row) in enumerate(
            batch.iterrows()
        ):

            with cols[pos]:

                st.html(
                    '<div class="product-shell">'
                )

                product_card(
                    row,
                    start + pos
                )

                st.html(
                    '</div>'
                )


# ============================================================
# CART
# ============================================================

def cart_page():

    st.title(
        "Your Cart"
    )

    if not st.session_state.cart:

        st.info(
            "Your NOVA cart is empty."
        )

        if st.button(
            "Discover Products →",
            type="primary"
        ):

            st.session_state.page = "Find Products"
            st.rerun()

        return

    left, right = st.columns(
        [1.7, 1]
    )

    with left:

        st.subheader(
            "Selected items"
        )

        for i, item in enumerate(
            st.session_state.cart
        ):

            with st.container(
                border=True
            ):

                st.markdown(
                    f"### {item['name']}"
                )

                st.caption(
                    item["brand"]
                )

                st.markdown(
                    f"## {money(item['price'])}"
                )

                a, b, c, d = st.columns(
                    [1, 1, 1, 2]
                )

                with a:

                    if st.button(
                        "−",
                        key=f"minus_{i}",
                        use_container_width=True
                    ):

                        change_quantity(
                            item["id"],
                            -1
                        )

                        st.rerun()

                with b:

                    st.write(
                        f"**{item['quantity']}**"
                    )

                with c:

                    if st.button(
                        "+",
                        key=f"plus_{i}",
                        use_container_width=True
                    ):

                        change_quantity(
                            item["id"],
                            1
                        )

                        st.rerun()

                with d:

                    if st.button(
                        "Remove",
                        key=f"remove_{i}",
                        use_container_width=True
                    ):

                        remove_from_cart(
                            item["id"]
                        )

                        st.rerun()

    with right:

        st.html(
            f"""
            <div class="dark-summary">

                <h3>Order summary</h3>

                <p>
                    Subtotal
                    <strong style="float:right;">
                        {money(cart_subtotal())}
                    </strong>
                </p>

                <p>
                    Delivery
                    <strong style="float:right;">
                        {"FREE" if delivery_charge() == 0 else money(delivery_charge())}
                    </strong>
                </p>

                <hr>

                <p style="font-size:20px;">
                    Total
                    <strong style="float:right;">
                        {money(cart_total())}
                    </strong>
                </p>

            </div>
            """
        )

        st.write("")

        if st.button(
            "Proceed to Checkout  →",
            type="primary",
            use_container_width=True
        ):

            st.session_state.page = "Checkout"
            st.rerun()

        if st.button(
            "← Continue Shopping",
            use_container_width=True
        ):

            st.session_state.page = "Find Products"
            st.rerun()


# ============================================================
# CHECKOUT
# ============================================================

def checkout_page():

    if not st.session_state.cart:

        st.session_state.page = "Cart"
        st.rerun()
        return

    st.title(
        "Checkout"
    )

    st.caption(
        "Complete your delivery and payment details."
    )

    st.html("""
    <div class="checkout-banner">

        <div style="
            display:grid;
            grid-template-columns:repeat(4,1fr);
            gap:8px;
        ">

            <div class="checkout-step checkout-done">
                ✓ Cart
            </div>

            <div class="checkout-step checkout-active">
                2 Address
            </div>

            <div class="checkout-step checkout-active">
                3 Payment
            </div>

            <div class="checkout-step checkout-pending">
                4 Confirm
            </div>

        </div>

    </div>
    """)

    left, right = st.columns(
        [1.55, 1]
    )

    with left:

        st.subheader(
            "📍 Delivery details"
        )

        name = st.text_input(
            "Full Name",
            placeholder="Your full name"
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="10 digit mobile number"
        )

        address = st.text_area(
            "Full Address",
            placeholder="House / Flat / Street / Area",
            height=110
        )

        a, b = st.columns(2)

        with a:

            city = st.text_input(
                "City",
                placeholder="Your city"
            )

        with b:

            pin = st.text_input(
                "PIN Code",
                placeholder="6 digit PIN"
            )

        st.divider()

        st.subheader(
            "💳 Payment method"
        )

        payment = st.radio(
            "Select payment",
            [
                "UPI",
                "Debit / Credit Card",
                "Cash on Delivery"
            ]
        )

        if payment == "UPI":

            st.info(
                "UPI selected"
            )

            upi_id = st.text_input(
                "UPI ID",
                placeholder="example@upi"
            )

        elif payment == "Debit / Credit Card":

            st.warning(
                "Demo payment only. "
                "Do not use real card information."
            )

            card_name = st.text_input(
                "Cardholder Name",
                placeholder="Name on card"
            )

            card_number = st.text_input(
                "Card Number",
                placeholder="XXXX XXXX XXXX XXXX"
            )

            a, b = st.columns(2)

            with a:

                expiry = st.text_input(
                    "Expiry",
                    placeholder="MM/YY"
                )

            with b:

                cvv = st.text_input(
                    "CVV",
                    placeholder="XXX",
                    type="password"
                )

        else:

            st.success(
                "Cash on Delivery selected."
            )

    with right:

        st.html(
            f"""
            <div class="dark-summary">

                <h3>Order summary</h3>

                <p style="color:#aeb9cb !important;">
                    {cart_count()} item(s)
                </p>
            """
        )

        for item in st.session_state.cart:

            st.write(
                f"**{item['name']}**"
            )

            st.caption(
                f"{item['quantity']} × "
                f"{money(item['price'])}"
            )

        st.html(
            f"""
                <hr>

                <p>
                    Subtotal
                    <strong style="float:right;">
                        {money(cart_subtotal())}
                    </strong>
                </p>

                <p>
                    Delivery
                    <strong style="float:right;">
                        {"FREE" if delivery_charge() == 0 else money(delivery_charge())}
                    </strong>
                </p>

                <hr>

                <p style="font-size:22px;">
                    Total
                    <strong style="float:right;">
                        {money(cart_total())}
                    </strong>
                </p>

            </div>
            """
        )

    st.divider()

    if st.button(
        "✓  Place Order",
        type="primary",
        use_container_width=True
    ):

        if not name.strip():

            st.error(
                "Please enter your full name."
            )
            st.stop()

        phone_digits = re.sub(
            r"\D",
            "",
            phone
        )

        if len(phone_digits) != 10:

            st.error(
                "Please enter a valid 10 digit phone number."
            )
            st.stop()

        if not address.strip():

            st.error(
                "Please enter your full address."
            )
            st.stop()

        if not city.strip():

            st.error(
                "Please enter your city."
            )
            st.stop()

        pin_digits = re.sub(
            r"\D",
            "",
            pin
        )

        if len(pin_digits) != 6:

            st.error(
                "Please enter a valid 6 digit PIN code."
            )
            st.stop()

        if payment == "UPI":

            if not upi_id.strip():

                st.error(
                    "Please enter your UPI ID."
                )
                st.stop()

        order_id = (
            "NOVA-"
            + str(
                random.randint(
                    100000,
                    999999
                )
            )
        )

        order = {

            "id": order_id,

            "date": datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            ),

            "status": "Order Confirmed",

            "delivery": "Expected in 3–5 days",

            "total": cart_total(),

            "payment": payment,

            "name": name,

            "phone": phone,

            "address": address,

            "city": city,

            "pin": pin,

            "items": [
                item.copy()
                for item in st.session_state.cart
            ]
        }

        st.session_state.orders.insert(
            0,
            order
        )

        st.session_state.last_order = order

        st.session_state.cart = []

        st.session_state.page = "Confirmation"

        st.rerun()


# ============================================================
# CONFIRMATION
# ============================================================

def confirmation_page():

    order = st.session_state.last_order

    if not order:

        st.session_state.page = "Orders"
        st.rerun()
        return

    st.success(
        "Your order has been confirmed."
    )

    st.title(
        "Thank you for choosing NOVA."
    )

    st.caption(
        "Your shopping journey is complete."
    )

    a, b, c = st.columns(3)

    with a:

        st.metric(
            "Order ID",
            order["id"]
        )

    with b:

        st.metric(
            "Total",
            money(order["total"])
        )

    with c:

        st.metric(
            "Payment",
            order["payment"]
        )

    st.subheader(
        "Delivery information"
    )

    with st.container(
        border=True
    ):

        st.write(
            f"**Name:** {order['name']}"
        )

        st.write(
            f"**Phone:** {order['phone']}"
        )

        st.write(
            f"**Address:** "
            f"{order['address']}, "
            f"{order['city']} - "
            f"{order['pin']}"
        )

        st.success(
            f"🚚 {order['delivery']}"
        )

    a, b = st.columns(2)

    with a:

        if st.button(
            "📦 View Orders",
            type="primary",
            use_container_width=True
        ):

            st.session_state.page = "Orders"
            st.rerun()

    with b:

        if st.button(
            "Continue Shopping",
            use_container_width=True
        ):

            st.session_state.page = "Find Products"
            st.rerun()


# ============================================================
# ORDERS
# ============================================================

def orders_page():

    st.title(
        "Orders"
    )

    if not st.session_state.orders:

        st.info(
            "No orders placed yet."
        )
        return

    for order in st.session_state.orders:

        with st.container(
            border=True
        ):

            a, b = st.columns(2)

            with a:

                st.subheader(
                    order["id"]
                )

                st.caption(
                    order["date"]
                )

            with b:

                st.success(
                    order["status"]
                )

                st.markdown(
                    f"### {money(order['total'])}"
                )

            st.write(
                f"Payment: **{order['payment']}**"
            )

            st.write(
                f"Delivery: **{order['delivery']}**"
            )

            with st.expander(
                "View details"
            ):

                st.write(
                    f"Name: {order['name']}"
                )

                st.write(
                    f"Phone: {order['phone']}"
                )

                st.write(
                    f"Address: "
                    f"{order['address']}, "
                    f"{order['city']} - "
                    f"{order['pin']}"
                )

                st.markdown(
                    "#### Items"
                )

                for item in order["items"]:

                    st.write(
                        f"• {item['name']} × "
                        f"{item['quantity']} — "
                        f"{money(item['price'] * item['quantity'])}"
                    )


# ============================================================
# SAVED
# ============================================================

def saved_page():

    st.title(
        "Saved"
    )

    selected = []

    for pid in st.session_state.saved:

        product = get_product(pid)

        if product:
            selected.append(product)

    if not selected:

        st.info(
            "You haven't saved anything yet."
        )
        return

    df = pd.DataFrame(
        selected
    )

    for start in range(
        0,
        len(df),
        3
    ):

        cols = st.columns(3)

        for pos, (_, row) in enumerate(
            df.iloc[
                start:start + 3
            ].iterrows()
        ):

            with cols[pos]:

                st.html(
                    '<div class="product-shell">'
                )

                product_card(
                    row,
                    30000 + start + pos
                )

                st.html(
                    '</div>'
                )


# ============================================================
# COMPARE
# ============================================================

def compare_page():

    st.title(
        "Compare"
    )

    selected = []

    for pid in st.session_state.compare:

        product = get_product(pid)

        if product:
            selected.append(product)

    if len(selected) < 2:

        st.info(
            "Save at least 2 products to compare them."
        )
        return

    df = pd.DataFrame(
        selected
    )

    comparison = pd.DataFrame({

        "Product": df["name"],

        "Brand": df["brand"],

        "Category": df["category"],

        "Price": [
            money(x)
            for x in df["price"]
        ],

        "Rating": [
            f"★ {x:.1f}"
            for x in df["rating"]
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    if st.button(
        "Clear Comparison"
    ):

        st.session_state.compare = []
        st.rerun()


# ============================================================
# HISTORY
# ============================================================

def history_page():

    st.title(
        "Search History"
    )

    if not st.session_state.history:

        st.info(
            "Your search history is empty."
        )
        return

    for item in reversed(
        st.session_state.history
    ):

        with st.container(
            border=True
        ):

            st.write(
                f"⌕ **{item['query']}**"
            )

            st.caption(
                item["time"]
            )

    if st.button(
        "Clear History"
    ):

        st.session_state.history = []
        st.rerun()


# ============================================================
# ROUTER
# ============================================================

if st.session_state.page == "Home":

    home_page()

elif st.session_state.page == "Find Products":

    find_products_page()

elif st.session_state.page == "Cart":

    cart_page()

elif st.session_state.page == "Checkout":

    checkout_page()

elif st.session_state.page == "Confirmation":

    confirmation_page()

elif st.session_state.page == "Orders":

    orders_page()

elif st.session_state.page == "Saved":

    saved_page()

elif st.session_state.page == "Compare":

    compare_page()

elif st.session_state.page == "History":

    history_page()

else:

    st.session_state.page = "Home"
    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="premium-footer">

    NOVA ✦ Premium Smart Shopping

    <br><br>

    Discover • Compare • Save • Cart • Checkout • Orders

</div>
""")