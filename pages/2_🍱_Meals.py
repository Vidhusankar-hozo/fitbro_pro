import streamlit as st
import pandas as pd
import os
from datetime import date
import altair as alt

MEAL_FILE = "data/meal_log.csv"

st.title("📈 Meal Tracker")
st.write("Analyze your eating habits and calorie intake.")

# Check if meal log exists
if not os.path.exists(MEAL_FILE):
    st.warning("No meals logged yet.")
    st.stop()

# Load data
df = pd.read_csv(MEAL_FILE)

# Date filter
dates = sorted(df["Date"].unique(), reverse=True)
selected_date = st.selectbox("📅 Select Date", dates)

# Filter data
filtered = df[df["Date"] == selected_date]

if filtered.empty:
    st.info("No meals logged on this date.")
else:
    st.subheader(f"🍽️ Meals on {selected_date}")
    st.dataframe(filtered)

    # Calories per meal type
    cal_chart = (
        alt.Chart(filtered)
        .mark_bar(color="#FF6666")
        .encode(
            x="Meal Type",
            y="Calories",
            tooltip=["Food", "Calories"]
        )
        .properties(width=600, height=300)
    )
    st.altair_chart(cal_chart)

    # Total calories
    total_kcal = filtered["Calories"].sum()
    st.success(f"🔥 Total calories for {selected_date}: **{total_kcal} kcal**")
