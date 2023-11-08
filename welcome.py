# welcome.py
import streamlit as st

def show_welcome_page():
    st.title("Welcome to the Uber Pickups App!")
    st.write("This application helps you analyze Uber pickups in New York City. Use the sidebar to navigate to different pages.")
    st.write("You can view interactive charts, maps of Uber pickup locations, and more insights by choosing the 'Main App' page.")


    if st.button("Logout"):
        logout_user()
