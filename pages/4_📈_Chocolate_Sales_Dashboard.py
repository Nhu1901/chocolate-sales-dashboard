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
The pie chart illustrates the proportion of bins shipped for the 10 high-quality-selling chocolate products, giving insight into their relative reputation.

Overall, the distribution is enormously even, with out a unmarried product dominating the market. However, 50% Dark Bites holds the biggest share, even as the remaining merchandise exhibit only minor variations in their proportions.

To begin with, 50% Dark Bites debts for the best share at eleven.3%, making it the top-selling object some of the ten. This is accompanied closely by Smooth Silky Salty (10.2%), Eclairs (10.1%), and Caramel Stuffed Bars (10.1%). All of these products exceed the ten% mark, indicating a robust consumer desire.

Meanwhile, Drinking Coco and Spicy Special Slims every contribute 10.0% to the total income, putting them within the mid-range. Similarly, Milk Bars and Peanut Butter Cubes sign in identical stocks at nine.6%, barely below the 10% threshold.

At the lower cease of the rating, After Nines and White Choc both make up nine.Five% of total income, although the gap between the best and lowest proportions is minimal—simply underneath 2%.

In conclusion, even though 50% Dark Bites is the maximum famous product, the pie chart exhibits a fairly balanced distribution some of the top 10 first-class-sellers, suggesting that consumer alternatives are incredibly numerous across chocolate types.
     """),

    # BAR CHART BY COUNTRY
    ("2. 🌍 Total Revenue by Country", "revenue_by_country.jpg",
     "- Australia tops with $1.05M\n- UK & India nearly equal\n- All countries > $950K",
     """
The bar chart compares the full sales from chocolate sales across six different nations: Australia, the UK, India, the united states, Canada, and New Zealand.

It is right now obvious that Australia generated the highest revenue, at the same time as New Zealand accounted for the bottom. Despite a few variant, all nations recorded enormously excessive income figures, with revenues fluctuating inside a narrow range across the one million greenback mark.

Specifically, Australia crowned the listing with overall revenue marginally exceeding $1.05 million. The UK and India accompanied carefully, every generating just over $1 million, indicating a sturdy and nearly equal marketplace presence. The USA ranked fourth, additionally reporting a parent in the identical variety, only barely decrease than that of India and the United Kingdom.

Meanwhile, Canada and New Zealand recorded the least sales many of the six countries. Canada’s figure fell just brief of the 1,000,000 dollar threshold, while New Zealand, even though simplest barely at the back of, introduced within the lowest income average, with a total of about $950,000.

In precis, the chart well-knownshows that chocolate sales are sturdy throughout all international locations provided, with Australia emerging because the most rewarding marketplace and New Zealand trailing slightly behind the relaxation. The relatively small disparity among the highest and lowest figures shows a consistently excessive call for for chocolate products in all six nations.
     """),

    # LINE CHART
    ("3. 📈 Monthly Sales Trend", "monthly_trend.jpg",
     "- Peaks: Feb & July\n- Lowest: March\n- Seasonal trends visible",
     """
The line graph affords the monthly fashion in chocolate container shipments from February to September 2022.

Overall, the trend suggests significant fluctuations in monthly income. The range of packing containers shipped began at a top in February, dropped sharply in March, after which experienced a slow restoration before peaking again in July, accompanied via a steady decline closer to September.

In element, the very best number of boxes turned into shipped in February 2022, reaching almost 28,000 gadgets. However, this figure declined significantly in the following month, hitting a low of round 18,000 in March — the bottom point within the period found.

From March onwards, sales step by step improved over the next four months. Shipments rose to approximately 19,500 in April, 21,000 in May, and 22,000 in June. This upward trend culminated in July, where income peaked once more at over 26,000 bins, marking the second one-maximum fee for the duration of the duration.

However, this healing turned into short-lived, as shipments fell over again, losing to round 23,000 in August after which to simply under 20,000 by using September.

In conclusion, while chocolate field shipments commenced and ended the length at excessive and coffee tiers respectively, the trend changed into characterised by means of one giant drop in early months and any other considerable decline after a mid-yr restoration.
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
