import streamlit as st
import yaml

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
        
        # Initialize income and expense data for new user
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
        else:
            st.error("Invalid username or password.")

    if st.session_state.current_user:
        if st.sidebar.button("Sign Out"):
            st.session_state.current_user = None

if 'current_user' not in st.session_state:
    st.session_state.current_user = None

global users
users = loadData()

option = st.selectbox("Select What You Would Like to do.", ["Sign In", "Sign Up"], index=0)

if option == "Sign In":
    sign_in_page()
elif option == "Sign Up":
    sign_up_page()