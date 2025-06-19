import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)
LOG_FILE = "data/workout_log.csv"

st.title("📓 Workout Logger")
st.write("Track your daily workouts and see your progress over time.")

# Input fields
exercise = st.text_input("🏋️ Exercise Name")
duration = st.number_input("⏱️ Duration (minutes)", min_value=1, max_value=500, step=1)
muscle_group = st.selectbox("💪 Muscle Group", ["Chest", "Back", "Legs", "Biceps", "Triceps", "Shoulders", "Abs", "Cardio"])
date = st.date_input("📅 Workout Date", value=datetime.today())

if st.button("✅ Log Workout"):
    if exercise:
        # Save entry
        entry = {
            "Date": date.strftime("%Y-%m-%d"),
            "Exercise": exercise,
            "Duration (min)": duration,
            "Muscle Group": muscle_group
        }
        df = pd.DataFrame([entry])

        # Append to CSV
        if os.path.exists(LOG_FILE):
            df.to_csv(LOG_FILE, mode="a", header=False, index=False)
        else:
            df.to_csv(LOG_FILE, index=False)

        st.success(f"Logged: {exercise} for {duration} min on {date}")
    else:
        st.warning("Please enter an exercise name.")

# Show history
st.subheader("📊 Workout History")

if os.path.exists(LOG_FILE):
    log_df = pd.read_csv(LOG_FILE)
    st.dataframe(log_df)
else:
    st.info("No workouts logged yet.")
