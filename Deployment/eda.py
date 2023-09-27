import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


st.set_page_config(
    page_title= 'Pistachio Types',
    layout='wide',
    initial_sidebar_state = 'expanded'
    )

def run ():
    # Membuat Title
    st.title('Pistachio Types Prediction')

    # Membuat Sub Header
    st.subheader('EDA of Dataset Pistachio Types')

    # Menambah Gambar
    image = Image.open('pistachio.jpg')
    st.image(image, caption ='Pistachio')

    # Menambahkan deskripsi

    st.write('Made by **Abi Sugiri**')
    
    
    

    # Membuat Garis Lurus
    st.markdown('----')

    # Show DataFrame
    #Loading Data
    data = pd.read_csv('h8dsft_P1M2_abi_sugiri.csv')
    st.dataframe(data)

    # Membuat Heatmap
    
    data_heatmap = data
    data_heatmap["Class"] = np.where(data["Class"] == "Kirmizi_Pistachio", 0, 1)                
    st.write('#### Plot Correlation Heatmap')
    fig = plt.figure(figsize=(25, 10))
    sns.heatmap(data_heatmap.corr(),annot=True)
    st.pyplot(fig)
    
    st.write('\n\n### Kirmizi_Pistachio is assigned to class "0" dan Siit_Pistachio is assigned to class "1"\n\n')
    
    # Membuat Histogram berdasarkan input User
    st.write('#### Histogram based on input')
    pilihan = st.selectbox('Pilih Column : ', ('AREA', 'PERIMETER', 'MAJOR_AXIS', 'MINOR_AXIS'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Scatter plot berdasarkan input User
    st.write('#### Scatter plot based on input')
    pilihan_x = st.selectbox('Pilih X : ', ('MAJOR_AXIS', 'MINOR_AXIS', 'ROUNDNESS', 'COMPACTNESS', 'ASPECT_RATIO', 'CONVEX_AREA', 'EXTENT'))
    pilihan_y = st.selectbox('Pilih Y : ', ('COMPACTNESS', 'MAJOR_AXIS', 'MINOR_AXIS', 'ROUNDNESS', 'ASPECT_RATIO', 'CONVEX_AREA', 'EXTENT'))
    fig = plt.figure(figsize=(15, 5))
    sns.scatterplot(data, x=data[pilihan_x], y=data[pilihan_y], hue='Class')
    st.pyplot(fig)


if __name__ == '__main__':
    run()