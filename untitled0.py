import streamlit as st
import pandas as pd
from pathlib import Path

den = Path(__file__).parents[1] 
st.write(den)
nav = st.sidebar.radio("Navigation",["Home","1st Assignment"])
if nav == "Home":
    st.title("Data Analyst Assignments")
    st.write(den)
elif nav == "1st Assignment":
   uploaded_files = st.file_uploader("Choose a CSV file", type="xlsx")
   if uploaded_files:
       df = pd.read_excel(uploaded_files)
       st.table(df)
