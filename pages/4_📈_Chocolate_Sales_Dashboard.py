import streamlit as st
from PIL import Image

st.set_page_config(page_title="Chocolate Sales Dashboard", layout="wide")

# === CSS STYLE ===
st.markdown("""
    <style>
        .title {
            font-size: 44px;
            font-weight: bold;
            color: #4B2E2E;
            text-align: center;
            margin-bottom: 20px;
        }
        .section {
            background-color: #fff7f0;
            padding: 25px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        }
    </style>
""", unsafe_allow_html=True)

# === TITLE ===
st.markdown("<div class='title'>🍫 Chocolate Sales Dashboard 📊</div>", unsafe_allow_html=True)

# === CHARTS ===
charts = [
    # PIE CHART
    ("1. 🍬 Top 10 Best-Selling Products", "top_products_pie.jpg",
     "- 50% Dark Bites leads at 11.3%\n- Top 4 products >10%\n- Balanced distribution",
     """
This pie chart displays sales proportions for the 10 best-selling chocolate products.

50% Dark Bites leads with 11.3%, followed by Smooth Silky Salty (10.2%), Eclairs (10.1%), and Caramel Stuffed Bars (10.1%). Drinking Coco and Spicy Special Slims are at 10.0%, while Milk Bars and Peanut Butter Cubes follow at 9.6%. White Choc and After Nines each take up 9.5%.

The chart shows preferences are diverse and fairly even across all items.
     """),

    # BAR CHART BY COUNTRY
    ("2. 🌍 Total Revenue by Country", "revenue_by_country.jpg",
     "- Australia tops with $1.05M\n- UK & India nearly equal\n- All countries > $950K",
     """
The bar chart compares chocolate sales across six countries.

Australia led with 1.05M in revenue. The UK and India followed closely, each just over 1M. The USA ranked fourth, ahead of Canada and New Zealand, which still surpassed $950K.

This shows strong chocolate demand in all surveyed countries.
     """),

    # LINE CHART
    ("3. 📈 Monthly Sales Trend", "monthly_trend.jpg",
     "- Peaks: Feb & July\n- Lowest: March\n- Seasonal trends visible",
     """
The line graph shows monthly chocolate box shipments from Feb to Sep 2022.

Sales peaked in February (28,000) and July (26,000). March had the lowest point at 18,000. The fluctuations reflect seasonal buying trends like Valentine’s and summer promos.
     """),

    # SALESPERSON CHART
    ("4. 💼 Top Salespeople by Revenue", "top_salespeople.jpg",
     "- Ches Bonnell leads with $320K+\n- 6 people > $300K\n- Tight performance range",
     """
This chart presents revenue by the top 10 chocolate salespeople.

Ches Bonnell is the highest with 320,901. Oby Sorrel (316,645) and Madelen Upcott (316,099) follow closely. Brien Boise, Kelci Walkden, and Van Tuxwell also passed the 300K mark.

Dennison Crosswaite (291,669) and Beverie Moffet (278,922) were mid-tier. Kaine Padly (266,490) and Marney O’Breen (259,742) complete the list.

The data reveals high-performing staff with minimal gaps.
     """)
]

# === RENDER EACH CHART ===
for title, img_file, summary, description in charts:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown(f"### {title}")
    col1, col2 = st.columns([1.8, 1.2])

    with col1:
        st.markdown(summary)
        with st.expander("📘 Click to read full insights"):
            st.markdown(description)

    with col2:
        img = Image.open(f"homepage_folder/{img_file}")
        st.image(img, caption=title, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# === FOOTER ===
st.success("✅ Dashboard loaded with insights and visuals – great job!")
