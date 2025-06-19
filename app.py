import streamlit as st

st.set_page_config(
    page_title="FitBro Pro 💪",
    page_icon="💪",
    layout="centered"
)

# --- HEADER / HERO SECTION ---
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #e63946;">💪 FitBro Pro</h1>
        <h4 style="color: #555;">Your AI-powered fitness, food & mental wellness companion</h4>
        <img src="https://cdn-icons-png.flaticon.com/512/1048/1048953.png" width="100">
        <p style="color: #999;">Track workouts, log meals, monitor weight, and chat with your AI bro!</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- QUICK ACCESS SECTIONS ---
st.subheader("🚀 Quick Access")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/2_📓_Workout_Logger.py", label="🏋️ Log Workout")
    st.page_link("pages/4_📈_Meal_Tracker.py", label="📈 Track Meals")
    st.page_link("pages/6_😴_Sleep_and_Mood_Tracker.py", label="😴 Sleep & Mood")

with col2:
    st.page_link("pages/3_🍽️_Meal_Logger.py", label="🍽️ Log Meal")
    st.page_link("pages/5_⚖️_Weight_Tracker.py", label="⚖️ Weight Tracker")
    st.page_link("pages/5_🤖_ChatBot.py", label="🤖 Ask FitBro")

# --- MOTIVATIONAL QUOTE ---
st.divider()
st.markdown("""
<div style="text-align: center; font-size: 20px; color: #444;">
    🧠 <i>“Your body can stand almost anything. It’s your mind you have to convince.”</i>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.caption("🔧 Built with ❤️ by Vidhusankar | Powered by Streamlit")
