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
       df = pd.read_excel(r"/app/den.xlsx")
       st.table(df)
