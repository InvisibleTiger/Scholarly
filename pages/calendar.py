import streamlit as st
import yaml
import os
from datetime import datetime

# Function to load activities from YAML file
def load_activities():
    with open("pages/data/calendar.yaml", "r") as file:
        return yaml.safe_load(file)

# Function to save activities to YAML file
def save_activities(data):
    with open("pages/data/calendar.yaml", "w") as file:
        yaml.dump(data, file)

# Ensure the user is signed in
if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the calendar.")
else:
    st.title("Student Activity Calendar")

    # Load existing activities
    activities = load_activities().get(st.session_state.current_user, [])

    # Display the current activities
    st.subheader("Current Activities")
    for i, activity in enumerate(activities):
        title = activity['activity']
        expander = st.expander(f"{title} at {activity['time']}")
        with expander:
            if "✅" not in title:
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button(f"Remove {title}", key=f"remove_{i}"):
                        activities.pop(i)
                        save_activities({st.session_state.current_user: activities})
                        st.rerun()
                with col2:
                    if st.button(f"Mark {title} as Completed", key=f"complete_{i}"):
                        activities[i]['activity'] += " ✅"
                        save_activities({st.session_state.current_user: activities})
                        st.balloons()
                        st.rerun()
            else:
                st.write(f"{title}")

    # Form to add a new activity
    st.subheader("Add New Activity")
    with st.form(key='add_activity_form'):
        new_activity = st.text_input("Activity")
        new_time = st.time_input("Time")
        submit_button = st.form_submit_button(label='Add Activity')

        if submit_button:
            activities.append({"activity": new_activity, "time": new_time.strftime('%H:%M')})
            save_activities({st.session_state.current_user: activities})
            st.success("Activity added successfully!")
            st.rerun()

    # Check if the current time matches any activity time
    current_time = datetime.now().strftime('%H:%M')
    for activity in activities:
        if activity['time'] == current_time:
            st.balloons()
            st.warning(f"It's time for: {activity['activity']}!")