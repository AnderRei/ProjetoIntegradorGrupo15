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

# =========================
# FILTROS
# =========================
st.sidebar.header("🔎 Filtros")

categorias = st.sidebar.multiselect(
    "Categoria:",
    options=sorted(df["categoria"].unique()),
    default=sorted(df["categoria"].unique())
)

tipos = st.sidebar.multiselect(
    "Tipo de Produto:",
    options=sorted(df["tipo_produto"].unique()),
    default=sorted(df["tipo_produto"].unique())
)

df_filtrado = df[
    (df["categoria"].isin(categorias)) &
    (df["tipo_produto"].isin(tipos))
]

# =========================
# AGRUPAMENTO
# =========================
resumo = df_filtrado.groupby("categoria").agg({
    "avaliacao": "mean",
    "qtd_avaliacoes": "sum",
    "codigo": "count",
    "valor_total_vendas": "sum"
}).reset_index()

resumo = resumo.rename(columns={
    "avaliacao": "rating_medio",
    "qtd_avaliacoes": "total_avaliacoes",
    "codigo": "total_produtos",
    "valor_total_vendas": "vendas_totais"
})

# =========================
# MÉTRICA DE POTENCIAL
# =========================
resumo["potencial"] = resumo["rating_medio"] * np.log1p(resumo["total_avaliacoes"])

# =========================
# MÉTRICAS GERAIS
# =========================
st.subheader("📈 Visão Geral")

col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Produtos", df_filtrado.shape[0])
col2.metric("⭐ Avaliações", int(df_filtrado["qtd_avaliacoes"].sum()))
col3.metric("📂 Categorias", df_filtrado["categoria"].nunique())
col4.metric("💰 Vendas (estimado)", f"{df_filtrado['valor_total_vendas'].sum():,.0f}")

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
    st.subheader("🔥 Popularidade (Avaliações)")
    st.bar_chart(
        resumo.set_index("categoria")["total_avaliacoes"]
    )

with col2:
    st.subheader("⭐ Rating Médio")
    st.bar_chart(
        resumo.set_index("categoria")["rating_medio"]
    )

# =========================
# GRÁFICO DE VENDAS
# =========================
st.subheader("💰 Vendas por Categoria")

st.bar_chart(
    resumo.set_index("categoria")["vendas_totais"]
)

# =========================
# TIPO DE PRODUTO
# =========================
st.subheader("📦 Distribuição por Tipo de Produto")

st.bar_chart(
    df_filtrado["tipo_produto"].value_counts()
)

# =========================
# RANKING COMPLETO
# =========================
st.subheader("📊 Ranking Geral")

st.dataframe(
    resumo.sort_values(by="potencial", ascending=False)
)

# =========================
# TABELA DETALHADA 
# =========================
with st.expander("🔍 Ver dados detalhados"):
    st.dataframe(df_filtrado)
