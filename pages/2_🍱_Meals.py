import streamlit as st
import pandas as pd
import os
import altair as alt

MEAL_FILE = "data/meal_log.csv"

st.title("📈 Meal Tracker")
st.write("Visualize your daily calorie intake from meals.")

# Check if meal log exists
if not os.path.exists(MEAL_FILE):
    st.warning("No meal log found. Log some meals first!")
    st.stop()

# Load meal data
df = pd.read_csv(MEAL_FILE)

# Date filter
dates = sorted(df["Date"].unique(), reverse=True)
selected_date = st.selectbox("📅 Select Date", dates)

# Filter by selected date
filtered = df[df["Date"] == selected_date]

if filtered.empty:
    st.info("No meals logged on this date.")
else:
    st.subheader(f"🍱 Meals on {selected_date}")
    st.dataframe(filtered)

    # Calories per meal type
    bar_chart = (
        alt.Chart(filtered)
        .mark_bar(color="#FF5733")
        .encode(
            x="Meal Type:N",
            y="Calories:Q",
            tooltip=["Food", "Calories"]
        )
        .properties(width=600, height=300, title="🔥 Calories per Meal Type")
    )
    st.altair_chart(bar_chart)

    # Total kcal
    total_kcal = filtered["Calories"].sum()
    st.success(f"🔢 Total Calories for {selected_date}: **{total_kcal} kcal**")
