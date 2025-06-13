import streamlit as st
from PIL import Image
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title="Explore our code", page_icon="🔍", layout="wide")

st.title("🔍 Explore our code")
st.subheader("📎 Instructor & Course Information")

# Giới thiệu nhóm
st.markdown("### 🧑‍🤝‍🧑 Meet Our Team")

# Chia layout thành 4 cột
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("nguyen.png", use_column_width=True)
    st.markdown("**Phan Nhật Nguyên**")
    st.write("ID: 106240514")
    st.write("Program: BBA")
    st.write("Email: [106240514@student.vgu.edu.vn](mailto:106240514@student.vgu.edu.vn)")

with col2:
    st.image("phuong.png", use_column_width=True)
    st.markdown("**Phạm Lê Trúc Phương**")
    st.write("ID: 106240422")
    st.write("Program: BBA")
    st.write("Email: [106240422@student.vgu.edu.vn](mailto:106240422@student.vgu.edu.vn)")

with col3:
    st.image("nhu.png", use_column_width=True)
    st.markdown("**Hồ Quỳnh Như**")
    st.write("ID: 103240278")
    st.write("Program: BFA")
    st.write("Email: [103240278@student.vgu.edu.vn](mailto:103240278@student.vgu.edu.vn)")

with col4:
    st.image("ngoc.png", use_column_width=True)
    st.markdown("**Hà Bích Ngọc**")
    st.write("ID: 106240020")
    st.write("Program: BBA")
    st.write("Email: [106240020@student.vgu.edu.vn](mailto:106240020@student.vgu.edu.vn)")

# Nhạc nền
st.markdown("### 🎵 Chill Background Music")
st.audio("music.mp3")

# Mưa emoji
rain(
    emoji="✨",
    font_size=40,
    falling_speed=5,
    animation_length="3",
)

# Lời cảm ơn
colored_header(
    label="Thank you for visiting!",
    description="If you have questions, feel free to reach out by email.",
    color_name="blue-green"
)
