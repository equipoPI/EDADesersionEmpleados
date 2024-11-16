import streamlit as st

# Título de la página
st.title("Mi primera página en Streamlit")

# Encabezado
st.header("¡Bienvenido!")

# Texto de descripción
st.write("Esta es una aplicación básica de ejemplo creada con Streamlit.")

# Entrada de texto
nombre = st.text_input("Ingresa tu nombre:")

# Botón
if st.button("Saludar"):
    if nombre:
        st.success(f"¡Hola, {nombre}! Bienvenido a Streamlit.")
    else:
        st.warning("Por favor, ingresa tu nombre.")

# Entrada numérica
numero = st.number_input("Ingresa un número:", value=0)

# Mostrar el doble del número
st.write(f"El doble de {numero} es {numero * 2}.")
