import streamlit as st
import pandas as pd
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")
df = pd.read_csv("pages/static/datasets/estudiantes_colombia.csv")
df.info()
df.describe()

print(df[['id', 'nombre', 'edad', 'ciudad']].head())
print(df[['id', 'nombre', 'edad', 'ciudad']].tail())


promedio = st.slider("Selecciona un rango de promedio", 0.0, 5.0, (4.0, 4.5))
st.write(df[(df['promedio'] >= promedio[0]) & (df['promedio'] <= promedio[1])])
