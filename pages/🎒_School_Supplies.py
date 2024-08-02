import streamlit as st
import yaml
import os
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="School Supplies by Scholarly", layout="centered", page_icon="🎒")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

SUPPLIES_PATH = 'pages/data/schoolsupplies.yaml'

@st.dialog("🎒 School Supplies by Scholarly")
def instructions():
    st.markdown("""    
    ### How to Use the App:
    1. **Select Grade Level**: Choose your grade level from the dropdown menu.
    2. **View Supplies**: See the recommended school supplies for the selected grade level.
    3. **Details**: Each item includes a quantity and description for better understanding.
    
    Prepare for school with the right supplies!
    """)

def load_supplies(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

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
    st.title('🎒 School Supplies by Scholarly')

    supplies = load_lottiefile("pages/assets/supplies.json")
    st_lottie(supplies, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    if os.path.exists(SUPPLIES_PATH):
        supplies = load_supplies(SUPPLIES_PATH)
        
        grade = st.selectbox("Select Your Grade Level", options=["K-2", "3-5", "6-8", "9-12"])
        
        display_supplies(supplies, grade)
    else:
        st.error(f"Supplies file not found at {SUPPLIES_PATH}")

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the supplies list.")
else:
    if 'school_supplies_instructions_shown' not in st.session_state:
        st.session_state['school_supplies_instructions_shown'] = False

    if not st.session_state['school_supplies_instructions_shown']:
        instructions()
        st.session_state['school_supplies_instructions_shown'] = True
    main()