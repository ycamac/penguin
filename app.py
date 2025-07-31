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

  st.write("Input Variables")
  X_raw = df.drop('species',axis=1)
  X_raw
  
  st.write("Tarjet Variables")
  y_raw = df.species
  y_raw

  st.write("Descriptive Statistics")
  des = df.describe()
  des
  
  st.write("Information about data")
  inf = df.info()
  st.write(inf)
  
with st.expander("Data Visualization"):
  st.scatter_chart(data = df, x='bill_length_mm',y='body_mass_g', color='species')
  
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

  data = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'gender': gender    
  }
  input_df = pd.DataFrame(data, index = [0])
  input_penguins =  pd.concat([input_df, X_raw], axis=0)

with st.expander("Input data"):
  st.write("**Input data**")
  input_df
  st.write("**Combined data**")
  input_penguins

#One hot enconding for X
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins, prefix = encode)
X = df_penguis[1:]
input_row = df_penguis[:1]

#One hot encoding for y
tarjet_mapper = {
  'Adelie':0,
  'Chinstrap':1,
  'Gentoo':2  
}

def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)

with st.expander('Data preparation'):
  st.write('**Encoded X (input penguin)**')
  input_row
  st.write('**Encoded y**')
  y


# Model training and inference
## Train the ML model
clf = RandomForestClassifier()
clf.fit(X, y)

## Apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_proba.rename(columns={0: 'Adelie',
                                 1: 'Chinstrap',
                                 2: 'Gentoo'})

# Display predicted species
st.subheader('Predicted Species')
st.dataframe(df_prediction_proba,
             column_config={
               'Adelie': st.column_config.ProgressColumn(
                 'Adelie',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'Chinstrap': st.column_config.ProgressColumn(
                 'Chinstrap',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'Gentoo': st.column_config.ProgressColumn(
                 'Gentoo',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
             }, hide_index=True)
