import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('Advertising.csv')
st.write("""
# Simple Prediction App
This app predicts the **Advertising Sales** type!
""")

st.sidebar.header('User Input Parameters')
st.write(df)

def user_input_features():
    TV_value = st.sidebar.slider
    Newspaper_value = st.sidebar.slider
    Radio_value = st.sidebar.slider
      data = {'TV_value': TV_value,
            'Newspaper_value': Newspaper_value,
            'Radio_value': Radio_value}
    features = pd.DataFrame(data, index=[0])
    return features

