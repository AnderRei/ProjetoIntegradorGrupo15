import streamlit as st
import pandas as pd
import numpy as np
from src.tratamento import carregar_e_tratar

st.set_page_config(layout="wide")

st.title("📊 Dashboard - Produtos Amazon")

# =========================
# CARREGAR DADOS
# =========================
df = carregar_e_tratar()

# Debug (ver as colunas disponíveis)
#st.write(df.columns)

# =========================
# FILTRO
# =========================
st.sidebar.header("🔎 Filtros")

categorias = st.sidebar.multiselect(
    "Selecione categorias:",
    options=df["categoria"].unique(),
    default=df["categoria"].unique()
)

df_filtrado = df[df["categoria"].isin(categorias)]

# =========================
# AGRUPAMENTO
# =========================
resumo = df_filtrado.groupby("categoria").agg({
    "avaliacao": "mean",
    "qtd_avaliacoes": "sum",
    "codigo": "count"
}).reset_index()

# Renomear corretamente
resumo = resumo.rename(columns={
    "avaliacao": "rating_medio",
    "qtd_avaliacoes": "total_avaliacoes",
    "codigo": "total_produtos"
})

# =========================
# MÉTRICA DE POTENCIAL
# =========================
resumo["potencial"] = resumo["rating_medio"] * np.log1p(resumo["total_avaliacoes"])

# =========================
# MÉTRICAS GERAIS
# =========================
st.subheader("📈 Visão Geral")

col1, col2, col3 = st.columns(3)

col1.metric("Total de Produtos", df_filtrado.shape[0])
col2.metric("Total de Avaliações", int(df_filtrado["qtd_avaliacoes"].sum()))
col3.metric("Categorias", df_filtrado["categoria"].nunique())

# =========================
# TOP 5 CATEGORIAS
# =========================
st.subheader("🏆 Top 5 Categorias (Potencial)")

top5 = resumo.sort_values(by="potencial", ascending=False).head(5)
st.dataframe(top5)

# =========================
# GRÁFICOS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Popularidade")
    st.bar_chart(
        resumo.set_index("categoria")["total_avaliacoes"]
    )

with col2:
    st.subheader("⭐ Rating Médio")
    st.bar_chart(
        resumo.set_index("categoria")["rating_medio"]
    )

# =========================
# TABELA COMPLETA
# =========================
st.subheader("📊 Ranking Geral")

st.dataframe(
    resumo.sort_values(by="potencial", ascending=False)
)
