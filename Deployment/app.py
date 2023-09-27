import streamlit as st
from streamlit_option_menu import option_menu
import eda
import prediction
import contact


st.write('### Pistachio Types Prediction')
st.write('##### Made by [Abi Sugiri](https://github.com/abisugiri)')
st.markdown('---')


selected = option_menu(None, ["EDA", "Prediction","Contact"], 
    icons=['graph-up', 'search', 'envelope-at-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "icon": {"color": "green", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "grey"},
    }
)
    
selected

if selected == 'EDA':
    eda.run()
elif selected == 'Prediction':
    prediction.run()
else:
    contact.run()