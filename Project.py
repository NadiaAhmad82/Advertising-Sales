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
    TV_Value = st.sidebar.slider('TV Value ', 0, 150, 300)
    Newspaper_Value = st.sidebar.slider('Newspaper Value', 0, 70, 120)
    Radio_Value = st.sidebar.slider('Radio Value', 0, 25, 50)
  
    data = {'TV_Value': TV_Value,
            'Newspaper_Value': Newspaper_Value,
            'Radio_Value': Radio_Value}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

Advertising = datasets.load_Advertising.csv()
X = Advertising.Sales
Y = Advertising.target

clf = RandomForestClassifier()
clf.fit(X, Y)



