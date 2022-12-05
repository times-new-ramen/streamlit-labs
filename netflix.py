import pandas as pd
import calendar
import plotly.express as px
from PIL import Image
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Filtros de Netflix",
                page_icon=":movie_camera:",
                layout="wide")

st.title('Filtros de Netflix :movie_camera:')

DATA_UPLOAD='movies.csv'
df=pd.read_csv(DATA_UPLOAD)


mytitle=st.sidebar.text_input('Ingresa el título de la película')

if st.sidebar.button('Search'):
#    df_title = df.loc[(df['name'] == mytitle), ['company','director','genre','name']]
    filtered_data_filme = df[df['name'].str.upper().str.contains(mytitle.upper())]
#    df_title = df['name'].str.upper().str.contains(mytitle.upper())
    count_row=filtered_data_filme.shape[0]
    st.write(f'Películas totales: {count_row}')
    st.dataframe(filtered_data_filme)

director_list=df['director'].unique().tolist()
mydirector=st.sidebar.selectbox('Selecciona al director: ', director_list)
showall=st.sidebar.checkbox('¿Mostrar todo?')

@st.cache
def load_data(select_director):
    data=pd.read_csv(DATA_UPLOAD)
    filtered_dir=data[data['director'].str.contains(select_director)]
    return filtered_dir

if (mydirector):
    fitleredbydir=load_data(mydirector)
    count_row=fitleredbydir.shape[0]
    st.write(f'Nombres totales: {count_row}')
    st.dataframe(fitleredbydir)  

if (showall):
    st.dataframe(df)