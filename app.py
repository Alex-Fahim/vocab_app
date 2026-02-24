import streamlit as st
import random

st.set_page_config(page_title="Vocabulary Practice", page_icon="📝", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>
body { background-color: black; }
.big-word { text-align: center; color: white; font-size: 36px; margin-bottom: 20px; }
.result { text-align: center; font-size: 24px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Vocabulary Practice</h1>", unsafe_allow_html=True)

# ---------- Load Words ----------
words = {}
with open("words.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "," in line:
            eng, bn = line.strip().split(",", 1)
            words[eng.strip()] = bn.strip()

# ---------- Session State ----------
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(list(words.keys()))
if "message" not in st.session_state:
    st.session_state.message = ""

# ---------- Show Word ----------
st.markdown(f"<div class='big-word'>{st.session_state.current_word}</div>", unsafe_allow_html=True)

# ---------- Form (IMPORTANT PART) ----------
with st.form("vocab_form", clear_on_submit=True):

    user_input = st.text_input("Enter Bangla")

    col1, col2 = st.columns(2)

    with col1:
        check_btn = st.form_submit_button("Check")

    with col2:
        next_btn = st.form_submit_button("Next")

    if check_btn:
        correct = words[st.session_state.current_word]
        if user_input.strip() == correct:
            st.session_state.message = "সঠিক ✅"
        else:
            st.session_state.message = f"ভুল ❌ | সঠিক: {correct}"

    if next_btn:
        st.session_state.current_word = random.choice(list(words.keys()))
        st.session_state.message = ""
        st.rerun()   # Clean rerun, no error

# ---------- Show Result ----------
st.markdown(f"<div class='result'>{st.session_state.message}</div>", unsafe_allow_html=True)

