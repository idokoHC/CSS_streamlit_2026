# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
st.image("https://studentroom.co.za/wiki/wp-content/uploads/2020/12/TUT-logo-1024x536.png")
# Title of the app
st.header("Student Profile")

# Collect basic information
name = "Engr. Hillary Chika Idoko"
level = "Doctor of Engineering" 
specialization = "Electric Machines and Drives"
department = "Electrical Engineering"
faculty = "Engineering and Built Environment" 
institution = "Tshwane University of Technology"
st.write(f"**Name:** {name}")
st.write(f"**Level of Study:** {level}")
st.write(f"**Area of specialization:** {specialization}")
st.write(f"**Department:** {department}")
st.write(f"**Faculty:** {faculty}")
st.write(f"**Institution:** {institution}")

# Add a section for research interests
st.header("Research Interest")
st.write("* Electric Machines and Drives")
st.write("* Power Electronics")
st.write("* Renewable Energy Technology")

# Add a section for computer programming skills
st.header("Computer Programming Skills")
st.write("* Python")
st.write("* Linux/Bash")
st.write("* ANSYS Maxwell")
st.write("* MATLAB/Simulink")

# Add a contact section
st.header("Contact Information")
email = "222449294@tut4life.ac.za"
st.write(f"You can reach {name} at {email}.")


















