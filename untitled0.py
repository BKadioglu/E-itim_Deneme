import streamlit as st


nav = st.sidebar.radio("Navigation",["Home","Linear Regression Model"])
if nav == "Home":
    video_file = open('first_vid', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
