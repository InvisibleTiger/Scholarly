import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottie_animation(file_path):
    with open(file_path, "r") as file:
        animation_data = json.load(file)
    st_lottie(animation_data, speed=1, width=400, height=400, key="animation")

animation_file_path = "assets/gpacalculator.json"
load_lottie_animation(animation_file_path)

if 'first_time_running' not in st.session_state:
    st.session_state.first_time_running = True

if st.session_state.first_time_running:
    @st.dialog("Instructions")
    def instructions():
        st.markdown("""
            **Welcome to the GPA Calculator!**  
            Here are some instructions to help you get started:

            - **Add Class**: Click the "Add Class" button to add a new class entry.
            - **Remove Class**: Click the "Remove Class" button to remove the last class entry.
            - **Class Name**: Enter the name of the class.
            - **Class Grade**: Enter the grade for the class (0-100). The GPA will be calculated based on this grade.
            - **Calculate GPA**: Click the "Calculate GPA" button to compute and display your GPA.
        """)

    instructions()
    st.session_state.first_time_running = False

st.title("GPA Calculator")

if 'class_info' not in st.session_state:
    st.session_state.class_info = [{"class_name": "", "class_grade": 70}]

def add_class():
    st.session_state.class_info.append({"class_name": "", "class_grade": 70})

def remove_class():
    if st.session_state.class_info:
        st.session_state.class_info.pop()

for i, class_data in enumerate(st.session_state.class_info):
    with st.expander(f"Class {i+1}"):
        class_data["class_name"] = st.text_input(f"Class Name {i+1}", key=f"class_name_{i}")
        class_data["class_grade"] = st.number_input(f"Class Grade {i+1}", min_value=0, max_value=100, value=70, step=1, key=f"class_grade_{i}")

def calculate_gpa():
    total_gpa = 0
    num_classes = len(st.session_state.class_info)
    
    for class_data in st.session_state.class_info:
        grade = class_data["class_grade"]
        gpa = 4.0 - (100 - grade) * 0.05
        
        total_gpa += gpa
    
    avg_gpa = total_gpa / num_classes if num_classes > 0 else 0
    st.session_state.calculated_gpa = avg_gpa

col1, col2 = st.columns([1, 1])
with col1:
    st.button("Add Class", on_click=add_class)
with col2:
    st.button("Remove Class", on_click=remove_class)

st.button("Calculate GPA", on_click=calculate_gpa)

if 'calculated_gpa' in st.session_state:
    st.success(f"Your calculated GPA is: {st.session_state.calculated_gpa:.2f}")
    st.balloons()