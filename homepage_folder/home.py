import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="🍫 Chocolate Sales Analysis",
    page_icon="🍩",
    layout="wide"
)

# ==== CUSTOM CSS ====
st.markdown("""
    <style>
        body {
            background-color: #f8f3ef;
        }
        .big-title {
            font-size: 48px;
            font-weight: bold;
            color: #6f4e37;
        }
        .section-header {
            font-size: 30px;
            font-weight: bold;
            color: #4d2600;
        }
        .team-box {
            text-align: center;
            padding-top: 10px;
            font-size: 16px;
            color: #333;
        }
        .choco-fall {
            position: fixed;
            top: -10px;
            z-index: 9999;
            animation: fall 10s linear infinite;
        }
        @keyframes fall {
            0% { top: -10px; opacity: 1; }
            100% { top: 100vh; opacity: 0; }
        }
    </style>
""", unsafe_allow_html=True)

# ==== CHOCOLATE FALLING EFFECT ====
st.markdown("""
<script>
const chocolates = Array.from({length: 30}, () => {
    const choco = document.createElement('div');
    choco.className = 'choco-fall';
    choco.textContent = '🍫';
    choco.style.left = Math.random() * 100 + 'vw';
    choco.style.animationDelay = Math.random() * 10 + 's';
    choco.style.fontSize = (Math.random() * 10 + 15) + 'px';
    choco.style.position = 'fixed';
    choco.style.color = '#6f4e37';
    document.body.appendChild(choco);
});
</script>
""", unsafe_allow_html=True)

# ==== TITLE ====
st.markdown("<div class='big-title'>🍫 Chocolate Sales Analysis</div>", unsafe_allow_html=True)
st.markdown("### BUSINESS IT2: PYTHON 2 PROJECT")

# ==== PROJECT DESCRIPTION ====
st.write("""
We chose to analyze chocolate sales data because chocolate is a widely consumed product with strong market demand.  
By exploring this dataset, we aim to uncover trends in consumer behavior, identify best-selling products, and determine the most effective sales periods.  
This project also helps us sharpen our data analysis skills and derive valuable business insights that can be applied in real-world contexts.
""")

st.markdown("[🔗 View Original Dataset on Kaggle](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales)")

# ==== INSTRUCTOR INFO ====
with st.expander("📌 Instructor & Course Information"):
    st.write("**Instructor:** Mr. Đỗ Đức Tân")
    st.write("**Course:** Business IT2 - Python 2 Project")
    st.write("**University:** Vietnamese-German University")

# ==== TEAM SECTION ====
st.markdown("<div class='section-header'>🧑‍🤝‍🧑 Meet Our Team</div>", unsafe_allow_html=True)

cols = st.columns(4)

with cols[0]:
    st.image("homepage_folder/PNN.jpg", width=250)
    st.markdown("""
    <div class='team-box'>
        <strong>Phan Nhật Nguyên</strong><br>
        ID: 106240514<br>
        Program: BBA<br>
        Email: 106240514@student.vgu.edu.vn
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.image("homepage_folder/TP.jpg", width=250)
    st.markdown("""
    <div class='team-box'>
        <strong>Phạm Lê Trúc Phương</strong><br>
        ID: 106240422<br>
        Program: BBA<br>
        Email: 106240422@student.vgu.edu.vn
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.image("homepage_folder/HQN.jpg", width=250)
    st.markdown("""
    <div class='team-box'>
        <strong>Hồ Quỳnh Như</strong><br>
        ID: 103240278<br>
        Program: BFA<br>
        Email: 103240278@student.vgu.edu.vn
    </div>
    """, unsafe_allow_html=True)

with cols[3]:
    st.image("homepage_folder/HBN.jpg", width=250)
    st.markdown("""
    <div class='team-box'>
        <strong>Hà Bích Ngọc</strong><br>
        ID: 106240020<br>
        Program: BBA<br>
        Email: 106240020@student.vgu.edu.vn
    </div>
    """, unsafe_allow_html=True)

# ==== BACKGROUND MUSIC ====
st.markdown("### 🎵 Chill Background Music")
st.markdown("""
<audio controls autoplay loop>
  <source src="https://www.bensound.com/bensound-music/bensound-slowmotion.mp3" type="audio/mp3">
  Your browser does not support the audio element.
</audio>
""", unsafe_allow_html=True)
