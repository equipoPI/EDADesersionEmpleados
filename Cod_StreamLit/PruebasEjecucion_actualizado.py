import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Análisis y Predicción de Empleados", layout="wide")

# Creación de pestañas
tab1, tab2 = st.tabs(["Visualización EDA", "Predicciones y Clasificación"])

# Contenido de la pestaña 1: Visualización EDA
with tab1:
    st.header("Visualización del Análisis Exploratorio de Datos (EDA)")
    # Agrega tu código para visualizaciones EDA aquí
    st.write("Aquí irán los gráficos y visualizaciones del EDA.")

# Contenido de la pestaña 2: Predicciones y Clasificación
with tab2:
    st.header("Predicción del Ingreso Mensual y Clasificación del Empleado")
    # Agrega tu código para predicciones y clasificación aquí
    st.write("Aquí irán los resultados de las predicciones y clasificaciones.")
