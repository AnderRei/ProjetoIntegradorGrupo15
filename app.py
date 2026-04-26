import streamlit as st
from src.tratamento import carregar_e_tratar

st.title("Dashboard - Produtos")

df = carregar_e_tratar()

st.subheader("Dados tratados")
st.write(df)

st.subheader("")
