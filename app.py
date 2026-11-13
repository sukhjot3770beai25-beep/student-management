
import streamlit as st

st.set_page_config(page_title="Student Management", page_icon="🎓")

st.title("🎓 Student Record Management System")

# Store student records
if "students" not in st.session_state:
    st.session_state.students = []

# Sidebar menu
menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# CREATE
if menu == "Add Student":
    st.header("Add New Student")

    with st.form("add_form"):
        roll = st.number_input("Roll Number", min_value=1, step=1)
        name = st.text_input("Student Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        course = st.text_input("Course")

        submit = st.form_submit_button("Add Student")

        if submit:
            if not name or not course:
                st.error("Please fill all fields")
            elif any(s["Roll"] == roll for s in st.session_state.students):
                st.error("Roll number already exists")
            else:
                st.session_state.students.append({
                    "Roll": roll,
                    "Name": name,
                    "Age": age,
                    "Course": course
                })
                st.success("Student added successfully!")

# READ
elif menu == "View Students":
    st.header("All Student Records")

    if st.session_state.students:
        st.dataframe(st.session_state.students)
    else:
        st.info("No student records found")

# UPDATE
elif menu == "Update Student":
    st.header("Update Student Details")

    if st.session_state.students:
        rolls = [s["Roll"] for s in st.session_state.students]

        selected_roll = st.selectbox("Select Roll Number", rolls)

        student = next(
            s for s in st.session_state.students
            if s["Roll"] == selected_roll
        )

        name = st.text_input("Name", value=student["Name"])
        age = st.number_input("Age", min_value=1, max_value=100,
                              value=student["Age"])
        course = st.text_input("Course", value=student["Course"])

        if st.button("Update Record"):
            student["Name"] = name
            student["Age"] = age
            student["Course"] = course

            st.success("Student updated successfully!")
    else:
        st.info("No records available to update")

# DELETE
elif menu == "Delete Student":
    st.header("Delete Student Record")

    if st.session_state.students:
        rolls = [s["Roll"] for s in st.session_state.students]

        selected_roll = st.selectbox("Select Roll Number", rolls)

        if st.button("Delete Record"):
            st.session_state.students = [
                s for s in st.session_state.students
                if s["Roll"] != selected_roll
            ]

            st.success("Student deleted successfully!")
    else:
        st.info("No records available to delete")
