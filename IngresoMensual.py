import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Cargar el modelo entrenado
with open('modelprediccion.pkl', 'rb') as file:
    model1 = pickle.load(file)

# Título de la app
st.title("Predicción con Modelo Bosque Aleatório")

# Descripción
st.write("Ingrese los valores de las características para obtener el Ingreso Mensual.")

#Opciones para Género
gender_options = {
    "Masculino": 0,
    "Femenino": 1,
}

gender_label = st.selectbox(
    "Seleccione el Género", 
    options=list(gender_options.keys())
)

#Opciones para Rol de Trabajo
role_options = {
    'Media': 0, 'Educación': 1, 'Tecnología': 2, 'Finanzas': 3, 
    'Cuidado de la salud': 4, 'Ejecutiva/o de ventas': 5, 'Gerente': 6, 'Director de Investigación': 7,
    'Representante de ventas': 8, 'Técnica/o de laboratorio': 9, 'Científica/o de investigación': 10,
    'Director de Manufactura': 11, 'Representante de atención médica': 12, 'Recursos humanos': 13
}

role_label = st.selectbox(
    "Seleccione el Rol de Trabajo", 
    options=list(role_options.keys())
)

#Opciones para Balance Trabajo-Vida
balance_options = {
    'Pobre': 0, 'Justo': 1, 'Bueno': 2, 'Excelente': 3
}

balance_label = st.selectbox(
    "Seleccione el Balance Trabajo-Vida", 
    options=list(balance_options.keys())
)

#Opciones para Satisfacción del Tabajo
satisfaccion_options = {
    'Bajo': 0, 'Medio': 1, 'Alto': 2, 'Muy Alto': 3
}

satisfaccion_label = st.selectbox(
    "Seleccione la Satisfacción del Tabajo", 
    options=list(satisfaccion_options.keys())
)

#Opciones para Desempeño
desempeno_options = {
    'Bajo': 0, 'Por debajo del promedio': 1, 'Promedio': 2, 'Alto': 3
}

desempeno_label = st.selectbox(
    "Seleccione el Desempeño", 
    options=list(desempeno_options.keys())
)

#Opciones para Horas Extras
overtime_options = {
    'Si': 1, 'No': 0
}

overtime_label = st.selectbox(
    "Seleccione si tiene Horas Extras", 
    options=list(overtime_options.keys())
)

#Opciones para Nivel de Educación
educacion_options = {
    'Secundario': 0, 
    'Grado asociado': 1, 
    'Licenciatura': 2, 
    'Maestría': 3, 
    'Doctor en Filosofía': 4
}

educacion_label = st.selectbox(
    "Seleccione el Nivel de Educación", 
    options=list(educacion_options.keys())
)

#Opciones para Nivel de Trabajo
job_options = {
    'Mid': 0, 'Entry': 1, 'Senior': 2
}

job_label = st.selectbox(
    "Seleccione el Nivel de Trabajo", 
    options=list(job_options.keys())
)

#Opciones para Tamaño de Empresa
tamano_options = {
    'Media': 0, 'Pequeña': 1, 'Grande': 2
}

tamano_label = st.selectbox(
    "Seleccione el Tamaño de Empresa", 
    options=list(tamano_options.keys())
)

#Opciones para Trabajo Remoto
remoto_options = {
    'Si': 1, 'No': 0
}

remoto_label = st.selectbox(
    "Seleccione si hace Trabajo Remoto", 
    options=list(remoto_options.keys())
)

#Opciones para Oportunidades de Liderazgo
liderazgo_options = {
    'Si': 1, 'No': 0
}

liderazgo_label = st.selectbox(
    "Seleccione si tiene Oportunidades de Liderazgo", 
    options=list(liderazgo_options.keys())
)

#Opciones para Oportunidades de Innovación
innovacion_options = {
    'Si': 1, 'No': 0
}

innovacion_label = st.selectbox(
    "Seleccione si tiene Oportunidades de Innovación", 
    options=list(innovacion_options.keys())
)

#Opciones para Reputación de la Empresa
reputacion_options = {
    'Justa': 0, 'Buena': 1, 'Excelente': 2, 'Pobre': 3
}

reputacion_label = st.selectbox(
    "Seleccione la Reputación de la Empresa", 
    options=list(reputacion_options.keys())
)

#Opciones para Reconocimiento a Empleado
reconocimiento_options = {
    'Bajo': 0, 'Medio': 1, 'Alto': 2, 'Muy Alto': 3
}

reconocimiento_label = st.selectbox(
    "Seleccione el Reconocimiento a Empleado", 
    options=list(reconocimiento_options.keys())
)

#Opciones para Deserción
desercion_options = {
    'Permanece': 0, 'Deserción': 1
}

desercion_label = st.selectbox(
    "Seleccione estado de Deserción", 
    options=list(desercion_options.keys())
)

# Crear un formulario para la entrada de datos del usuario
input_data = {}

input_data['Edad'] = st.number_input("Ingrese el valor de Edad", min_value=18.0, max_value=60.0, value=18.0)
input_data['Género'] = gender_options[gender_label]
input_data['Antigüedad en la Empresa'] = st.number_input("Ingrese el valor de Antigüedad en la Empresa", min_value=0.0, max_value=43.0, value=0.0)
input_data['Rol de Trabajo'] = role_options[role_label]
input_data['Balance Trabajo-Vida'] = balance_options[balance_label]
input_data['Satisfacción del Trabajo'] = satisfaccion_options[satisfaccion_label]
input_data['Desempeño'] = desempeno_options[desempeno_label]
input_data['Número de Promociones'] = st.number_input("Ingrese el valor de Número de Promociones", min_value=0.0, max_value=4.0, value=0.0)
input_data['Horas Extras'] = overtime_options[overtime_label]
input_data['Distancia a Casa'] = st.number_input("Ingrese el valor de Distancia a Casa", min_value=1.0, max_value=99.0, value=1.0)
input_data['Nivel de Educación'] = educacion_options[educacion_label]
input_data['Número de Dependientes'] = st.number_input("Ingrese el valor de Número de Dependientes", min_value=0.0, max_value=6.0, value=0.0)
input_data['Nivel de Trabajo'] = job_options[job_label]
input_data['Tamaño de Empresa'] = tamano_options[tamano_label]
input_data['Trabajo Remoto'] = remoto_options[remoto_label]
input_data['Oportunidades de Liderazgo'] = liderazgo_options[liderazgo_label]
input_data['Oportunidades de Innovación'] = innovacion_options[innovacion_label]
input_data['Reputación de la Empresa'] = reputacion_options[reputacion_label]
input_data['Reconocimiento a Empleado'] = reconocimiento_options[reconocimiento_label]
input_data['Deserción'] = desercion_options[desercion_label]

# Crear botón para realizar predicción
if st.button("Realizar Predicción"):
    # Convertir los datos en un array o DataFrame de acuerdo al modelo
    input_df = np.array([input_data])
    scaler = MinMaxScaler()
    input_data_normalized = scaler.transform(input_df)
    # Realizar la predicción
    prediction_normalized = model1.predict(input_data_normalized)

    # Desnormalizar la salida, si es necesario (por ejemplo, si predice un salario)
    min_val, max_val = '1009', '19999' # Rango original usado en la normalización del entrenamiento
    prediction_original = prediction_normalized * (max_val - min_val) + min_val

    # Mostrar el resultado
    st.write("La predicción del Ingreso Mensual es:", prediction_original)
