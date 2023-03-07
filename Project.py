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
         
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn

knn.fit(Xtrain, ytrain)
