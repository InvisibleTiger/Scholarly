import streamlit as st
import requests
import re
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Cooking Recipes by Scholarly", layout="centered", page_icon="🍽️")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.dialog("🍽️ Cooking Recipes by Scholarly")
def instructions():
    st.markdown("""
    
    ### How to Use the App:
    1. **Enter Ingredients**: Input the ingredients you have in your kitchen, separated by commas.
    2. **Find Recipes**: Click 'Find Recipes' to get recipe recommendations based on the ingredients you provided.
    3. **View Recipes**: Browse through the recipes, view the ingredients used, and follow the instructions to cook your meal.
    
    Enjoy your cooking experience!
    """)

def clean_html_tags(text):
    if text is None:
        return ""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

if 'recipes_instructions_shown' not in st.session_state:
    st.session_state['recipes_instructions_shown'] = False

if not st.session_state['recipes_instructions_shown']:
    instructions()
    st.session_state['recipes_instructions_shown'] = True

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the recipes.")
else:
    st.title('🍽️ Cooking Recipes by Scholarly')

    recipes = load_lottiefile("pages/assets/cooking.json")
    st_lottie(recipes, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    
    st.header('Ingredients')

    st.subheader('How to Use')
    st.write("Enter the ingredients you have in your kitchen, separated by commas in the text input. Click 'Find Recipes' to get recommendations based on the provided ingredients.")
    user_input = st.text_input('Enter Ingredients (comma-separated)')

    API_KEY = st.secrets["Food_Key"]

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