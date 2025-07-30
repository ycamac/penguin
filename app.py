import pandas as pd
import numpy
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

st.title('Penguine Specie Prediction ML App')
st.info('This is a end-to-end Machine Learning App')

with st.expander("Data"):
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df
with st.expander("Data Visialization"):
  pass
with st.expander("Input Data"):
  pass
with st.expander("Data Preparation"):
  pass
with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1,21.5,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172,231,201)
  body_mass_g = st.slider('Body mass (g)', 2700,6300,4207)
  gender = st.selectbox('Gender', ('male','female'))
