import streamlit as st
import pandas as pd
import os
from datetime import datetime
import altair as alt

# File path
os.makedirs("data", exist_ok=True)
WEIGHT_FILE = "data/weight_log.csv"

st.title("⚖️ Weight Tracker")
st.write("Log your weight daily and monitor your progress.")

# Input form
today = datetime.today().strftime("%Y-%m-%d")
weight = st.number_input("🏋️ Enter your weight (kg)", min_value=30.0, max_value=200.0, step=0.1)
date = st.date_input("📅 Date", value=datetime.today())

if st.button("✅ Log Weight"):
    df = pd.DataFrame([{
        "Date": date.strftime("%Y-%m-%d"),
        "Weight (kg)": weight
    }])
    if os.path.exists(WEIGHT_FILE):
        df.to_csv(WEIGHT_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(WEIGHT_FILE, index=False)
    st.success(f"Logged {weight} kg on {date.strftime('%Y-%m-%d')}")

# Display data
st.subheader("📋 Weight History")

if os.path.exists(WEIGHT_FILE):
    data = pd.read_csv(WEIGHT_FILE)
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date")
    st.dataframe(data.tail(10))  # Show recent 10 logs

    # Line chart
    chart = (
        alt.Chart(data)
        .mark_line(point=True, color="#4CAF50")
        .encode(
            x="Date:T",
            y="Weight (kg):Q",
            tooltip=["Date:T", "Weight (kg):Q"]
        )
        .properties(title="📈 Weight Progress Over Time", width=700, height=350)
    )
    st.altair_chart(chart)
else:
    st.info("No weight data yet.")
