import streamlit as st
import random

st.title("🎮 Number Guessing Game")

if 'random_number' not in st.session_state:
    st.session_state['random_number'] = random.randint(1, 100)
    st.session_state['attempts_left'] = 10
    st.session_state['game_over'] = False
    st.session_state['message'] = ""

st.subheader(f"Attempts Left: {st.session_state['attempts_left']}")

if not st.session_state['game_over']:
    guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

if st.button("Submit Guess") and not st.session_state['game_over']:
    if guess == st.session_state['random_number']:
        st.session_state['message'] = "🎉 Correct! You've guessed the number!"
        st.session_state['game_over'] = True
    elif guess < st.session_state['random_number']:
        st.session_state['message'] = "Too low! Try again."
        st.session_state['attempts_left'] -= 1
    else:
        st.session_state['message'] = "Too high! Try again."
        st.session_state['attempts_left'] -= 1

    if st.session_state['attempts_left'] == 0:
        st.session_state['message'] = f"😢 Game Over! The number was {st.session_state['random_number']}."
        st.session_state['game_over'] = True

st.write(st.session_state['message'])

if st.session_state['game_over']:
    if st.button("Play Again"):
        st.session_state['random_number'] = random.randint(1, 100)
        st.session_state['attempts_left'] = 10
        st.session_state['game_over'] = False
        st.session_state['message'] = ""
