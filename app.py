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
    st.page_link("pages/1_🏋️_Workouts.py", label="🏋️ Log Workout")
    st.page_link("pages/2_🍱_Meals.py", label="🍱 Meals & Calories")
    st.page_link("pages/4_😴_Sleep_Mood.py", label="😴 Sleep & Mood")

with col2:
    st.page_link("pages/3_📉_Weight.py", label="📉 Track Weight")
    st.page_link("pages/5_🤖_ChatBot.py", label="🤖 Ask FitBro")

st.divider()
st.markdown("""
<div style="text-align: center; font-size: 18px;">
    🧠 <i>“Your body can stand almost anything. It’s your mind you have to convince.”</i>
</div>
""", unsafe_allow_html=True)

st.divider()
st.caption("🔧 Built with ❤️ by Vidhusankar | Powered by Streamlit")
