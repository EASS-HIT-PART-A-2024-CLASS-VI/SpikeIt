import streamlit as st
import requests

BACKEND_URL = "http://backend_microservice:8000"

st.title("SpikeIt! - Volleyball Workout App")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar with clickable navigation links
with st.sidebar:
    st.title("Navigation")
    
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    
    if st.button("➕ Add Workout"):
        st.session_state.page = "Add Workout"

    if st.button("🔍 Search Drills"):
        st.session_state.page = "Search Drills"
    
    if st.button("📋 View Workouts"):
        st.session_state.page = "View Workouts"

# Page logic based on session state
if st.session_state.page == "Home":
    st.subheader("Welcome to SpikeIt!")

elif st.session_state.page == "Add Workout":
    st.subheader("Add a New Workout")
    workout_id = 0
    num_drills = st.number_input("Number of Drills", min_value=1, step=1)
    
    drills = []
    for i in range(int(num_drills)):
        st.write(f"Drill {i + 1}")
        drill_name = st.text_input(f"Name {i + 1}", key=f"name_{i}")
        drill_duration = st.number_input(f"Duration (min) {i + 1}", key=f"duration_{i}")
        drill_equipment = st.text_input(f"Equipment {i + 1}", key=f"equipment_{i}")
        drill_type = st.selectbox(f"Type {i + 1}", ["Attack", "Defence", "Recive", "Setting", "Strength"], key=f"type_{i}")
        drill_explanation = st.text_area(f"Explanation {i + 1}", key=f"explanation_{i}")
        drills.append({
            "name": drill_name,
            "duration": drill_duration,
            "equipment": drill_equipment,
            "type": drill_type,
            "explanation": drill_explanation
        })
    
    if st.button("Submit Workout"):
        response = requests.post(
            f"{BACKEND_URL}/new_workout/",
            json={"workout_id": workout_id, "drills": drills}
        )
        if response.status_code == 200:
            st.success("Workout created successfully!")
        else:
            st.error("Failed to create workout.")

elif st.session_state.page == "Search Drills":
    st.subheader("Search Drills by Type")
    drill_type = st.selectbox("Select Drill Type", ["Attack", "Defence", "Recive", "Setting", "Strength"])
    
    if st.button("Search"):
        response = requests.get(f"{BACKEND_URL}/search_drills/{drill_type}")
        if response.status_code == 200:
            drills = response.json()
            for drill in drills:
                st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 10px; margin: 10px 0; border-radius: 5px; background-color: #f9f9f9;">
                    <strong>Drill Name:</strong> {drill['name']}<br>
                    <strong>Duration:</strong> {drill['duration']} minutes<br>
                    <strong>Equipment:</strong> {drill['equipment']}<br>
                    <strong>Type:</strong> {drill['type']}<br>
                    <strong>Explanation:</strong> {drill['explanation']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No drills found for this type.")


elif st.session_state.page == "View Workouts":
    st.subheader("View Workouts")
    response = requests.get(f"{BACKEND_URL}/show_all_workouts/")
    if response.status_code == 200:
        workouts = response.json()
        for workout in workouts:
            st.markdown(f"### Workout ID: {workout['workout_id']}")
            details_response = requests.get(f"{BACKEND_URL}/show_workout/{workout['workout_id']}")
            if details_response.status_code == 200:
                drills = details_response.json()
                for drill in drills:
                    st.markdown(f"""
                    <div style="border: 1px solid #ddd; padding: 10px; margin: 10px 0; border-radius: 5px; background-color: #f9f9f9;">
                        <strong>Drill Name:</strong> {drill['name']}<br>
                        <strong>Duration:</strong> {drill['duration']} minutes<br>
                        <strong>Equipment:</strong> {drill['equipment']}<br>
                        <strong>Type:</strong> {drill['type']}<br>
                        <strong>Explanation:</strong> {drill['explanation']}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No drills found.")
    else:
        st.error("Failed to fetch workouts.")
