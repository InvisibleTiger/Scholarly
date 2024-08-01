import streamlit as st
import yaml
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Income And Expense Tracker by Scholarly", layout="centered", page_icon="💵")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.dialog("💵 Income And Expense Tracker by Scholarly")
def instructions():
    st.markdown("""    
    ### How to Use the App:
    1. **Add Income or Expense**: Choose 'Add Income or Expense' from the dropdown. Select the month and year, then input the details of your income or expense.
    2. **Visualize Data**: Select 'Visualize Data' to see a summary of your financial transactions for a selected month. You can view the details and visualize the data using bar charts.
    3. **Manage Data**: You can append new entries to existing data for the selected month.
    
    Start tracking your finances efficiently!
    """)

def load_or_create_yaml(filename, default_data):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = yaml.safe_load(file)
        return data
    else:
        with open(filename, "w") as file:
            yaml.dump(default_data, file)
        return default_data

def save_to_yaml(filename, data):
    with open(filename, "w") as file:
        yaml.dump(data, file)

def get_current_month_year_tag():
    now = datetime.now()
    return now.strftime("%B %Y")

if 'income_expense_instructions_shown' not in st.session_state:
    st.session_state['income_expense_instructions_shown'] = False

if not st.session_state['income_expense_instructions_shown']:
    instructions()
    st.session_state['income_expense_instructions_shown'] = True

if 'current_user' not in st.session_state or st.session_state.current_user is None:
    st.warning("Please sign in to access the tracker.")
else:
    st.title("💵 Income And Expense Tracker by Scholarly")

    money = load_lottiefile("pages/assets/money.json")
    st_lottie(money, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    filename = "pages/data/incomeandexpense.yaml"

    option = st.selectbox("Select what you would like to do", ["Add Income or Expense", "Visualize Data"])

    data = load_or_create_yaml(filename, {st.session_state.current_user: []})

    available_months = [entry["month"] for entry in data.get(st.session_state.current_user, [])]

    months_and_years = [get_current_month_year_tag()]
    for i in range(1, 12):
        date = datetime.now() - pd.DateOffset(months=i)
        tag = date.strftime("%B %Y")
        if tag not in available_months:
            months_and_years.append(tag)

    if option == "Add Income or Expense":
        selected_month_year_tag = st.selectbox("Select Month and Year", months_and_years)
        month_data = next((entry for entry in data[st.session_state.current_user] if entry["month"] == selected_month_year_tag), None)

        if month_data is None:
            month_data = {"month": selected_month_year_tag, "incomes": [], "expenses": []}
            data[st.session_state.current_user].append(month_data)

        st.header("Add Income or Expense")

        if month_data and month_data.get("incomes") and month_data.get("expenses"):
            st.info("Data already exists for this month. You can append to it.")

        option = st.selectbox("Select Category", ["Income", "Expense"])
        amount = st.number_input("Amount")
        description = st.text_input("Description")
        if st.button("Add"):
            if month_data:
                if option == "Income":
                    month_data["incomes"].append({"amount": amount, "description": description})
                else:
                    month_data["expenses"].append({"amount": amount, "description": description})
                save_to_yaml(filename, data)
                st.success("Data saved successfully!")

    elif option == "Visualize Data":
        st.header("Visualize Data")
        selected_month_for_visualization = st.selectbox("Select Month to Visualize", available_months)

        selected_month_data = next((entry for entry in data[st.session_state.current_user] if entry["month"] == selected_month_for_visualization), None)

        if selected_month_data:
            st.header(f"Income and Expense Data for {selected_month_for_visualization}")
            incomes = selected_month_data["incomes"]
            expenses = selected_month_data["expenses"]

            st.subheader("Income")
            df_incomes = pd.DataFrame(incomes)
            st.write(df_incomes)

            st.subheader("Expense")
            df_expenses = pd.DataFrame(expenses)
            st.write(df_expenses)

            income_amount = sum(item["amount"] for item in incomes)
            expense_amount = sum(item["amount"] for item in expenses)
            net_amount = income_amount - expense_amount

            categories = ['Income', 'Expense', 'Net']
            amounts = [income_amount, expense_amount, net_amount]
            colors = ['green', 'red', 'blue']

            fig, ax = plt.subplots()
            ax.bar(categories, amounts, color=colors)
            ax.set_xlabel('Category')
            ax.set_ylabel('Amount')
            ax.set_title(f'Income, Expense, and Net for {selected_month_for_visualization}')
            st.pyplot(fig)