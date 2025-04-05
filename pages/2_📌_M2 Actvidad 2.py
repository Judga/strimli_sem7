import streamlit as st
import pandas as pd
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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
st.header("Solución")
df = pd.read_csv("pages/static/datasets/estudiantes_colombia.csv")
df.info()
df.describe()
st.subheader("Selección de columnas: Nombre, Edad y Promedio")
st.write(df[['nombre', 'edad', "promedio"]])
opcion = st.selectbox("¿Qué quieres explorar?", 
                      ["Nombres", "Edad", "Promedio"])

if opcion == "Nombres":
    st.write(df.head())
elif opcion == "Edad":
    st.write(df.describe())
elif opcion == "Promedio":
    promedio = st.slider("promedio", 0, 7, 2)
    st.write(df[df['promedio'] >= promedio])
