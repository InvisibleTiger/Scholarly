import streamlit as st
import time

st.title("Study Planner")

study_sessions = st.number_input("Number of Study Sessions", min_value=1, value=1)
session_length = st.number_input("Session Length (minutes)", min_value=1, value=25)
break_length = st.number_input("Break Length (minutes)", min_value=1, value=5)

if st.button("Start Pomodoro Timer"):
    for session in range(study_sessions):
        st.write(f"Session {session + 1}")
        with st.empty():
            for i in range(session_length * 60, 0, -1):
                st.metric("Time Left", f"{i // 60}:{i % 60:02d}")
                time.sleep(1)
        st.write("Time for a break!")
        with st.empty():
            for i in range(break_length * 60, 0, -1):
                st.metric("Break Time Left", f"{i // 60}:{i % 60:02d}")
                time.sleep(1)
        st.write("Break over, back to work!")