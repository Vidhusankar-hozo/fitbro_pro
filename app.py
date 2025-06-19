# 1. Import + page config
import streamlit as st

st.set_page_config(
    page_title="FitBro Pro 💪",
    page_icon="💪",
    layout="wide"
)

# 2. Main Title + Subtitle
st.markdown("<h1 class='main-title'>💪 FitBro Pro</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track workouts, log meals, monitor weight, and talk with your AI bro</div>", unsafe_allow_html=True)

# ✅ 🔥 3. ADD GIF GALLERY HERE:
st.divider()
st.subheader("🔥 Stay Motivated")

gif_urls = [
    "https://cdn.dribbble.com/users/214068/screenshots/3861570/fitness-loader.gif",
    "https://i.pinimg.com/originals/43/84/d5/4384d5a6a1ae20e508ff8c1a489ad202.gif",
    "https://darebee.com/images/stories/banners/banner-fitness-the-moment.jpg",
    "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/16f6f980484165.5c644d9e0b1e6.gif"
]

cols = st.columns(4)
for idx, col in enumerate(cols):
    with col:
        st.image(gif_urls[idx], use_container_width=True)

# 4. Navigation links
st.divider()
st.subheader("🚀 Quick Access")

# Continue your existing columns and links here...


# --- App Navigation Cards ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>🏋️‍♂️</div>", unsafe_allow_html=True)
    st.page_link("pages/1_🏋️_Workouts.py", label="Log Workout", icon="🏋️‍♂️")
    
    st.markdown("<div class='card'>🍱</div>", unsafe_allow_html=True)
    st.page_link("pages/2_🍱_Meals.py", label="Meals & Calories", icon="🍱")

with col2:
    st.markdown("<div class='card'>📉</div>", unsafe_allow_html=True)
    st.page_link("pages/3_📉_Weight.py", label="Track Weight", icon="📉")

    st.markdown("<div class='card'>😴</div>", unsafe_allow_html=True)
    st.page_link("pages/4_😴_Sleep_Mood.py", label="Sleep & Mood", icon="😴")

with col3:
    st.markdown("<div class='card'>🤖</div>", unsafe_allow_html=True)
    st.page_link("pages/5_🤖_ChatBot.py", label="Ask FitBro", icon="🤖")

st.divider()

# --- Motivational Quote ---
st.markdown("<div class='quote'>“Discipline is choosing between what you want now and what you want most.”</div>", unsafe_allow_html=True)

st.caption("🔧 Built by Vidhusankar with ❤️ | Powered by Streamlit")
