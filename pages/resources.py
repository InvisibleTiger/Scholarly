import streamlit as st
import yaml
import os

# Path to the YAML file
RESOURCES_PATH = 'pages/data/resources.yaml'

# Load resources from the YAML file
def load_resources(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

# Function to display the resources
def display_resources(resources):
    for topic, items in resources.items():
        st.header(topic)
        for item in items:
            st.subheader(item['title'])
            st.write(f"[{item['link']}]({item['link']})")
            st.write(item['description'])
            st.write("---")

def main():
    st.title('Comprehensive Resource Library')

    if os.path.exists(RESOURCES_PATH):
        resources = load_resources(RESOURCES_PATH)
        display_resources(resources)
    else:
        st.error(f"Resources file not found at {RESOURCES_PATH}")

if __name__ == "__main__":
    main()