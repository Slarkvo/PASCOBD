import streamlit as st

#tìtulo de la aplicaciòn
st.title("ejercicios con bucles bàsicos en python")

#ejercicio 1: imprimir 10 veces 'Hola mundo'
st.subheader("Ejercicio1: imprimir 'Hola Mundo' 10 Veces")
if st.button("Ejecutar Ejercicio 1")
    for i in range(10):
        st.write("Hola mundo")
#Ejercicio 2: Imprimir los primeros 10 nùmeros
st.subheader("Ejercicio 2: Imprimir los primeros 10 nùmeros")
is st.button("Ejecutar Ejercicio 2")
    for i in range(1, 11):
        st.write(i)
#Ejercicio 3: Tabla de multiplicar
St. subheader("Ejercicio 3: Imprimir la tabla de multiplicar del nùmero ingresado")
num = st.number_imput("Ingrese un nùmero para ver su tabla de multiplicar del 1 al 12" min_value=1)
if st.button("Ejecutar Ejercicio3"):
    for i in range(1, 13):
        st.write(f"{num} x {i} = {num * i}")