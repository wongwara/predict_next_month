import streamlit as st
import pandas as pd
from prediction import load_model
import re

data = load_model()
regressor_loaded = data["model"]


def show_predict_page():
    st.title("Predict Next Month")
    st.write("""Client Financial management: Help clients organise their budget by predicting their spending for the next month. This will help improve financial stability and overall pleasure.""")
    st.subheader("We need some information to predict your next month")

    age = st.number_input('Enter your age', min_value=0, max_value=150, step=1)
    current_month_spending = st.number_input('Enter your current month spending', min_value=0, max_value=20000000, step=1)
    
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
    
    gender_dict = {
        'Male': 1,
        'Female': 0,
    }
    
    
    st.subheader("**month**")
    month_options = list(month_dict.keys())
    month = st.selectbox("month", month_options)
    month = month_dict[month]
    gender_options = list(gender_dict.keys())
    gender = st.selectbox("gender", gender_options)
    gender = gender_dict[gender]

    ok = st.button("Calculate next month total spending")
    if ok:
        X = pd.DataFrame({
        'month': [month],
        'gender': [gender],
        'age':[age],
        'current_month_spending':[current_month_spending],
        })
        
        next_month = regressor_loaded.predict(X)
        next_month = np.round(next_month, 2)  # Round the value to two digits
        next_month_str = str(next_month[0])  # Convert to string

        # Display the predicted next month spending
        st.write(f"Your next month spending will be: {next_month_str}")
      
    st.write(""" 36106 Machine Learning Algorithms and Applications - Autumn 2023 University of Technology Sydney """)
