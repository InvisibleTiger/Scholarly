import streamlit as st

# Initialize session state for class count
if 'class_count' not in st.session_state:
    st.session_state.class_count = 1

def add_class():
    st.session_state.class_count += 1

def remove_class():
    if st.session_state.class_count > 1:
        st.session_state.class_count -= 1

st.title("GPA Calculator")

# Radio selector for GPA type
gpa_type = st.radio("Select GPA Type", ["Unweighted GPA", "Weighted GPA"])

# Collect class information
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

# Buttons to add or remove classes
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Add Class"):
        add_class()
with col2:
    if st.button("Remove Class"):
        remove_class()

# GPA calculation logic
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
            # Calculate GPA, no need to cap here, just make sure no negative values
            gpa_points.append(max(base_gpa, 0))
        
        # Average GPA for all classes
        average_gpa = sum(gpa_points) / len(gpa_points)
        st.write(f"Weighted GPA: {average_gpa:.2f}")
    else:
        st.error("Please ensure that all classes have a level selected.")
