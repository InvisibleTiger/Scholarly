import streamlit as st
import yaml
import os
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="School Supplies", layout="centered", page_icon="🎒")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Path to the YAML file
SUPPLIES_PATH = 'pages/data/schoolsupplies.yaml'

# Load supplies from the YAML file
def load_supplies(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

# Function to display the recommended supplies
def display_supplies(supplies, grade):
    st.header(f"Recommended Supplies for {grade}")
    if grade in supplies:
        for item in supplies[grade]:
            st.subheader(item['item'])
            st.write(f"**Quantity:** {item['quantity']}")
            st.write(f"**Description:** {item['description']}")
            st.write("---")
    else:
        st.write("No supplies information available for this grade level.")

def main():
    st.title('School Supplies Recommendations')

    supplies = load_lottiefile("pages/assets/supplies.json")
    st_lottie(supplies, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    # Load the supplies data
    if os.path.exists(SUPPLIES_PATH):
        supplies = load_supplies(SUPPLIES_PATH)
        
        # Select grade level
        grade = st.selectbox("Select Your Grade Level", options=["K-2", "3-5", "6-8", "9-12"])
        
        # Display the supplies for the selected grade
        display_supplies(supplies, grade)
    else:
        st.error(f"Supplies file not found at {SUPPLIES_PATH}")

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the supplies list.")
else:
    main()