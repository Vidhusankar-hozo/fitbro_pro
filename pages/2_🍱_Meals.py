import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Ensure data folder exists
os.makedirs("data", exist_ok=True)
MEAL_FILE = "data/meal_log.csv"

st.title("🍽️ Meal Logger")
st.write("Track what you eat and how many calories you're consuming.")

# Input fields
meal_type = st.selectbox("🍴 Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"])
food = st.text_input("🥗 Food Item")
calories = st.number_input("🔥 Calories (kcal)", min_value=0, max_value=2000, step=10)
meal_time = st.time_input("🕒 Time", value=datetime.now().time())
date = st.date_input("📅 Date", value=datetime.today())

if st.button("✅ Log Meal"):
    if food:
        entry = {
            "Date": date.strftime("%Y-%m-%d"),
            "Time": meal_time.strftime("%H:%M"),
            "Meal Type": meal_type,
            "Food": food,
            "Calories": calories
        }
        df = pd.DataFrame([entry])

        if os.path.exists(MEAL_FILE):
            df.to_csv(MEAL_FILE, mode="a", header=False, index=False)
        else:
            df.to_csv(MEAL_FILE, index=False)

        st.success(f"✅ Logged: {food} ({calories} kcal) for {meal_type}")
    else:
        st.warning("⚠️ Please enter the food item before logging.")

# Display meal history
st.subheader("📋 Recent Meal Logs")

if os.path.exists(MEAL_FILE):
    log_df = pd.read_csv(MEAL_FILE)
    st.dataframe(log_df.tail(10))
else:
    st.info("No meals logged yet.")
