import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json


#Load all files

with open('model_scaler.pkl', 'rb') as file_1:
  scaler = pickle.load(file_1)

with open('rf_clf.pkl', 'rb') as file_2:
  rf_clf = pickle.load(file_2)


def run():
    # Membuat Form
    with st.form(key='Pistachio Class Prediction'):
      area = st.number_input('AREA', min_value=30000, max_value=124000, value=50000, step=100, help='maximal value = 124000')
      perimeter = st.slider('PERIMETER', 860, 2755, 1000)
      major_axis = st.slider('MAJOR_AXIS', 322, 535, 350)
      minor_axis = st.slider('MINOR_AXIS', 134, 383, 200)
      eccentricity= st.slider('ECCENTRICITY',0.5, 0.9, 0.7)
      st.markdown('---')

      eqdiascq = st.slider('EQDIASQ', 195, 397, 250)
      solidity = st.slider('SOLIDITY', 0.6, 0.99, 0.8)
      convex_area = st.slider('CONVEX_AREA', 38000, 132000, 25000)
      extent = st.slider('EXTENT', 0.43, 0.8, 0.6)
      st.markdown('---')
        
      aspect_ratio = st.number_input('ASPECT_RATIO', min_value=1.16, max_value=3.08, value=2.0, step=0.01)
      roundness = st.slider('ROUNDNESS', 0.06, 0.93, 0.5)
      compactness = st.slider('COMPACTNESS', 0.48, 0.86, 0.6)
      st.markdown('---')


      shapefactor_1 = st.number_input('SHAPEFACTOR_1', min_value=0.004, max_value=0.0131, value=0.01, help='maximal value = 0.0131')
      shapefactor_2 = st.number_input('SHAPEFACTOR_2', min_value=0.0024, max_value=0.0053, value=0.0030, help='maximal value = 0.0053')
      shapefactor_3 = st.number_input('SHAPEFACTOR_3', min_value=0.23, max_value=0.75, value=0.5, help='maximal value = 0.75')
      shapefactor_4 = st.number_input('SHAPEFACTOR_4', min_value=0.62, max_value=0.99, value=0.75, help='maximal value = 0.99')
      
      
      submitted = st.form_submit_button('Predict')
    data_inf = {
      'AREA' : area,
      'PERIMETER' : perimeter,
      'MAJOR_AXIS' : major_axis,
      'MINOR_AXIS' : minor_axis,
      'ECCENTRICITY' : eccentricity,
      'EQDIASQ' : eqdiascq,
      'SOLIDITY' : solidity,
      'CONVEX_AREA' : convex_area,
      'EXTENT' : extent,
      'ASPECT_RATIO': aspect_ratio,
      'ROUNDNESS' : roundness,
      'COMPACTNESS' : compactness,
      'SHAPEFACTOR_1' : shapefactor_1,
      'SHAPEFACTOR_2' : shapefactor_2,
      'SHAPEFACTOR_3' : shapefactor_3,
      'SHAPEFACTOR_4' : shapefactor_4
    }
        
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

        #Feature scaling and feature encoding
        data_inf_scaled = scaler.transform(data_inf)
        
        
        #Predict usiing linear regression
        y_pred_inf = rf_clf.predict(data_inf_scaled)
        if y_pred_inf == 0:
          st.write('## Pistachio Class : Kirmizi_Pistachio')
        
        else:
          st.write('## Pistachio Class : Siit_Pistachio')

if __name__ == '__main__':
    run()