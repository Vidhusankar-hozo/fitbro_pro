import streamlit as st
import pandas as pd
import os
from datetime import datetime, time

# File path
os.makedirs("data", exist_ok=True)
SLEEP_FILE = "data/sleep_mood_log.csv"

st.title("🧠 Sleep & Mood Tracker")
st.write("Track how you're feeling and how well you're resting.")

# Input fields
date = st.date_input("📅 Date", value=datetime.today())
bed_time = st.time_input("🛌 Bed Time", value=time(22, 0))
wake_time = st.time_input("⏰ Wake Time", value=time(6, 0))
mood = st.selectbox("😊 Mood Today", ["Great 😄", "Good 🙂", "Okay 😐", "Tired 😴", "Bad 😞"])

# Calculate sleep hours
sleep_duration = (
    datetime.combine(datetime.today(), wake_time) -
    datetime.combine(datetime.today(), bed_time)
).total_seconds() / 3600
if sleep_duration < 0:
    sleep_duration += 24

if st.button("✅ Log Sleep & Mood"):
    entry = {
        "Date": date.strftime("%Y-%m-%d"),
        "Bed Time": bed_time.strftime("%H:%M"),
        "Wake Time": wake_time.strftime("%H:%M"),
        "Sleep Hours": round(sleep_duration, 2),
        "Mood": mood
    }
    df = pd.DataFrame([entry])

    if os.path.exists(SLEEP_FILE):
        df.to_csv(SLEEP_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(SLEEP_FILE, index=False)

    st.success("✅ Sleep & mood logged successfully!")

# Display recent logs
st.subheader("📋 Recent Sleep & Mood Logs")

if os.path.exists(SLEEP_FILE):
    log_df = pd.read_csv(SLEEP_FILE)
    st.dataframe(log_df.tail(10))
else:
    st.info("No sleep or mood logs yet.")
