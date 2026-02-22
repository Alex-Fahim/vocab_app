import streamlit as st
import random

st.set_page_config(page_title="Vocabulary Practice", page_icon="📝", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: black;
    }
    .big-word {
        text-align: center;
        color: white;
        font-size: 36px;
        margin-bottom: 20px;
    }
    .result {
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Vocabulary Practice</h1>", unsafe_allow_html=True)

# Load words
words = {}
with open("words.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "," in line:
            eng, bn = line.strip().split(",", 1)
            words[eng.strip()] = bn.strip()

# Session state
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(words.keys()))
if "message" not in st.session_state:
    st.session_state.message = ""

# Show current word
st.markdown(f"<div class='big-word'>{st.session_state.current_word}</div>", unsafe_allow_html=True)

# Input field
user_input = st.text_input("Enter Bangla")

# Button
if st.button("Check & Next"):
    correct = words[st.session_state.current_word]

    if user_input.strip() == correct:
        st.session_state.message = "সঠিক ✅"
    else:
        st.session_state.message = f"ভুল ❌ | সঠিক: {correct}"

    # Show result
    st.markdown(f"<div class='result'>{st.session_state.message}</div>", unsafe_allow_html=True)

    # Load next word
    st.session_state.current_word = random.choice(list(words.keys()))
