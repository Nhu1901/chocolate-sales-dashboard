import streamlit as st

st.set_page_config(page_title="Explore Our Code", layout="wide")

# === HEADER ===
st.markdown("""
<h1 style='text-align: center;
           background: -webkit-linear-gradient(45deg, #FF6B6B, #FFD93D);
           -webkit-background-clip: text;
           -webkit-text-fill-color: transparent;
           font-size: 3em;'>
🔍 Explore Our Code
</h1>
""", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>✨ Dive into the brains behind our chocolate dashboard ✨</h4>", unsafe_allow_html=True)
# 📌 GENERAL NOTE TO TEACHER
st.info("ℹ️ Note: The code examples below are simplified summaries of key components used in each page. They are meant to demonstrate our coding structure and logic—not full implementations of each individual page with all design or interactivity.")

st.markdown("---")

# === DROPDOWN 1 ===
section = st.selectbox("🎯 Select a part of code to explore:", [
    "📊 Chart Visualization",
    "📁 Data Cleaning",
    "📦 Data Source",
    "👥 Meet Our Team"
])

if section == "📊 Chart Visualization":
    st.subheader("📊 Chart Visualization")
    st.code("""
import plotly.express as px

def create_sales_chart(df):
    fig = px.bar(df, x='Product', y='Revenue', title='Top-selling Products')
    st.plotly_chart(fig)
    """, language="python")

elif section == "📁 Data Cleaning":
    st.subheader("🧹 Data Cleaning")
    st.code("""
import pandas as pd

df = pd.read_csv("chocolate_data_sales.csv")
df["Amount"] = df["Amount"].replace('[\\$,]', '', regex=True).astype(float)
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
    """, language="python")

elif section == "📦 Data Source":
    st.subheader("📦 Data Source")
    st.markdown("""
- Dataset: [Kaggle - Chocolate Sales](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales)  
- File: `Chocolate_data_sales.csv`
    """)

elif section == "👥 Meet Our Team":
    st.subheader("👥 Meet Our Team")
    st.markdown("""
- Hồ Quỳnh Như – BFA – 103240278  
- Phạm Lê Trúc Phương – BBA – 106240422  
- Hà Bích Ngọc – BBA – 106240020  
- Phan Nhật Nguyên – BBA – 106240514
    """)

st.markdown("---")

# === DROPDOWN 2: FULL CODE ===
st.markdown("### 📘 Want to see the full source code of each page?")

page = st.selectbox("📄 Choose a page:", [
    "1️⃣ Chocolate Market",
    "2️⃣ Learn About Our Dataset",
    "3️⃣ Explore Our Code (this page)",
    "4️⃣ Chocolate Sales Dashboard"
])

if page == "1️⃣ Chocolate Market":
    st.subheader("📄 Full Code – Chocolate Market")
    st.code("""
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Chocolate Market & Fun Facts",
    page_icon="🍫",
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>🍫 Chocolate Market & Fun Facts</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explore how chocolate is loved around the world and enjoy some sweet facts!</p>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("🌍 Chocolate Around the World")
col1, col2 = st.columns([1.2, 1])
with col1:
    st.image("homepage_folder/map.jpg", caption="🗺️ Chocolate-Themed World Map", use_container_width=True)
with col2:
    st.markdown("...")
    
st.subheader("📊 Chocolate Consumption Per Capita")
col3, col4 = st.columns([1, 1.2])
with col3:
    st.markdown("...")
with col4:
    st.image("homepage_folder/chocolatemarket.jpg", use_container_width=True)

st.subheader("🍬 Fun Facts About Chocolate")
st.markdown("- 🎁 The first chocolate bar...")
""", language="python")

elif page == "2️⃣ Learn About Our Dataset":
    st.subheader("📄 Full Code – Learn About Our Dataset")
    st.code("""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Learn about our dataset", page_icon="📘", layout="wide")
st.title("📘 Learn About Our Dataset")
st.markdown("Welcome to our chocolate data exploration journey! 🍫")

df = pd.read_csv("pages/Chocolate_data_sales.csv")
df["Amount"] = df["Amount"].replace('[\\$,]', '', regex=True).astype(float)
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y", errors="coerce")
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Filters
country_option = st.sidebar.selectbox("Country", options=["All"] + sorted(df["Country"].dropna().unique()))
...

st.success("✅ This page gave us a clear understanding of the dataset.")
""", language="python")

elif page == "3️⃣ Explore Our Code (this page)":
    st.subheader("📄 Full Code – Explore Our Code")
    st.info("⚠️ You're already viewing this page!")

elif page == "4️⃣ Chocolate Sales Dashboard":
    st.subheader("📄 Full Code – Chocolate Sales Dashboard")
    st.code("""
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Chocolate Sales Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center;'>🍫 Chocolate Sales Dashboard 📊</h1>", unsafe_allow_html=True)

charts = [
    ("1. 🍬 Top Products", "top_products_pie.jpg", "- Summary", "Full analysis..."),
    ("2. 🌍 Revenue by Country", "revenue_by_country.jpg", "- Summary", "Full analysis..."),
    ("3. 📈 Monthly Trend", "monthly_trend.jpg", "- Summary", "Full analysis..."),
    ("4. 💼 Salespeople", "top_salespeople.jpg", "- Summary", "Full analysis...")
]

for title, img_file, summary, description in charts:
    st.markdown(f"### {title}")
    col1, col2 = st.columns([1.8, 1.2])
    with col1:
        st.markdown(summary)
        with st.expander("📘 Click to read full insights"):
            st.markdown(description)
    with col2:
        st.image(f"homepage_folder/{img_file}", use_container_width=True)

st.success("✅ Dashboard loaded with insights and visuals – great job!")
""", language="python")

st.markdown("---")
st.success("✅ You can now browse our actual project code, all in one place! 💡")

