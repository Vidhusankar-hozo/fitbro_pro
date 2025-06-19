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
            padding-top: 1rem;
        }
        .subtitle {
            text-align: center;
            color: #555;
            font-size: 1.3rem;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .card {
            padding: 1.2rem;
            border-radius: 16px;
            background-color: #fff;
            border: 1px solid #eee;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 1.2rem;
            text-align: center;
            transition: all 0.2s ease-in-out;
        }
        .card:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 15px rgba(0,0,0,0.08);
        }
        .quote {
            font-style: italic;
            color: #444;
            text-align: center;
            font-size: 1.2rem;
            margin-top: 2rem;
        }
        .main-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            max-width: 800px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title + Subtitle ---
st.markdown("<h1 class='main-title'>💪 FitBro Pro</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI-powered fitness, food & mental wellness tracker</div>", unsafe_allow_html=True)


# --- Hero Image ---
st.divider()
st.subheader("🔥 Let’s Crush Your Goals")

st.markdown("""
    <div style='text-align: center;'>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSpGzehCnQ2s2v_cORVK-X4ck9KBwfilixKg&s' 
             style='max-width: 800px; width: 100%; border-radius: 16px; box-shadow: 0 4px 18px rgba(0,0,0,0.2);' />
    </div>
""", unsafe_allow_html=True)


# --- Navigation Buttons ---
st.divider()
st.subheader("🚀 Quick Access")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown("<div class='card'>🏋️‍♂️</div>", unsafe_allow_html=True)
        if st.button("Log Workout", key="btn1"):
            st.switch_page("pages/1_🏋️_Workouts.py")

    with st.container():
        st.markdown("<div class='card'>🍱</div>", unsafe_allow_html=True)
        if st.button("Meals & Calories", key="btn2"):
            st.switch_page("pages/2_🍱_Meals.py")

with col2:
    with st.container():
        st.markdown("<div class='card'>📉</div>", unsafe_allow_html=True)
        if st.button("Track Weight", key="btn3"):
            st.switch_page("pages/3_📉_Weight.py")

    with st.container():
        st.markdown("<div class='card'>😴</div>", unsafe_allow_html=True)
        if st.button("Sleep & Mood", key="btn4"):
            st.switch_page("pages/4_😴_Sleep_Mood.py")

with col3:
    with st.container():
        st.markdown("<div class='card'>🤖</div>", unsafe_allow_html=True)
        if st.button("Ask FitBro", key="btn5"):
            st.switch_page("pages/5_🤖_ChatBot.py")

# --- Footer Quote ---
st.divider()
st.markdown("<div class='quote'>“Your body can stand almost anything. It’s your mind you have to convince.”</div>", unsafe_allow_html=True)
st.caption("🔧 Built by Vidhusankar with ❤️ | Powered by Streamlit")
