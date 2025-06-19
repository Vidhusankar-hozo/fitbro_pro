import streamlit as st
import random

st.markdown("## 🤖 Mental Fitness ChatBot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Simulated intelligent responses
def get_reply(user_input):
    responses = [
        "I'm here for you. Remember to take deep breaths. 🌿",
        "You're stronger than you think. Keep going 💪",
        "I'm listening... what's on your mind?",
        "Self-care isn't selfish. Prioritize yourself today ❤️",
        "Let's take one step at a time. You've got this!"
    ]
    if "sad" in user_input.lower():
        return "I'm sorry you're feeling down. Want to try a breathing exercise together?"
    elif "happy" in user_input.lower():
        return "That's awesome! Celebrate even the small wins 🎉"
    else:
        return random.choice(responses)

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your thoughts here:")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        reply = get_reply(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("FitBro Bot", reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender if sender == "You" else "assistant"):
        st.markdown(message)
