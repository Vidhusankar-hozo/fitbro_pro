import streamlit as st
import random
import requests

st.markdown("## 🤖 FitBro ChatBot – Your Smart Fitness + Wellness Coach")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Optional API Key (Free if you register at https://api-ninjas.com)
API_NINJAS_KEY = "VD2rCWR7wKnJYicECdB7IQ==PD6itUqwLev8y4z4"  # can leave blank for now

def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        data = res.json()
        return f"{data[0]['q']} — *{data[0]['a']}*"
    except:
        return "Keep going, you’re doing better than you think. 🚀"

def get_exercise(bodypart="chest"):
    if not API_NINJAS_KEY:
        return "⚠️ Workout suggestions need an API key from api-ninjas.com (free)."
    try:
        res = requests.get(
            f"https://api.api-ninjas.com/v1/exercises?muscle={bodypart}",
            headers={"X-Api-Key": API_NINJAS_KEY}
        )
        data = res.json()
        if not data:
            return "😕 Couldn't find workouts for that muscle group."
        return "\\n".join([f"🏋️ {ex['name'].title()}: {ex['instructions'][:100]}..." for ex in data[:2]])
    except:
        return "⚠️ Error fetching exercise data."

def get_food_info(food="oats"):
    try:
        res = requests.get(f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={food}&search_simple=1&action=process&json=1")
        data = res.json()
        if data["count"] == 0:
            return "🍽️ Nutrition info not found. Try a common item like milk, oats, egg, or rice."

        product = data["products"][0]
        name = product.get("product_name", food)
        kcal = product.get("nutriments", {}).get("energy-kcal_100g", "N/A")
        proteins = product.get("nutriments", {}).get("proteins_100g", "N/A")
        return f"🍽️ **{name.title()}** → {kcal} kcal / 100g, {proteins}g protein"
    except Exception as e:
        return "⚠️ Could not fetch nutrition info right now."


def get_bored_suggestion():
    try:
        res = requests.get("https://www.boredapi.com/api/activity")
        return "🧘 " + res.json()["activity"]
    except:
        return "Take a walk, stretch, or listen to calming music 🎧"

def get_smart_reply(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["workout", "exercise", "train", "gym"]):
        # 🧠 Map friendly terms to actual API muscle names
        muscle_map = {
            "arms": "biceps",
            "abs": "abdominals",
            "core": "abdominals",
            "back": "middle_back",
            "chest": "chest",
            "legs": "legs",
            "shoulders": "shoulders",
            "triceps": "triceps",
            "biceps": "biceps"
        }
        body = "chest"  # default muscle
        for word in muscle_map:
            if word in user_input:
                body = muscle_map[word]
                break
        return get_exercise(body)

  elif any(word in user_input for word in ["calorie", "nutrition", "eat", "food", "kcal", "protein"]):
    # Try to extract known foods from user input
    for item in ["apple", "banana", "egg", "milk", "rice", "chicken", "oats", "biryani", "peanut butter"]:
        if item in user_input:
            return get_food_info(item)
    # If no known food matched, use whole user_input as the food name
    return get_food_info(user_input)


    elif any(word in user_input for word in ["motivate", "motivation", "quote", "inspire"]):
        return get_quote()

    elif any(word in user_input for word in ["bored", "stress", "tired", "low", "sad"]):
        return get_bored_suggestion()

    elif "sleep" in user_input:
        return "😴 Tip: Avoid screens 30 min before bed and stick to a sleep routine."

    else:
        return random.choice([
            "How are you feeling today? Want to talk food, mood, or movement?",
            "Your health is your power, bro. Let’s build it together 💪",
            "Need a meal tip, workout plan, or just a mental reset?"
        ])


# Chat form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("👨‍💻 You:")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        reply = get_smart_reply(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("FitBro Bot", reply))

# Display chat
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender if sender == "You" else "assistant"):
        st.markdown(message)
