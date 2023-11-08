# login.py
import streamlit as st
from utils import check_login_status, logout_user, load_data
import numpy as np

def show_login_page():
    st.subheader("Login to the Uber Pickups App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login_status(username, password):
            st.session_state['logged_in'] = True
        else:
            st.error("Incorrect username or password")



def show_main_app():
    st.title("Uber Pickups in NYC")
    
    # Load 10,000 rows of data into the dataframe for visualization
    data = load_data(10000)

    # Assuming you have a datetime column in your dataframe to filter by hour
    hour_to_filter = st.slider('hour', 0, 23, 17)  # default value set to 17
    filtered_data = data[data['date/time'].dt.hour == hour_to_filter]
    
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)

    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(data['date/time'].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

    if st.button("Logout"):
        logout_user()
