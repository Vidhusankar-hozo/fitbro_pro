import streamlit as st

st.set_page_config(
    page_title="FitBro Pro 💪",
    page_icon="💪",
    layout="centered"
)

st.title("💪 FitBro Pro")
st.markdown("Your AI-powered fitness, food & mental wellness companion.")

st.divider()
st.subheader("🚀 Quick Access")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/2_Workout_Logger.py", label="🏋️ Log Workout")
    st.page_link("pages/4_Meal_Tracker.py", label="📈 Track Meals")
    st.page_link("pages/6_Sleep_and_Mood_Tracker.py", label="😴 Sleep & Mood")

with col2:
    st.page_link("pages/3_Meal_Logger.py", label="🍽️ Log Meal")
    st.page_link("pages/5_Weight_Tracker.py", label="⚖️ Weight Tracker")
    st.page_link("pages/5_ChatBot.py", label="🤖 Ask FitBro")

st.divider()
st.markdown("""
<div style="text-align: center; font-size: 18px;">
    🧠 <i>“Your body can stand almost anything. It’s your mind you have to convince.”</i>
</div>
""", unsafe_allow_html=True)

st.divider()
st.caption("🔧 Built with ❤️ by Vidhusankar | Powered by Streamlit")
