import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Choose a the following site : ', ('EDA', 'Predict A Class'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()