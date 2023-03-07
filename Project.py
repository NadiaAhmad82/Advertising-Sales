import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Advertising Sales App

This app predicts the **Adverstising Sales** type!
""")

st.sidebar.header('User Input Parameters')

