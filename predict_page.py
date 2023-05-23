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
    
    name = st.text_input("Write your name")
    favorite = st.selectbox("Select your favorite", ["🐈", "🐶", "🌷"])
    Hi = st.button("Click me")
    
    st.title(f"Hello {name.upper()}!{favorite}, Welcome to the application")
      
    st.write("We need some information to predict your next month spending")
    age = st.number_input('Enter your age', min_value=15, max_value=95, step=1)
    st.write("The minimum age for our data is 15 and maximum is 95 years old")
    current_month_spending = st.number_input('Enter your current month spending', min_value=0, max_value=20000000, step=1)
    st.write("The lowest monthly amont spending should be higher than 0")
    
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
    
    
    cates = pd.read_csv("https://raw.githubusercontent.com/wongwara/predict_next_month/main/age_cates.csv")
    st.title("Check what is the highest spending for your Age Group in the Heatmap")

    fig = px.imshow(cates.values, x=cates.columns, y=cates.index, color_continuous_scale='ice')
    fig.update_xaxes(side="top")  # Display x-axis labels on top
    
    # Set the axes labels and title
    fig.update_layout(
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        title="Age Group Heatmap"
    )
    
    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
 
    st.write("""Wongwara Wijara 14191732 """)
    st.write(""" 36106 Machine Learning Algorithms and Applications - Autumn 2023 University of Technology Sydney """)
