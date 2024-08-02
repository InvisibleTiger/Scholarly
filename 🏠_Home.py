import streamlit as st
import yaml
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Home by Scholarly", layout="centered", page_icon="🏠")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def loadData():
    try:
        with open("pages/data/userandpassword.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def saveData(user_data):
    with open("pages/data/userandpassword.yaml", "w") as file:
        yaml.safe_dump(user_data, file)

def loadIncomeExpenseData():
    try:
        with open("pages/data/incomeandexpense.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def saveIncomeExpenseData(data):
    with open("pages/data/incomeandexpense.yaml", "w") as file:
        yaml.safe_dump(data, file)

def loadFlashcardsData():
    try:
        with open("pages/data/flashcards.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def saveFlashcardsData(data):
    with open("pages/data/flashcards.yaml", "w") as file:
        yaml.safe_dump(data, file)

def loadCalendarData():
    try:
        with open("pages/data/calendar.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {}

def saveCalendarData(data):
    with open("pages/data/calendar.yaml", "w") as file:
        yaml.safe_dump(data, file)

def signUp(username, password):
    if username in users:
        return "Username already exists. Please choose a different username."
    else:
        users[username] = password
        saveData(users)
        
        income_expense_data = loadIncomeExpenseData()
        income_expense_data[username] = []
        saveIncomeExpenseData(income_expense_data)

        flashcards_data = loadFlashcardsData()
        flashcards_data[username] = []
        saveFlashcardsData(flashcards_data)

        calendar_data = loadCalendarData()
        calendar_data[username] = []
        saveCalendarData(calendar_data)

        st.balloons()
        return "Sign Up successful! You can now Sign In."

def signIn(username, password):
    if username in users and users[username] == password:
        st.balloons()
        return True
    else:
        return False

def sign_up_page():
    st.header("Sign Up")
    
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        result = signUp(new_username, new_password)
        st.info(result)

def sign_in_page():
    st.header("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if signIn(username, password):
            st.session_state.current_user = username
            st.success(f"Welcome, {username}!")
            st.info("To signout, just refresh the app.")
        else:
            st.error("Invalid username or password.")

def check_things_out():
    st.subheader("Rethinking Student Productivity.")

    graphic9, text9 = st.columns([1, 2])
    with graphic9:
        st_lottie(timer, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text9:
        st.subheader("Timer")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic3, text3 = st.columns([1, 2])
    with graphic3:
        st_lottie(cooking, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text3:
        st.subheader("Cooking Recipies")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic8, text8 = st.columns([1, 2])
    with graphic8:
        st_lottie(supplies, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text8:
        st.subheader("School Supplies")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic5, text5 = st.columns([1, 2])
    with graphic5:
        st_lottie(money, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text5:
        st.subheader("Income and Expense Tracker")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic2, text2 = st.columns([1, 2])
    with graphic2:
        st_lottie(calendar, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text2:
        st.subheader("Calendar")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic4, text4 = st.columns([1, 2])
    with graphic4:
        st_lottie(flashcards, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text4:
        st.subheader("Flashcards")
        st.write("A database that recommends books to read based on genre and lexile level.")

    
    graphic7, text7 = st.columns([1, 2])
    with graphic7:
        st_lottie(resources, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text7:
        st.subheader("Resources")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic6, text6 = st.columns([1, 2])
    with graphic6:
        st_lottie(news, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text6:
        st.subheader("News")
        st.write("A database that recommends books to read based on genre and lexile level.")

    graphic1, text1 = st.columns([1, 2])
    with graphic1:
        st_lottie(gpacalculator, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)
    with text1:
        st.subheader("GPA Calculator")
        st.write("A database that recommends books to read based on genre and lexile level.")

    


if 'current_user' not in st.session_state:
    st.session_state.current_user = None

global users
users = loadData()

gpacalculator = load_lottiefile("pages/assets/gpacalculator.json")
calendar = load_lottiefile("pages/assets/calendar.json")
cooking = load_lottiefile("pages/assets/cooking.json")
flashcards = load_lottiefile("pages/assets/flashcards.json")
money = load_lottiefile("pages/assets/money.json")
news = load_lottiefile("pages/assets/news.json")
resources = load_lottiefile("pages/assets/resources.json")
supplies = load_lottiefile("pages/assets/supplies.json")
timer = load_lottiefile("pages/assets/timer.json")

st.image("pages/assets/scholarly-logo.png")

option = st.selectbox("Select What You Would Like to do.", ["Check Things Out", "Sign In", "Sign Up"], index=0)

if option == "Check Things Out":
    check_things_out()
elif option == "Sign In":
    sign_in_page()
elif option == "Sign Up":
    sign_up_page()