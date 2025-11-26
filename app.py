import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header("Analisis exploratorio vehicles dataset")


hist_checkbox = st.checkbox("Construir Histograma")
scatter_checkbox = st.checkbox("Construir diagrama de dispersion ")
if hist_checkbox:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig,use_container_width=True)

if scatter_checkbox:
    st.write("Creacion de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches")
    fig = px.scatter(car_data,x="odometer", y="price")
    st.plotly_chart(fig,use_container_width=True)