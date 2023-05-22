import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go

def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/wongwara/predict_next_month/main/df_monthly.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Predict next month")
  
    st.write(
        """ 
       As bank data scientists, we employ machine learning to analyse the huge amount of data available in banking. This data includes transaction history, client information, and meaningful financial information. We can swiftly process and evaluate this massive amount of data by leveraging machine learning algorithms' capabilities, detecting anomalies, and making accurate forecasts.
       """
    ) 
    
    st.write(
        """
             Therefore, the objective of this project would be to develop a machine learning model that accepts a job title and the job description with any related words from the job as input and returns expected salary associated with that job.
             """
            )
    st.subheader("The highest demand job classification in Australia")
