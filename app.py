# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
st.image("https://studentroom.co.za/wiki/wp-content/uploads/2020/12/TUT-logo-1024x536.png")
# Title of the app
st.header("Student Profile")

# Collect basic information
name = "Engr. Dr Hillary Chika Idoko"
field = "Electrical Engineering"
institution = "University of Nigeria Nsukka"


st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")














