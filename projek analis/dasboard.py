import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis Data")

data = pd.read_csv("database.csv")
st.write("Preview Data", data.head())

st.subheader("Statistik Deskriptif")
st.write(data.describe())

column = st.selectbox("Pilih kolom", data.columns)
if data[column].dtype == "year" or data[column].nunique() < 30:
    fig, ax = plt.subplots()
    data[column].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)
else:
    st.warning("Kolom ini bukan.")
