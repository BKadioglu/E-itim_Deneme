import streamlit as st
import pandas as pd

nav = st.sidebar.radio("Navigation",["Home","1st Assignment"])
if nav == "Home":
    st.title("Data Analyst Assignments")
elif nav == "1st Assignment":
   uploaded_files = st.file_uploader("Choose a CSV file", type="xlsx")
   if uploaded_files:
       df = pd.read_excel(uploaded_files)
       st.table(df)
