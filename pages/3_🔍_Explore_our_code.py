import streamlit as st

st.title("🔍 Explore our code")

# Dropdown menu
option = st.selectbox(
    "Would you like to learn more about?",
    ("Homepage", "🍫 Chocolate Market", "📘 Learn about our dataset", "📈 Chocolate Sales Dashboard")
)

# Trang homepage thì không hiện gì thêm
if option == "Homepage":
    st.info("Please select one of the topics below to explore further.")

elif option == "🍫 Chocolate Market":
    st.subheader("🍫 Chocolate Market")
    st.write("""
        This section explores trends in the global chocolate industry, including production, 
        consumption, pricing, and market share of major brands.
    """)
    # Thêm biểu đồ / bảng nếu cần

elif option == "📘 Learn about our dataset":
    st.subheader("📘 Learn about our dataset")
    st.write("""
        Here we provide an overview of the dataset used in this project, including
        key features such as product names, sales figures, regions, and time frames.
    """)
    # Thêm bảng hiển thị dữ liệu nếu muốn

elif option == "📈 Chocolate Sales Dashboard":
    st.subheader("📈 Chocolate Sales Dashboard")
    st.write("""
        A visual dashboard presenting sales performance, market segmentation, and product trends.
    """)
    # Có thể hiển thị biểu đồ hoặc chuyển hướng người dùng đến dashboard
