import streamlit as st

def bienvenida(nombre):
    mymensaje = 'bienvenido/a : ' + nombre
    return mymensaje

myname=st.text_input('Nombre: ')
if (myname):
    mensaje= bienvenida(myname)
    st.write(f'mensaje: {myname}')