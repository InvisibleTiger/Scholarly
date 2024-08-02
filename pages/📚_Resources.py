import streamlit as st
import yaml
import os
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Resources by Scholarly", layout="centered", page_icon="📚")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.dialog("📚 Resources by Scholarly")
def instructions():
    st.markdown("""    
    ### How to Use the App:
    1. **View Resources**: Browse through the various topics and their associated resources.
    2. **Access Links**: Click on the links provided to access external resources.
    3. **Descriptions**: Read the descriptions to understand more about each resource.
    
    Make the most of these resources to enhance your learning experience!
    """)

RESOURCES_PATH = 'pages/data/resources.yaml'

def load_resources(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def display_resources(resources):
    for topic, items in resources.items():
        st.title(topic)
        for item in items:
            st.subheader(item['title'])
            st.write(f"[{item['link']}]({item['link']})")
            st.write(item['description'])
            # st.write("---")

def main():
    st.title('📚 Resources by Scholarly')

    resources = load_lottiefile("pages/assets/resources.json")
    st_lottie(resources, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    if os.path.exists(RESOURCES_PATH):
        resources = load_resources(RESOURCES_PATH)
        display_resources(resources)
    else:
        st.error(f"Resources file not found at {RESOURCES_PATH}")

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the resources.")
else:
    if 'resources_instructions_shown' not in st.session_state:
        st.session_state['resources_instructions_shown'] = False

    if not st.session_state['resources_instructions_shown']:
        instructions()
        st.session_state['resources_instructions_shown'] = True
    main()