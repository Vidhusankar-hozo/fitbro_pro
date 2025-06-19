import streamlit as st

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
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #e63946, #f1faee);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            color: #6c757d;
            font-size: 1.2rem;
            margin-top: -10px;
        }
        .card {
            padding: 1.5rem;
            border-radius: 20px;
            background-color: #ffffff10;
            border: 1px solid #ccc;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            text-align: center;
        }
        .quote {
            font-style: italic;
            color: #495057;
            text-align: center;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title + Subtitle ---
st.markdown("<h1 class='main-title'>💪 FitBro Pro</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track workouts, log meals, monitor weight, and talk with your AI bro</div>", unsafe_allow_html=True)

st.divider()

# --- Hero Image ---
st.image("https://cdn.dribbble.com/users/149378/screenshots/6126105/fitness_app_dribble.gif", use_column_width=True)

st.divider()
st.subheader("🚀 Quick Access")

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
