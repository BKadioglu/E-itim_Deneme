import streamlit as st


nav = st.sidebar.radio("Navigation",["Home","Linear Regression Model"])
if nav == "Home":
    video_file = open(r'C:\Users\berke\OneDrive\Masaüstü\first_vid.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
