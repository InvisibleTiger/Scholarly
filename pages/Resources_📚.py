import streamlit as st
import yaml
import os
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Resources", layout="centered", page_icon="📚")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Path to the YAML file
RESOURCES_PATH = 'pages/data/resources.yaml'

# Load resources from the YAML file
def load_resources(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

# Function to display the resources
def display_resources(resources):
    for topic, items in resources.items():
        st.title(topic)
        for item in items:
            st.subheader(item['title'])
            st.write(f"[{item['link']}]({item['link']})")
            st.write(item['description'])
            st.write("---")

def main():
    st.title('Comprehensive Resource Library')

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
    main()