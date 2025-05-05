import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Chocolate Sales Analysis",
    page_icon="🍫",
    layout="wide"
)

# ===== TITLE =====
st.markdown("<h1 style='color:#5D3A00;'>🍫 Chocolate Sales Analysis</h1>", unsafe_allow_html=True)
st.subheader("BUSINESS IT2: PYTHON 2 PROJECT 🔍")

st.write("""
We chose to analyze chocolate sales data because chocolate is a widely consumed product with strong market demand.  
By exploring this dataset, we aim to uncover trends in consumer behavior, identify best-selling products, and determine the most effective sales periods.  
This project also helps us sharpen our data analysis skills and derive valuable business insights that can be applied in real-world contexts.
""")

st.markdown("📎 [View Original Dataset on Kaggle](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales)")

with st.expander("📌 Instructor & Course Information"):
    st.write("""
    - **Instructor**: Mr. Đỗ Đức Tân  
    - **Course**: Business IT 2 – Python 2  
    - **University**: Vietnamese-German University (VGU)  
    - **Semester**: Spring 2025  
    """)

# ===== MEET OUR TEAM =====
st.markdown("---")
st.markdown("## 👫 Meet Our Team")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("homepage_folder/PNN.jpg", width=200)
    st.markdown("**Phan Nhật Nguyên**  \nID: 106240514  \nProgram: BBA  \nEmail: 106240514@student.vgu.edu.vn")

with col2:
    st.image("homepage_folder/TP.jpg", width=200)
    st.markdown("**Phạm Lê Trúc Phương**  \nID: 106240422  \nProgram: BBA  \nEmail: 106240422@student.vgu.edu.vn")

with col3:
    st.image("homepage_folder/HQN.jpg", width=200)
    st.markdown("**Hồ Quỳnh Như**  \nID: 103240278  \nProgram: BFA  \nEmail: 103240278@student.vgu.edu.vn")

with col4:
    st.image("homepage_folder/HBN.jpg", width=200)
    st.markdown("**Hà Bích Ngọc**  \nID: 106240020  \nProgram: BBA  \nEmail: 106240020@student.vgu.edu.vn")

# ===== MUSIC =====
st.markdown("---")
st.markdown("### 🎵 Chill Background Music")
st.markdown("""
<audio controls autoplay loop>
  <source src="https://www.bensound.com/bensound-music/bensound-slowmotion.mp3" type="audio/mp3">
  Your browser does not support the audio element.
</audio>
""", unsafe_allow_html=True)

# ===== FEEDBACK SECTION =====
st.markdown("---")
st.markdown("## 💬 We’d Love Your Feedback!")
st.info("If you enjoyed our project or have any suggestions, please let us know by contacting one of our team members. Your feedback is greatly appreciated! 🙌")

# ===== SNOW EFFECT =====
st.markdown("""
<style>
.snowflake {
  position: fixed;
  color: #fff;
  user-select: none;
  z-index: 9999;
  animation: fall 10s linear infinite;
}
@keyframes fall {
  0% { top: -10px; }
  100% { top: 100vh; }
}
</style>
<script>
const snowflakes = Array.from({length: 30}, () => {
  const snow = document.createElement('div');
  snow.className = 'snowflake';
  snow.textContent = '❄';
  snow.style.left = Math.random() * 100 + 'vw';
  snow.style.fontSize = (Math.random() * 10 + 10) + 'px';
  snow.style.animationDuration = (Math.random() * 5 + 5) + 's';
  document.body.appendChild(snow);
});
</script>
""", unsafe_allow_html=True)
