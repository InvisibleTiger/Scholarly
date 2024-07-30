import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottie_animation(file_path):
    with open(file_path, "r") as file:
        animation_data = json.load(file)
    st_lottie(animation_data, speed=1, width=400, height=400, key="animation")

animation_file_path = "assets/gpacalculator.json"
load_lottie_animation(animation_file_path)

@st.dialog("Instructions")
def instructions():    
    st.markdown("""
        **Welcome to the Career Quiz!**  
        Here are some instructions to help you get started:

        - **Answer Questions**: Choose the options that best reflect your interests, skills, and preferences.
        - **Submit Answers**: Click the "Submit" button to get your recommended career based on your responses.
    """)

instructions()
st.title("Career Quiz")

questions = {
    "What are your favorite activities?": [
        "Reading", "Coding", "Designing", "Helping Others", "Building Things", "Analyzing Data", "Traveling", "Writing", "Researching", "Public Speaking"
    ],
    "What skills do you enjoy using?": [
        "Problem Solving", "Creativity", "Leadership", "Technical Skills", "Communication", "Organizational Skills", "Critical Thinking", "Negotiation", "Strategic Planning", "Data Analysis"
    ],
    "What type of work environment do you prefer?": [
        "Office", "Remote", "Outdoor", "Laboratory", "Creative Studio", "Fieldwork", "Corporate", "Startup", "Non-Profit", "Educational"
    ],
    "What kind of tasks do you prefer?": [
        "Analytical Tasks", "Creative Tasks", "Management Tasks", "Technical Tasks", "Helping Others", "Independent Projects", "Team Projects", "Strategic Tasks", "Administrative Tasks", "Client Interaction"
    ],
    "How do you handle stress?": [
        "Calmly", "By Organizing", "By Seeking Help", "Through Exercise", "By Taking Breaks", "By Avoiding the Problem", "Through Meditation", "By Working Longer Hours", "By Talking to Friends", "Through Hobbies"
    ],
    "How do you prefer to learn new things?": [
        "Online Courses", "Hands-On Experience", "Reading Books", "Workshops", "Mentorship", "Formal Education", "Peer Learning", "Webinars", "Self-Study", "Practice and Feedback"
    ],
    "What type of leadership style resonates with you?": [
        "Democratic", "Autocratic", "Transformational", "Transactional", "Servant", "Charismatic", "Laissez-Faire", "Participative", "Coaching", "Visionary"
    ],
    "What motivates you at work?": [
        "Recognition", "Financial Rewards", "Career Growth", "Job Satisfaction", "Helping Others", "Challenging Work", "Work-Life Balance", "Autonomy", "Team Success", "Professional Development"
    ],
    "What are your long-term career goals?": [
        "Become an Expert", "Start My Own Business", "Achieve a Managerial Role", "Work in a Creative Field", "Contribute to Society", "Gain Financial Independence", "Work in a Technology-Driven Role", "Advance to Executive Position", "Make a Significant Impact", "Develop New Products"
    ],
    "How do you prefer to work on projects?": [
        "Individually", "In a Team", "With a Mentor", "Under Tight Deadlines", "In a Structured Environment", "With Flexibility", "On Multiple Projects Simultaneously", "With Clear Guidelines", "With Frequent Check-ins", "In an Agile Environment"
    ],
    "What types of tasks do you excel at?": [
        "Strategic Planning", "Technical Problem Solving", "Creative Design", "Team Collaboration", "Customer Service", "Data Analysis", "Project Management", "Administrative Tasks", "Negotiation", "Client Relations"
    ],
    "What type of impact do you want to make?": [
        "Innovative Solutions", "Social Change", "Financial Success", "Creative Expressions", "Technical Advances", "Educational Contributions", "Environmental Protection", "Cultural Impact", "Economic Development", "Health Improvements"
    ],
    "What work schedule do you prefer?": [
        "9 to 5", "Flexible Hours", "Night Shifts", "Weekend Work", "Part-Time", "Full-Time", "Project-Based", "Shift Work", "Seasonal Work", "On-Demand"
    ],
    "How do you prefer to interact with colleagues?": [
        "Face-to-Face", "Virtual Meetings", "Email", "Chat", "Collaborative Platforms", "In-Person Networking", "Formal Communication", "Social Media", "Informal Catch-Ups", "Project Management Tools"
    ],
    "What kind of projects do you enjoy?": [
        "Long-Term Projects", "Short-Term Tasks", "High-Risk Projects", "Collaborative Projects", "Solo Projects", "Innovation-Focused Projects", "Research-Driven Projects", "Community-Based Projects", "Client-Focused Projects", "Development Projects"
    ],
    "What kind of recognition do you value?": [
        "Awards", "Public Acknowledgment", "Promotions", "Bonuses", "Certificates", "Team Celebrations", "Client Testimonials", "Media Coverage", "Peer Appreciation", "Personal Growth"
    ],
    "What type of work-life balance are you looking for?": [
        "Strict Separation", "Flexible Hours", "Remote Work", "Extended Vacation", "Part-Time Work", "Job Sharing", "Compressed Workweek", "Unlimited PTO", "On-Demand Work", "Flexible Location"
    ]
}

responses = {question: st.multiselect(question, options) for question, options in questions.items()}

if st.button("Submit"):
    career_recommendations = {
        "Technology": {
            "interests": ["Coding", "Analyzing Data", "Technical Skills"],
            "skills": ["Technical Skills", "Problem Solving"],
            "work_environment": ["Office", "Remote", "Laboratory", "Startup"],
            "tasks": ["Technical Tasks", "Analytical Tasks"],
            "impact": ["Innovative Solutions", "Technical Advances"]
        },
        "Design": {
            "interests": ["Designing", "Creative Tasks"],
            "skills": ["Creativity", "Creative Design"],
            "work_environment": ["Creative Studio", "Remote"],
            "tasks": ["Creative Tasks", "Collaborative Projects"],
            "impact": ["Creative Expressions"]
        },
        "Management": {
            "interests": ["Helping Others", "Building Things"],
            "skills": ["Leadership", "Organizational Skills"],
            "work_environment": ["Office", "Corporate", "Non-Profit"],
            "tasks": ["Management Tasks", "Team Projects"],
            "impact": ["Career Growth", "Financial Success"]
        },
        "Social Work": {
            "interests": ["Helping Others"],
            "skills": ["Communication", "Customer Service"],
            "work_environment": ["Fieldwork", "Office"],
            "tasks": ["Helping Others", "Team Projects"],
            "impact": ["Social Change", "Contribute to Society"]
        },
        "Research": {
            "interests": ["Analyzing Data", "Research-Driven Projects"],
            "skills": ["Critical Thinking", "Data Analysis"],
            "work_environment": ["Laboratory", "Office"],
            "tasks": ["Research-Driven Projects", "Analytical Tasks"],
            "impact": ["Innovative Solutions", "Technical Advances"]
        },
        "Entrepreneurship": {
            "interests": ["Building Things", "Starting My Own Business"],
            "skills": ["Leadership", "Organizational Skills"],
            "work_environment": ["Office", "Remote"],
            "tasks": ["Independent Projects", "Innovation-Focused Projects"],
            "impact": ["Financial Success", "Innovative Solutions"]
        },
        "Education": {
            "interests": ["Teaching", "Mentorship"],
            "skills": ["Communication", "Organizational Skills"],
            "work_environment": ["Office", "Remote"],
            "tasks": ["Educational Contributions", "Collaborative Projects"],
            "impact": ["Educational Contributions", "Social Change"]
        },
        "Environmental Science": {
            "interests": ["Environmental Protection", "Fieldwork"],
            "skills": ["Analytical Skills", "Problem Solving"],
            "work_environment": ["Outdoor", "Fieldwork"],
            "tasks": ["Research-Driven Projects", "Analytical Tasks"],
            "impact": ["Environmental Protection", "Innovative Solutions"]
        },
        "Finance": {
            "interests": ["Analyzing Data", "Problem Solving"],
            "skills": ["Critical Thinking", "Financial Analysis"],
            "work_environment": ["Office", "Corporate"],
            "tasks": ["Analytical Tasks", "Data Analysis"],
            "impact": ["Financial Success", "Economic Development"]
        },
        "Healthcare": {
            "interests": ["Helping Others", "Research"],
            "skills": ["Communication", "Critical Thinking"],
            "work_environment": ["Fieldwork", "Office", "Laboratory"],
            "tasks": ["Helping Others", "Research-Driven Projects"],
            "impact": ["Health Improvements", "Social Change"]
        },
        "Marketing": {
            "interests": ["Creative Tasks", "Public Speaking"],
            "skills": ["Creativity", "Communication"],
            "work_environment": ["Office", "Remote"],
            "tasks": ["Creative Tasks", "Client Interaction"],
            "impact": ["Creative Expressions", "Financial Success"]
        },
        "Engineering": {
            "interests": ["Building Things", "Technical Skills"],
            "skills": ["Problem Solving", "Technical Skills"],
            "work_environment": ["Office", "Laboratory", "Fieldwork"],
            "tasks": ["Technical Tasks", "Analytical Tasks"],
            "impact": ["Technical Advances", "Innovative Solutions"]
        }
    }

    def match_career():
        matched_careers = []
        for career, criteria in career_recommendations.items():
            match_score = 0
            total_criteria = len(criteria)
            
            for category, values in criteria.items():
                if category == "interests":
                    if any(item in responses["What are your favorite activities?"] for item in values):
                        match_score += 1
                elif category == "skills":
                    if any(item in responses["What skills do you enjoy using?"] for item in values):
                        match_score += 1
                elif category == "work_environment":
                    if any(item in responses["What type of work environment do you prefer?"] for item in values):
                        match_score += 1
                elif category == "tasks":
                    if any(item in responses["What kind of tasks do you prefer?"] for item in values):
                        match_score += 1
                elif category == "impact":
                    if any(item in responses["What type of impact do you want to make?"] for item in values):
                        match_score += 1
            
            if match_score >= (total_criteria / 2):
                matched_careers.append(career)
        
        return matched_careers

    recommended_careers = match_career()

    st.write("Based on your responses, the following career paths might suit you:")
    st.write(", ".join(recommended_careers) if recommended_careers else "No specific career recommendations available.")
    st.balloons()
