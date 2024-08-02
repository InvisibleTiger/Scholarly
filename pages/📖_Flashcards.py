import streamlit as st
import yaml
import os
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Flashcards by Scholarly", layout="centered", page_icon="📖")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.dialog("📖 Flashcards by Scholarly")
def instructions():
    st.markdown("""    
    ### How to Use the App:
    1. **View Flashcards**: Expand each flashcard to view its contents.
    2. **Remove Flashcards**: Click the 'Remove Flashcard' button to delete a flashcard.
    3. **Add Flashcards**: Use the form at the bottom to add new flashcards by providing the front and back text.
    
    Keep your learning efficient and organized!
    """)

yaml_path = 'pages/data/flashcards.yaml'

def load_or_create_yaml(filename, default_data):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = yaml.safe_load(file)
                if not isinstance(data, dict):
                    data = {}
            except yaml.YAMLError:
                data = {}
        return data
    else:
        with open(filename, "w") as file:
            yaml.dump(default_data, file)
        return default_data

def save_to_yaml(filename, data):
    with open(filename, "w") as file:
        yaml.dump(data, file)

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if st.session_state.current_user is None:
    st.warning("Please sign in to access your flashcards.")
else:
    if 'flashcards_instructions_shown' not in st.session_state:
        st.session_state['flashcards_instructions_shown'] = False

    if not st.session_state['flashcards_instructions_shown']:
        instructions()
        st.session_state['flashcards_instructions_shown'] = True

    flashcards_data = load_or_create_yaml(yaml_path, {})

    if st.session_state.current_user not in flashcards_data:
        flashcards_data[st.session_state.current_user] = []

    st.title("📖 Flashcards by Scholarly")

    flashcards = load_lottiefile("pages/assets/flashcards.json")
    st_lottie(flashcards, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    
    st.header("Your Flashcards")
    if flashcards_data[st.session_state.current_user]:
        for i, flashcard in enumerate(flashcards_data[st.session_state.current_user]):
            with st.expander(f"Flashcard {i + 1}: {flashcard['front']}"):
                st.write(f"**Back:** {flashcard['back']}")
                if st.button(f"Remove Flashcard {i + 1}", key=f"remove_{i}"):
                    del flashcards_data[st.session_state.current_user][i]
                    save_to_yaml(yaml_path, flashcards_data)
                    st.success("Flashcard removed successfully!")
                    st.rerun()
    else:
        st.write("No flashcards available.")
    
    st.header("Add New Flashcard")
    front = st.text_input("Front")
    back = st.text_input("Back")
    
    if st.button("Add Flashcard"):
        if front and back:
            flashcards_data[st.session_state.current_user].append({"front": front, "back": back})
            save_to_yaml(yaml_path, flashcards_data)
            st.success("Flashcard added successfully!")
            st.rerun()
        else:
            st.error("Please fill in both fields.")