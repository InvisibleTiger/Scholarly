import streamlit as st
import yaml
import os

# Path to the YAML file
yaml_path = 'pages/data/flashcards.yaml'

# Function to load or create the YAML file
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

# Function to save data to the YAML file
def save_to_yaml(filename, data):
    with open(filename, "w") as file:
        yaml.dump(data, file)

# Initialize the session state for the user if it doesn't exist
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

if st.session_state.current_user is None:
    st.write("Please sign in to access your flashcards.")
else:
    # Load or create the flashcards YAML file
    flashcards_data = load_or_create_yaml(yaml_path, {})

    # Ensure the current user has an entry in the flashcards data
    if st.session_state.current_user not in flashcards_data:
        flashcards_data[st.session_state.current_user] = []

    # Display the flashcards
    st.title("Flashcard Maker")
    
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
    
    # Add new flashcard
    st.header("Add New Flashcard")
    front = st.text_input("Front")
    back = st.text_input("Back")
    
    if st.button("Add Flashcard"):
        if front and back:
            flashcards_data[st.session_state.current_user].append({"front": front, "back": back})
            save_to_yaml(yaml_path, flashcards_data)
            st.success("Flashcard added successfully!")
            # Update the session state to reflect the new flashcard
            st.rerun()
        else:
            st.error("Please fill in both fields.")