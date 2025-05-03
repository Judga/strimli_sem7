import streamlit as st
import pandas 
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Proyecto Integrador de Analisis ")

st.header("Descripción de la actividad")
st.markdown("""
En este proyecto se analiza un archivo de datos publicos utilizando Streamlit y Python junto a uin par de sus librerias .
En este, exploraremos los datos de un archivo publico usando las distintas herramientas que se tienen disponibles.
""")

st.header("Objetivos del proyecto")

st.markdown("""
- Comprender los tipos de datos disponibles
- Analizar los datos disponibles
- Usar diferentes tipos de estructuras para filtrar datos
""")

st.header("Datos")
df = pd.read_csv("strimli_sem7/pages/static/datasets/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250425.csv")
df.info()
df.describe()
st.subheader("Selección de columnas: Nombre, Edad ")
st.write(df[['nombre', 'edad', "promedio"]])
opcion = st.selectbox("¿Qué quieres explorar?", 
                      ["Nombres", "Edad"])

if opcion == "Nombres":
    st.write(df.head())
elif opcion == "Edad":
    st.write(df.describe())
elif opcion == "Promedio":
    promedio = st.slider("promedio", 0, 7, 2)
    st.write(df[df['promedio'] >= promedio])