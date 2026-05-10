import streamlit as st
import pandas as pd
import numpy as np
from src.tratamento import carregar_e_tratar

st.set_page_config(layout="wide")

st.title(" Dashboard - Análise de Mercado Amazon ")

# =========================
# CARREGAR DADOS
# =========================
df = carregar_e_tratar()

# =========================
# FILTROS
# =========================
st.sidebar.header(" Filtros")

categorias = st.sidebar.multiselect(
    "Categoria",
    options=sorted(df["categoria"].unique()),
    default=sorted(df["categoria"].unique())
)

tipos = st.sidebar.multiselect(
    "Tipo de Produto",
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
    "valor_total_vendas": "sum",
    "preco_desconto": "mean"
}).reset_index()

resumo = resumo.rename(columns={
    "avaliacao": "rating_medio",
    "qtd_avaliacoes": "total_avaliacoes",
    "codigo": "total_produtos",
    "preco_desconto": "ticket_medio"
})

# =========================
# SCORE INTELIGENTE
# =========================
C = df_filtrado["avaliacao"].mean()
m = resumo["total_avaliacoes"].quantile(0.75)

resumo["score_bayesiano"] = (
    (resumo["total_avaliacoes"] / (resumo["total_avaliacoes"] + m)) * resumo["rating_medio"]
    + (m / (resumo["total_avaliacoes"] + m)) * C
)

resumo["score_final"] = (
    0.5 * resumo["score_bayesiano"]
    + 0.3 * np.log1p(resumo["total_avaliacoes"])
    + 0.2 * np.log1p(resumo["valor_total_vendas"])
)

# =========================
# MÉTRICAS GERAIS
# =========================
st.subheader(" Visão Geral")

col1, col2, col3, col4 = st.columns(4)

col1.metric(" Produtos", df_filtrado.shape[0])
col2.metric(" Avaliações", int(df_filtrado["qtd_avaliacoes"].sum()))
col3.metric(" Categorias", df_filtrado["categoria"].nunique())

valor = df_filtrado["preco_desconto"].mean()
valor_formatado = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

col4.metric(" Ticket Médio", valor_formatado)

# =========================
# TOP CATEGORIAS
# =========================
st.subheader(" Ranking de Categorias - Top 5")

top = resumo.sort_values(by="score_final", ascending=False)

st.dataframe(top.head(5))

# =========================
# GRÁFICOS PRINCIPAIS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader(" Popularidade (Avaliações)")
    st.bar_chart(
        resumo.set_index("categoria")["total_avaliacoes"]
    )

with col2:
    st.subheader(" Qualidade (Rating Médio)")
    st.bar_chart(
        resumo.set_index("categoria")["rating_medio"]
    )

# =========================
# SCATTER INSIGHTS
# =========================
st.subheader(" Avaliação vs Popularidade")

st.scatter_chart(
    df_filtrado,
    x="qtd_avaliacoes",
    y="avaliacao"
)

st.subheader(" Desconto vs Avaliação")

st.scatter_chart(
    df_filtrado,
    x="perc_desconto",
    y="avaliacao"
)

# =========================
# RECEITA POR CATEGORIA
# =========================
st.subheader(" Receita Estimada por Categoria")

st.bar_chart(
    resumo.set_index("categoria")["valor_total_vendas"]
)

# =========================
# TOP PRODUTOS
# =========================
st.subheader(" Top Produtos")

top_produtos = df_filtrado.sort_values(
    by="valor_total_vendas", ascending=False
).head(10)

st.dataframe(
    top_produtos[[
        "produto",
        "categoria",
        "tipo_produto",
        "preco_desconto",
        "avaliacao",
        "valor_total_vendas"
    ]]
)

# =========================
# RANKING COMPLETO
# =========================
st.subheader(" Ranking Geral Completo")

st.dataframe(
    resumo.sort_values(by="score_final", ascending=False)
)

# =========================
# TABELA DETALHADA
# =========================
with st.expander(" Ver dados detalhados"):
    st.dataframe(df_filtrado)

