
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="FitBro Pro", layout="centered")

with st.sidebar:
    selected = option_menu("FitBro Pro Menu", ["🏋️ Workouts", "🍱 Meals", "📉 Weight", "😴 Sleep & Mood", "🤖 ChatBot"],
        icons=["dumbbell", "egg-fried", "graph-down", "moon-stars", "robot"], menu_icon="person", default_index=0)

st.title("🏠 FitBro Pro")
st.markdown("Welcome to your upgraded Fitness & Mental Wellness Assistant 💪🧠")
st.info("Use the sidebar to navigate to different sections of your fitness journey.")
