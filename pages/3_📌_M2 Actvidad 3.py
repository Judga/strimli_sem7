import streamlit as st
import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import date

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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
colab_url = "https://colab.research.google.com/drive/13ob3GJkm40t7X-0NDe4dUMbfzU8VBWwr?usp=sharing"
if st.button("Actividad 3 con Colab 🚀"):
    st.markdown(f"[Haz clic aquí para abrir en Google Colab]({colab_url})", unsafe_allow_html=True)


n = 50
fake = Faker()
random.seed(42)
np.random.seed(42)

data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',            # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

df = pd.DataFrame(data)
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

df_nuevo = df.copy()

with st.sidebar:
    st.title("Filtros dinámicos")

    # 1. Filtro por rango de edad
    activar_edad = st.checkbox("Filtrar por rango de edad")
    if activar_edad:
        min_edad, max_edad = st.slider("Rango de edad", 15, 75, (18, 30))
        df_nuevo = df_nuevo[df_nuevo['edad'].between(min_edad, max_edad)]

    # 2. Filtro por municipios específicos
    activar_municipios = st.checkbox("Filtrar por municipios")
    municipios_opciones = [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales',
        'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'
    ]
    if activar_municipios:
        municipios_sel = st.multiselect("Municipios", municipios_opciones)
        if municipios_sel:
            df_nuevo = df_nuevo[df_nuevo['municipio'].isin(municipios_sel)]

    # 3. Filtro por ingreso mensual mínimo
    activar_ingreso = st.checkbox("Filtrar por ingreso mensual mínimo")
    if activar_ingreso:
        ingreso_min = st.slider("Ingreso mensual mínimo (COP)", 800_000, 12_000_000, 1_000_000, step=100_000)
        df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'] > ingreso_min]

    # 4. Filtro por ocupación
    activar_ocupacion = st.checkbox("Filtrar por ocupación")
    ocupaciones_opciones = [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico',
        'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero'
    ]
    if activar_ocupacion:
        ocupaciones_sel = st.multiselect("Ocupaciones", ocupaciones_opciones)
        if ocupaciones_sel:
            df_nuevo = df_nuevo[df_nuevo['ocupacion'].isin(ocupaciones_sel)]

    # 5. Filtro por tipo de vivienda no propia
    activar_vivienda = st.checkbox("Filtrar personas sin vivienda propia")
    if activar_vivienda:
        df_nuevo = df_nuevo[df_nuevo['tipo_vivienda'] != 'Propia']

    # 6. Filtro por nombres que contienen una cadena
    activar_nombre = st.checkbox("Filtrar por nombre")
    if activar_nombre:
        texto_nombre = st.text_input("Nombre contiene...")
        if texto_nombre:
            df_nuevo = df_nuevo[df_nuevo['nombre_completo'].str.contains(texto_nombre, case=False, na=False)]

    # 7. Filtro por año de nacimiento específico
    activar_anio = st.checkbox("Filtrar por año de nacimiento")
    if activar_anio:
        anios = list(range(1949, 2010))
        anio_sel = st.selectbox("Año de nacimiento", anios)
        df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].dt.year == anio_sel]

    # 8. Filtro por acceso a internet
    activar_internet = st.checkbox("Filtrar por acceso a internet")
    if activar_internet:
        acceso = st.radio("¿Acceso a internet?", ["Sí", "No"])
        valor = True if acceso == "Sí" else False
        df_nuevo = df_nuevo[df_nuevo['acceso_internet'] == valor]

    # 9. Filtro por ingresos nulos
    activar_nulos = st.checkbox("Filtrar por ingresos nulos")
    if activar_nulos:
        df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'].isnull()]

    # 10. Filtro por rango de fechas de nacimiento
    activar_fecha = st.checkbox("Filtrar por rango de fechas de nacimiento")
    if activar_fecha:
        fecha_inicio = st.date_input("Fecha de inicio", date(1949, 1, 1))
        fecha_fin = st.date_input("Fecha de fin", date(2009, 12, 31))
        df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

st.write("Resultados filtrados:", df_nuevo.shape[0])
st.dataframe(df_nuevo)