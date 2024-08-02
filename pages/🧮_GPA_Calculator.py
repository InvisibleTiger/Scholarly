import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="GPA Calculator by Scholarly", layout="centered", page_icon="🧮")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
@st.dialog("🧮 GPA Calculator by Scholarly")
def instructions():
    st.markdown("""    
    ### How to Use the App:
    1. **Select GPA Type**: Weighted awards for taking a higher level while unweighted considers it equal.
    2. **Add/Remove Classes As Required**: Click on the buttons to add/remove classes as per required as your schedule.
    3. **Fill In Information**: Fill in information and recieve your GPA.

    Stay informed about your academics!
    """)

if 'class_count' not in st.session_state:
    st.session_state.class_count = 1

def add_class():
    st.session_state.class_count += 1

def remove_class():
    if st.session_state.class_count > 1:
        st.session_state.class_count -= 1

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the GPA calculator.")
else:
    if 'gpa_instructions_shown' not in st.session_state:
        st.session_state['gpa_instructions_shown'] = False

    if not st.session_state['gpa_instructions_shown']:
        instructions()
        st.session_state['gpa_instructions_shown'] = True

    st.title("🧮 GPA Calculator by Scholarly")

    calculator = load_lottiefile("pages/assets/gpacalculator.json")
    st_lottie(calculator, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    gpa_type = st.radio("Select GPA Type", ["Unweighted GPA", "Weighted GPA"])

    class_grades = []
    class_levels = []

    for i in range(1, st.session_state.class_count + 1):
        with st.expander(f"Class {i}"):
            class_name = st.text_input(f"Class Name {i} (Optional)", key=f"class_name_{i}")
            if gpa_type == "Weighted GPA":
                class_level = st.selectbox(f"Class Level {i}", ["Standard", "Honors", "AP/IB"], key=f"class_level_{i}")
                class_levels.append(class_level)
            class_grade = st.number_input(f"Class Grade {i}", min_value=0, max_value=100, value=100, key=f"class_grade_{i}")
            class_grades.append(class_grade)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Add Class"):
            add_class()
    with col2:
        if st.button("Remove Class"):
            remove_class()

    if gpa_type == "Unweighted GPA":
        if class_grades:
            gpa_points = [(4.0 - (100 - grade) * 0.05) for grade in class_grades]
            average_gpa = sum(gpa_points) / len(gpa_points)
            st.write(f"Unweighted GPA: {average_gpa:.2f}")

    elif gpa_type == "Weighted GPA":
        if class_grades and len(class_grades) == len(class_levels):
            gpa_points = []
            for grade, level in zip(class_grades, class_levels):
                base_gpa = 4.0 - (100 - grade) * 0.05
                if level == "Honors":
                    base_gpa += 0.5
                elif level == "AP/IB":
                    base_gpa += 1.0
                gpa_points.append(max(base_gpa, 0))
            
            average_gpa = sum(gpa_points) / len(gpa_points)
            st.write(f"Weighted GPA: {average_gpa:.2f}")
        else:
            st.error("Please ensure that all classes have a level selected.")