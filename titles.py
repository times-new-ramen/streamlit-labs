import streamlit as st
import numpy as np
import pandas as pd


#crear title de la webapp
st.title("Streamlit con Sidebar")

sidebar= st.sidebar
sidebar.title("Título de barra lateral", )

sidebar.write("Información de mi sidebar")

st.header("Header de mi app")
st.write("Información de mi app")

if sidebar.checkbox("Show dataframe"):
    chart_data= pd.DataFrame(
        np.random.randint(10,20,size=(6,3)),
        columns=['a','b','c'])
    st.dataframe(chart_data)
