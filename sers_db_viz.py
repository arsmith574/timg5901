import streamlit as st
import pandas as pd
import numpy as np

st.title('Visualisation')

DATA_URL=('https://github.com/arsmith574/timg5901/blob/main/CompanyInventorycleaned.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data