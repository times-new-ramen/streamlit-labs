import streamlit as st
import pandas as pd

DATA_URL= 'uber-raw-data-sep14.csv'
DATE_COLUMN= 'Date/Time'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data= load_data(100)
st.dataframe(data)

st.map(data)
