import streamlit as st
from services.user_service import create_user

st.title("User Registration via Kafka")

username = st.text_input("Username")
email = st.text_input("Email")

if st.button("Register"):
    if username and email:
        create_user(username, email)
        st.success(f"User {username} registered and event sent to Kafka!")
    else:
        st.warning("Please enter both username and email.")