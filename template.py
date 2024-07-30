import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottie_animation(file_path):
    with open(file_path, "r") as file:
        animation_data = json.load(file)
    st_lottie(animation_data, speed=1, width=400, height=400, key="animation")

animation_file_path = "assets/animation_placeholder.json"
load_lottie_animation(animation_file_path)

if 'first_time_running' not in st.session_state:
    st.session_state.first_time_running = True

if st.session_state.first_time_running:
    @st.dialog("Instructions")
    def instructions():
        st.markdown("""
            **Welcome to the Template App!**  
            Here are some instructions to help you get started:

            - **Section 1**: Add your content or functionality here.
            - **Section 2**: Configure any additional features or elements.
            - **Section 3**: Use this space to build out the core features of your app.
        """)

    instructions()
    st.session_state.first_time_running = False

st.title("Template App")

st.write("This is a placeholder for your app's UI.")
st.write("Replace this section with your app's functionality.")

if st.button("Example Button 1"):
    st.write("Button 1 clicked")

if st.button("Example Button 2"):
    st.write("Button 2 clicked")