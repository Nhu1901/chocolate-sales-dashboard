import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Learn about our dataset", page_icon="📘", layout="wide")

# Title
st.title("📘 Learn About Our Dataset")
st.markdown("Welcome to our chocolate data exploration journey! 🍫")

# Load dataset
df = pd.read_csv("pages/Chocolate_data_sales.csv")
df["Amount"] = df["Amount"].replace('[\$,]', '', regex=True).astype(float)
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y", errors="coerce")
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# --- PROJECT OVERVIEW ---
st.markdown("----")
st.subheader("💡 Our Reason")
st.write("""
Chocolate is a beloved treat enjoyed by people all around the world. Its global popularity makes it not only a delightful product but also a powerful subject for business and consumer research. We decided to work with a chocolate sales dataset because it offers a fun and relatable topic while still being packed with real-world business potential. The idea of analyzing something familiar and widely appreciated adds both interest and practical value to our project.
""")

st.subheader("🎯 Our Goal")
st.write("""
Our main objective in working with this dataset is to uncover meaningful patterns in chocolate sales across different countries, seasons, and sales personnel. We aim to identify which chocolate products perform best in which regions, observe how sales change over time (such as during special events like Valentine’s Day), and analyze the impact of individual salespeople. By doing so, we hope to draw insights that could help companies make smarter decisions regarding product placement, marketing strategies, and sales planning.


""")

st.subheader("🛠️ Our Way")
st.write("""
To ensure accurate and insightful analysis, we began by cleaning the dataset — this included formatting dates, removing currency symbols, and preparing the data for analysis. We then extracted useful features like the month and year from each sales transaction. Using Python libraries such as Streamlit and Matplotlib, we designed a set of interactive tools and visualizations that allow users to filter and explore the data easily. These visualizations help present trends and relationships that would otherwise be hidden in raw data.
""")

st.subheader("🧾 Our Dataset")
st.write("""
The dataset we are working with contains transaction-level chocolate sales data, with essential fields like Product, Amount, Sales Person, Country, and Date. These fields allow us to explore not just how much was sold, but also where, by whom, and when. To deepen our analysis, we extracted additional time-based features such as Month and Year, which allow us to track sales patterns over time and detect seasonal trends or spikes.


""")

st.subheader("🔍 Our Findings")
st.write("""
Based on our initial analysis, we’ve already observed some interesting trends. Certain chocolate products are more popular in specific countries, hinting at regional preferences and tastes. Sales tend to spike in the early months of the year, especially around holidays like Valentine’s Day — a peak season for chocolate consumption. Moreover, our data suggests that successful salespersons often focus their efforts on promoting the right products in high-demand markets, which could be a key factor in their success.


""")

# --- FILTERS ---
st.markdown("----")
st.subheader("📊 Filter the Dataset")

st.sidebar.header("🔎 Filter Options")

country_option = st.sidebar.selectbox("Select Country", options=["All"] + sorted(df["Country"].dropna().unique().tolist()))
year_option = st.sidebar.selectbox("Select Year", options=["All"] + sorted(df["Year"].dropna().astype(int).unique().tolist()))
product_option = st.sidebar.selectbox("Select Product", options=["All"] + sorted(df["Product"].dropna().unique().tolist()))

# Apply filters
filtered_df = df.copy()
if country_option != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country_option]
if year_option != "All":
    filtered_df = filtered_df[filtered_df["Year"] == int(year_option)]
if product_option != "All":
    filtered_df = filtered_df[filtered_df["Product"] == product_option]

# --- PREVIEW & PIE CHART ---
st.markdown("----")
st.subheader("📋 Filtered Data & Pie Chart")

if filtered_df.empty:
    st.warning("⚠️ No data available for this combination of filters. Please try different options.")
else:
    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.dataframe(filtered_df, use_container_width=True)
    with col2:
        st.markdown("#### 🍩 Sales Distribution by Country")
        country_counts = filtered_df["Country"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(country_counts, labels=country_counts.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

# --- SUMMARY METRICS ---
st.markdown("----")
col3, col4, col5 = st.columns(3)
col3.metric("Total Records", f"{filtered_df.shape[0]}")
col4.metric("Total Revenue ($)", f"{filtered_df['Amount'].sum():,.2f}")
col5.metric("Unique Products", f"{filtered_df['Product'].nunique()}")

# --- FOOTER ---
st.markdown("----")
st.success("✅ This page gave us a clear understanding of the dataset and set the foundation for further analysis.")
