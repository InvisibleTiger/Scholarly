import streamlit as st
import requests
import re
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Cooking Recipies", layout="centered", page_icon="🍽️")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def clean_html_tags(text):
    if text is None:
        return ""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the recipies.")
else:
    st.title('Cooking Recipes 🍽️')

    recipies = load_lottiefile("pages/assets/cooking.json")
    st_lottie(recipies, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    
    st.header('Ingredients')

    st.subheader('How to Use')
    st.write("Enter the ingredients you have in your kitchen, separated by commas in the text input. Click 'Find Recipes' to get recommendations based on the provided ingredients.")
    user_input = st.text_input('Enter Ingredients (comma-separated)')

    # Replace 'YOUR_API_KEY' with your Spoonacular API key
    API_KEY = 'e6eec33a959a4b2285baff0d0a7e99d8'

    if st.button('Find Recipes'):
        ingredients = user_input
        search_url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY}&ingredients={ingredients}'
        response = requests.get(search_url)

        if response.status_code == 200:
            data = response.json()
            for recipe in data:
                st.subheader(f"**{recipe['title']}**")
                
                if 'image' in recipe:
                    st.image(recipe['image'], use_column_width=True)
                
                recipe_id = recipe['id']
                recipe_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}'
                recipe_info = requests.get(recipe_url).json()

                used_ingredients = [ingredient['name'] for ingredient in recipe['usedIngredients']]
                missed_ingredients = [ingredient['name'] for ingredient in recipe['missedIngredients']]
                st.write(f"Used Ingredients: {', '.join(used_ingredients)}")
                st.write(f"Missed Ingredients: {', '.join(missed_ingredients)}")

                if 'instructions' in recipe_info:
                    st.write("Instructions:")
                    clean_instructions = clean_html_tags(recipe_info['instructions'])
                    st.write(clean_instructions)
                else:
                    st.warning('No instructions available.')
        else:
            st.warning(f'Error fetching recipes. Status code: {response.status_code}')