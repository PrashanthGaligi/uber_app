# utils.py
import streamlit as st
import pandas as pd

DATA_URL = 'data/uber-raw-data-sep14.csv'


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data = data.rename(str.lower, axis='columns')
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data
# ... rest of the utils.py functions


def check_login_status(username, password):
    # This should be a database check in production
    users = {
        "user1": "password1",
        "user2": "password2"
    }
    return username in users and users[username] == password

def logout_user():
    st.session_state['logged_in'] = False

