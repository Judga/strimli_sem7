import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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


df = pd.read_csv("pages/static/datasets/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250425.csv")

st.subheader("Vista previa de los datos")
st.dataframe(df.head(20))

st.sidebar.title("Explorador interactivo")


st.sidebar.markdown("### Selección por índice (iloc)")
start_row = st.sidebar.number_input("Fila inicial", min_value=0, max_value=len(df)-1, value=0)
end_row = st.sidebar.number_input("Fila final (no inclusiva)", min_value=1, max_value=len(df), value=5)
if start_row < end_row:
    st.write(f"Filas seleccionadas con `.iloc[{start_row}:{end_row}]`")
    st.dataframe(df.iloc[start_row:end_row])
else:
    st.warning("La fila final debe ser mayor que la inicial.")


st.sidebar.markdown("### Selección por columnas (loc)")
columnas = st.sidebar.multiselect("Selecciona columnas", df.columns.tolist(), default=list(df.columns[:3]))
if columnas:
    st.write(f"Columnas seleccionadas con `.loc[:, {columnas}]`")
    st.dataframe(df.loc[:, columnas])


st.sidebar.markdown("### Filtro por valor")
columna_filtro = st.sidebar.selectbox("Columna para filtrar", df.columns)
valores_unicos = df[columna_filtro].dropna().unique()
valor_seleccionado = st.sidebar.selectbox("Valor a filtrar", valores_unicos)
df_filtrado = df.loc[df[columna_filtro] == valor_seleccionado]
st.write(f"Filas donde `{columna_filtro}` es `{valor_seleccionado}`")
st.dataframe(df_filtrado.head(20))


st.sidebar.markdown("### Modificación de datos")
modificar = st.sidebar.checkbox("Modificar un valor")
if modificar:
    fila_mod = st.sidebar.number_input("Fila a modificar", min_value=0, max_value=len(df)-1, value=0)
    columna_mod = st.sidebar.selectbox("Columna a modificar", df.columns, key="mod_col")
    nuevo_valor = st.sidebar.text_input("Nuevo valor", value=str(df.at[fila_mod, columna_mod]))
    if st.sidebar.button("Aplicar cambio"):
        df.at[fila_mod, columna_mod] = nuevo_valor
        st.success(f"Valor en fila {fila_mod}, columna '{columna_mod}' modificado a: {nuevo_valor}")
        st.dataframe(df.iloc[[fila_mod]])

st.info("Puedes combinar los filtros y selecciones para explorar el DataFrame de diferentes maneras usando `.loc` y `.iloc`.")
