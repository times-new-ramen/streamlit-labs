import streamlit as st
import pandas as pd
import numpy as np


DATA_URL = 'uber-raw-data-sep14.csv'
DATE_COLUMN='Date/Time'

st.title('Visualización --- Uber')
sidebar=st.sidebar
st.sidebar.caption('Controla los gráficos con las barras móviles') 
st.write('Este dashboard tiene el propósito de mostrar los datos de Uber')

@st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    lowercase=lambda x: str(x).lower()
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    data.rename(lowercase,axis='columns', inplace=True)
    return data

data=load_data(1000)
st.dataframe(data)
st.map(data)

#Funciones 

st.sidebar.slider('Selecciona la fecha',
min_value=float(data[DATE_COLUMN].min()),
max_value=float(data[DATE_COLUMN].max())
)
