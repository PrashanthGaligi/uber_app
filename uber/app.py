# app.py
import streamlit as st
from login import show_login_page, show_main_app
from welcome import show_welcome_page  # assuming you have a welcome.py with this function

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Define navigation for your application
def main():
    # Show login page if not logged in, otherwise show welcome or main app page
    if st.session_state['logged_in']:
        # Show welcome page once logged in
        page = st.sidebar.radio("Choose your page", ("Welcome", "Main App"))
        if page == "Welcome":
            show_welcome_page()
        elif page == "Main App":
            show_main_app()
    else:
        show_login_page()

main()
