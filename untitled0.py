import streamlit as st
import pandas as pd

nav = st.sidebar.radio("Navigation",["Home","1st Assignment"])
if nav == "Home":
    st.title("Data Analyst Assignments")
elif nav == "1st Assignment":
    df = pd.read_excel("den.xlsx")
    st.table(df)
