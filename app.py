import streamlit as st
import random

st.set_page_config(page_title="Vocabulary Practice", page_icon="📝", layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>Vocabulary Practice</h1>", unsafe_allow_html=True)
st.markdown("<style>body{background-color: black;}</style>", unsafe_allow_html=True)

# Load words
words = {}
with open("words.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "," in line:
            eng, bn = line.strip().split(",", 1)
            words[eng.strip()] = bn.strip()

if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(words.keys()))
    st.session_state.message = ""

def check():
    answer = st.session_state.user_input.strip()
    correct = words[st.session_state.current_word]
    if answer == correct:
        st.session_state.message = "সঠিক ✅"
    else:
        st.session_state.message = f"ভুল ❌ | সঠিক: {correct}"
    st.session_state.current_word = random.choice(list(words.keys()))
    st.session_state.user_input = ""

st.text_input("Enter Bangla", key="user_input", on_change=check)
st.markdown(f"<h2 style='color:white;text-align:center;'>{st.session_state.current_word}</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:white;font-size:24px;'>{st.session_state.message}</p>", unsafe_allow_html=True)