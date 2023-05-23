import streamlit as st
import pandas as pd
from prediction import load_model
import re
import numpy as np

data = load_model()
regressor_loaded = data["model"]


def show_predict_page():
    st.title("🌸 Application for Client to Predict their next month spending")
    st.write("""This application is create to help you organise your budget by predicting your spending for the next month.""")
    
    st.text_input("Write your name")
    st.selectbox("Select your favorite", ["cat", "dog", "flower"])
    st.button("Click me")
    
    st.title("Hi Customer!")
    st.subheader("We need some information to predict your next month spending")
    age = st.number_input('Enter your age', min_value=15, max_value=95, step=1)
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
    
   
    month_options = list(month_dict.keys())
    month = st.selectbox("month", month_options)
    month = month_dict[month]
    

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
    
    st.write("""Wongwara Wijara 14191732 """)
    st.write(""" 36106 Machine Learning Algorithms and Applications - Autumn 2023 University of Technology Sydney """)
