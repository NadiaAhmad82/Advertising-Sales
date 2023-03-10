import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
df = pd.read_csv('Advertising.csv')
st.write("""
# Simple Prediction App
This app predicts the **Advertising Sales** type!
""")

st.sidebar.header('User Input Parameters')
st.write(df)

def user_input_features():
    TV_Value = st.sidebar.slider('TV Value ', 0, 150, 300)
    Radio_Value = st.sidebar.slider('Radio Value', 0, 25, 50)
    Newspaper_Value = st.sidebar.slider('Newspaper Value', 0, 70, 150)
    
  
    data = {'TV': TV_Value,
            'Radio': Radio_Value,
            'Newspaper': Newspaper_Value}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

data = pd.read_csv('Advertising.csv')
data = data.drop(data.columns[0], axis=1)

X = data[['TV','Radio', 'Newspaper']]
y = data['Sales']

regr = LinearRegression()
regr.fit(X,y)

prediction = regr.predict(df)

st.subheader('Prediction')
st.write(prediction[0])




