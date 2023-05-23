import streamlit as st
import pandas as pd
from prediction import load_model
import re
import numpy as np
import plotly.express as px

data = load_model()
regressor_loaded = data["model"]


def show_predict_page():
    st.title("Application for Client to Predict their next month spending")
    st.write("""This application is create to help you organise your budget by predicting your spending for the next month.""")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Write your name")
        favorite = st.selectbox("Select your favorite", ["🐈", "🐶", "🌷"])
        Hi = st.button("Click me")
    
        st.title(f"Hello {name.upper()}!{favorite}, Welcome to the application")
    with col2: 
        st.write("We need some information to predict your next month spending")
        age = st.number_input('Enter your age', min_value=15, max_value=95, step=1)
        st.write("The minimum age for our data is 15 and maximum is 95 years old")
        current_month_spending = st.number_input('Enter your current month spending', min_value=0, max_value=20000000, step=1)
        month_options = list(month_dict.keys())
        month = st.selectbox("month", month_options)
        month = month_dict[month]
        
    month_dict = {
        'Jan': 0,
        'Feb': 1,
        'March':2,
        'Apr': 3,
        'May': 4,
        'June':5,
        'July': 6,
        'Aug': 7,
        'Sep':8,
        'Oct': 9,
        'Nov': 10,
        'Dec':11,
        
    }
    

    ok = st.button("Calculate next month total spending")
    if ok:
        X = pd.DataFrame({
        'month': [month],
        'age':[age],
        'current_month_spending':[current_month_spending],
        })
        
        next_month = regressor_loaded.predict(X)
        next_month = np.round(next_month, 2)  # Round the value to two digits
        next_month_str = str(next_month[0])  # Convert to string

        # Display the predicted next month spending
        st.write(f"Your predict next month spending would be {next_month_str}")
    
    
    cates = pd.read_csv("https://raw.githubusercontent.com/wongwara/predict_next_month/main/age_cates.csv")
    st.subheader("Check what is the highest spending for your Age Group in the Heatmap")
    age_groups = {
        (15, 24): '15-24',
        (25, 34): '25-34',
        (35, 44): '35-44',
        (45, 54): '45-54',
        (55, 64): '55-64',
        (65, 74): '65-74',
        (75, 84): '75-84',
        (85, 95): '85-95'
        }
    def determine_age_group(age):
        for group_range, group_name in age_groups.items():
            if group_range[0] <= age <= group_range[1]:
                return group_name
        return "Unknown"
    # Determine the age group
    age_group = determine_age_group(age)

    # Display the age group box
    st.info(f"Your age group: {age_group}")
    st.write(""" The below table shows the maximum amont spend in each age group""")
    # Find the maximum value in each column
    cates = round(cates,2)
    def highlight_max(s):
        is_max = s == s.max()
        return ['background-color: yellow' if v else '' for v in is_max]

    # Display the table in Streamlit
    st.write(cates.style.apply(highlight_max, axis=0))
    
 
    st.write("""Wongwara Wijara 14191732 """)
    st.write(""" 36106 Machine Learning Algorithms and Applications - Autumn 2023 University of Technology Sydney """)
