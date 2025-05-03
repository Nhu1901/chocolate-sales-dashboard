import streamlit as st

# ==== SETUP PAGE ====
st.set_page_config(
    page_title="Chocolate Sales Analysis",
    page_icon="🍫",
    layout="wide"
)

# ==== BACKGROUND SNOW EFFECT ====
snow_gif_url = "https://i.gifer.com/7efs.gif"  # Link ảnh động tuyết rơi
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{snow_gif_url}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==== HEADER ====
st.title("🍫 Chocolate Sales Analysis")
st.markdown("### BUSINESS IT2: PYTHON 2 PROJECT")

st.markdown("""
We chose to analyze chocolate sales data because chocolate is a widely consumed product with strong market demand.  
By exploring this dataset, we aim to uncover trends in consumer behavior, identify best-selling products, and determine the most effective sales periods.  
This project also helps us sharpen our data analysis skills and derive valuable business insights that can be applied in real-world contexts.
""")

# ==== Instructor & Dataset Link ====
with st.expander("📌 Instructor & Course Information"):
    st.markdown("""
    - **Instructor**: Đỗ Đức Tân  
    - **Course**: BUSINESS IT2 – PYTHON 2 PROJECT  
    - **Dataset**: [Kaggle - Chocolate Sales](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales)
    """)

# ==== TEAM MEMBERS ====
st.markdown("## 👥 Meet Our Team")
st.markdown("Click on the images or read more below to get to know us!")

cols = st.columns(2)

with cols[0]:
    st.image("HQN.jpg", width=250, caption="Hồ Quỳnh Như")
    st.markdown("""
    **Full name:** Hồ Quỳnh Như  
    **Student ID:** 103240278  
    **Email:** [103240278@student.vgu.edu.vn](mailto:103240278@student.vgu.edu.vn)  
    **Study Program:** BFA
    """)

    st.image("PNN.jpg", width=250, caption="Phan Nhật Nguyên")
    st.markdown("""
    **Full name:** Phan Nhật Nguyên  
    **Student ID:** 106240514  
    **Email:** [106240514@student.vgu.edu.vn](mailto:106240514@student.vgu.edu.vn)  
    **Study Program:** BBA
    """)

with cols[1]:
    st.image("TP.jpg", width=250, caption="Phạm Lê Trúc Phương")
    st.markdown("""
    **Full name:** Phạm Lê Trúc Phương  
    **Student ID:** 106240422  
    **Email:** [106240422@student.vgu.edu.vn](mailto:106240422@student.vgu.edu.vn)  
    **Study Program:** BBA
    """)

    st.image("HBN.jpg", width=250, caption="Hà Bích Ngọc")
    st.markdown("""
    **Full name:** Hà Bích Ngọc  
    **Student ID:** 106240020  
    **Email:** [106240020@student.vgu.edu.vn](mailto:106240020@student.vgu.edu.vn)  
    **Study Program:** BBA
    """)

# ==== FEEDBACK FORM ====
st.markdown("---")
st.subheader("💬 Leave us your message!")
st.caption("Let us know if you have any recommendations.")

with st.form("feedback_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email address")
    message = st.text_area("What do you think?")
    send = st.form_submit_button("Send")
    if send:
        st.success("✅ Thank you! Your message has been received.")

# ==== BACKGROUND MUSIC ====
st.markdown("### 🎵 Chill Background Music")
st.markdown(
    """
    <audio controls autoplay loop>
      <source src="https://www.bensound.com/bensound-music/bensound-slowmotion.mp3" type="audio/mp3">
      Your browser does not support the audio element.
    </audio>
    """,
    unsafe_allow_html=True
)
