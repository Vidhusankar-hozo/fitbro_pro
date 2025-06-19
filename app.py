import streamlit as st

# Page config
st.set_page_config(
    page_title="FitBro Pro 💪",
    page_icon="💪",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 900;
            background: -webkit-linear-gradient(45deg, #ff3c3c, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 1rem;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.3rem;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .card {
            padding: 1.5rem;
            border-radius: 20px;
            background-color: #fefefe;
            border: 1px solid #ddd;
            box-shadow: 0 6px 12px rgba(0,0,0,0.08);
            margin-bottom: 1.5rem;
            text-align: center;
            transition: all 0.2s ease-in-out;
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 18px rgba(0,0,0,0.1);
        }
        .quote {
            font-style: italic;
            color: #444;
            text-align: center;
            font-size: 1.2rem;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title + Subtitle ---
st.markdown("<h1 class='main-title'>💪 FitBro Pro</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI-powered fitness, food & mental wellness tracker</div>", unsafe_allow_html=True)

# --- GIF Gallery ---
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
        try:
            st.image(gif_urls[idx], use_container_width=True)
        except:
            st.warning(f"⚠️ Image #{idx+1} couldn't load.")

# --- Navigation Cards ---
st.divider()
st.subheader("🚀 Quick Access")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown("<div class='card'>🏋️‍♂️</div>", unsafe_allow_html=True)
        st.page_link("pages/1_🏋️_Workouts.py", label="Log Workout", icon="🏋️‍♂️")

    with st.container():
        st.markdown("<div class='card'>🍱</div>", unsafe_allow_html=True)
        st.page_link("pages/2_🍱_Meals.py", label="Meals & Calories", icon="🍱")

with col2:
    with st.container():
        st.markdown("<div class='card'>📉</div>", unsafe_allow_html=True)
        st.page_link("pages/3_📉_Weight.py", label="Track Weight", icon="📉")

    with st.container():
        st.markdown("<div class='card'>😴</div>", unsafe_allow_html=True)
        st.page_link("pages/4_😴_Sleep_Mood.py", label="Sleep & Mood", icon="😴")

with col3:
    with st.container():
        st.markdown("<div class='card'>🤖</div>", unsafe_allow_html=True)
        st.page_link("pages/5_🤖_ChatBot.py", label="Ask FitBro", icon="🤖")

# --- Footer Quote ---
st.divider()
st.markdown("<div class='quote'>“Discipline is choosing between what you want now and what you want most.”</div>", unsafe_allow_html=True)
st.caption("🔧 Built by Vidhusankar with ❤️ | Powered by Streamlit")

