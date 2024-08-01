import streamlit as st
import yaml
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Income And Expense Tracker", layout="centered", page_icon="💵")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

if 'current_user' not in st.session_state or st.session_state.current_user is None:
    st.warning("Please sign in to access the tracker.")
else:
    st.title("Income And Expense Tracker 💵")

    money = load_lottiefile("pages/assets/money.json")
    st_lottie(money, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    # File path for YAML data
    filename = "pages/data/incomeandexpense.yaml"

    # Function to load or create a YAML file
    def load_or_create_yaml(filename, default_data):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = yaml.safe_load(file)
            return data
        else:
            with open(filename, "w") as file:
                yaml.dump(default_data, file)
            return default_data

    # Function to save data to the YAML file
    def save_to_yaml(filename, data):
        with open(filename, "w") as file:
            yaml.dump(data, file)

    # Function to get the current month and year as a tag
    def get_current_month_year_tag():
        now = datetime.now()
        return now.strftime("%B %Y")

    option = st.selectbox("Select what you would like to do", ["Add Income or Expense", "Visualize Data"])

    # Load or create the YAML file
    data = load_or_create_yaml(filename, {st.session_state.current_user: []})

    # Extract available months from the YAML data
    available_months = [entry["month"] for entry in data.get(st.session_state.current_user, [])]

    # Create a dropdown at the top to select a month and year
    months_and_years = [get_current_month_year_tag()]
    for i in range(1, 12):
        date = datetime.now() - pd.DateOffset(months=i)
        tag = date.strftime("%B %Y")
        if tag not in available_months:
            months_and_years.append(tag)

    if option == "Add Income or Expense":
        selected_month_year_tag = st.selectbox("Select Month and Year", months_and_years)

        # Get or initialize the data for the selected month and year
        month_data = next((entry for entry in data[st.session_state.current_user] if entry["month"] == selected_month_year_tag), None)

        if month_data is None:
            # Initialize data for the selected month if it doesn't exist
            month_data = {"month": selected_month_year_tag, "incomes": [], "expenses": []}
            data[st.session_state.current_user].append(month_data)

        # Input fields in the "Add Data" section
        st.header("Add Income or Expense")

        # Display info message if data already exists for the selected month
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
        # "Visualize Data" section
        st.header("Visualize Data")

        # Create a dropdown to select a month from the available data
        selected_month_for_visualization = st.selectbox("Select Month to Visualize", available_months)

        # Find the data for the selected month
        selected_month_data = next((entry for entry in data[st.session_state.current_user] if entry["month"] == selected_month_for_visualization), None)

        # Display data for the selected month if available
        if selected_month_data:
            # Display Income and Expense data
            st.header(f"Income and Expense Data for {selected_month_for_visualization}")
            incomes = selected_month_data["incomes"]
            expenses = selected_month_data["expenses"]

            st.subheader("Income")
            df_incomes = pd.DataFrame(incomes)
            st.write(df_incomes)

            st.subheader("Expense")
            df_expenses = pd.DataFrame(expenses)
            st.write(df_expenses)

            # Bar graph for the selected month
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