import streamlit as st
import streamlit_player
from streamlit_player import st_player

nav = st.sidebar.radio("Navigation",["Home","Linear Regression Model"])
if nav == "Home":
    st_player("https://youtu.be/CmSKVW1v0xM")
