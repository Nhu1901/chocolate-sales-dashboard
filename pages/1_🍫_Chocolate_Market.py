import streamlit as st
from PIL import Image

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="Chocolate Market & Fun Facts",
    page_icon="🍫",
    layout="wide"
)

# ==== TITLE ====
st.markdown("<h1 style='text-align: center;'>🍫 Chocolate Market & Fun Facts</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Explore how chocolate is loved around the world and enjoy some sweet facts!</p>", unsafe_allow_html=True)
st.markdown("---")

# ==== SECTION 1: Chocolate Around the World ====
st.subheader("🌍 Chocolate Around the World")

col1, col2 = st.columns([1.2, 1])

with col1:
    st.image("homepage_folder/map.jpg", caption="🗺️ Chocolate-Themed World Map", use_container_width=True)

with col2:
    st.markdown("""
    - 🍫 **Chocolate is consumed globally**, but Europe dominates per capita consumption.
    - 🇨🇭 **Switzerland**, 🇩🇪 **Germany**, and 🇬🇧 **UK** are among the highest consumers.
    - 🌍 Cultural traditions, weather, and holidays all impact consumption.
    - 🍂 Colder countries tend to consume more chocolate per person.
    """)
    st.markdown("✨ *Is your country a chocolate lover?*")

st.markdown("---")

# ==== SECTION 2: Per Capita Consumption ====
st.subheader("📊 Chocolate Consumption Per Capita")

col3, col4 = st.columns([1, 1.2])

with col3:
    st.markdown("""
    According to **Statista**, here's how many kg of chocolate people consume annually:

    - 🇨🇭 **Switzerland**: 11.8 kg  
    - 🇺🇸 **USA**: 9.0 kg  
    - 🇩🇪 **Germany**: 5.8 kg  
    - 🇫🇷 **France**: 3.6 kg  
    - 🇬🇧 **UK**: 2.9 kg  
    - 🇧🇷 **Brazil**: 1.4 kg  
    - 🇮🇳 **India**: 1.0 kg  
    - 🇨🇳 **China**: 0.2 kg  
    """)

    st.markdown("> 📌 **Switzerland still wins the chocolate crown!**")

with col4:
    st.image("homepage_folder/chocolatemarket.jpg", caption="🍫 Per Capita Consumption by Country | Source: Statista", use_container_width=True)

st.markdown("---")

# ==== SECTION 3: Fun Facts ====
st.subheader("🍬 Fun Facts About Chocolate")

st.markdown("""
- 🎁 The first chocolate bar was created in the **1800s** in the UK.
- 🎂 **Chocolate cake** was originally considered a luxury in Europe.
- 📈 Global chocolate revenue exceeds **$100 billion** annually.
- 💝 Chocolate sales peak during **Valentine’s Day** and **Christmas**.
- 🧠 Eating chocolate **releases serotonin**, boosting your mood!
""")

st.success("🍀 Hope you had a sweet time learning! Check the sidebar for more 🍫 insights!")
