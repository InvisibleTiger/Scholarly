import streamlit as st
import time
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Timer by Scholarly", layout="centered", page_icon="⌛")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.dialog("⌛ Timer by Scholarly")
def instructions():
    st.markdown("""    
    ### How to Use the Timer:
    1. **Number of Study Sessions**: Input how many study sessions you want to have.
    2. **Session Length**: Set the length of each study session in minutes.
    3. **Break Length**: Set the length of breaks between study sessions in minutes.
    4. Click **Start Pomodoro Timer** to begin your sessions. The app will guide you through each session and break.
    
    Enjoy your productive study time!
    """)

if 'instructions_shown' not in st.session_state:
    st.session_state['instructions_shown'] = False

if not st.session_state['instructions_shown']:
    instructions()
    st.session_state['instructions_shown'] = True

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the timer.")
else:
    st.title("⌛ Timer by Scholarly")

    timer = load_lottiefile("pages/assets/timer.json")
    st_lottie(timer, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

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