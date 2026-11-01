import streamlit as st
import pandas as pd

# Load your data
data = pd.read_csv("E:/DataScience_practice/data/employee_dataset.csv")  # Update path
st.title("Your Data Analysis App")
st.write("Explore your dataset")
st.dataframe(data)

# Add widgets/analysis as needed
column = st.selectbox("Select Column", data.columns)
st.write(f"Summary of {column}:")
st.write(data[column].describe())