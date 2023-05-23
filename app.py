import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    secret_key = "your_secret_key"  # Replace with your own secret key

    entered_key = st.text_input("Enter the secret key", type="password")

    if entered_key == secret_key:
        st.success("Authentication successful!")
        show_predict_page()
        # Add your application logic here
    else:
        st.error("Authentication failed!")
else:
    show_explore_page()
