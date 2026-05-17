import streamlit as st
import pandas as pd
import numpy as np
from src.tratamento import carregar_e_tratar

st.set_page_config(layout="wide")

st.title(" Dashboard - Análise de Mercado Amazon ")


# CARREGAR DADOS

df = carregar_e_tratar()


# FILTROS

st.sidebar.header(" Filtros")

categorias = st.sidebar.multiselect(
    "Categoria",
    options=sorted(df["categoria"].unique()),
    default=sorted(df["categoria"].unique()),
)

tipos = st.sidebar.multiselect(
    "Tipo de Produto",
    options=sorted(df["tipo_produto"].unique()),
    default=sorted(df["tipo_produto"].unique()),
)

df_filtrado = df[(df["categoria"].isin(categorias)) & (df["tipo_produto"].isin(tipos))]


# AGRUPAMENTO

resumo = (
    df_filtrado.groupby("categoria")
    .agg(
        {
            "avaliacao": "mean",
            "qtd_avaliacoes": "sum",
            "codigo": "count",
            "valor_total_vendas": "sum",
            "preco_desconto": "mean",
        }
    )
    .reset_index()
)

resumo = resumo.rename(
    columns={
        "avaliacao": "rating_medio",
        "qtd_avaliacoes": "total_avaliacoes",
        "codigo": "total_produtos",
        "preco_desconto": "ticket_medio",
    }
)


# SCORE DAS CATEGORIAS

# média geral das avaliações
C = df_filtrado["avaliacao"].mean()

# quantidade mínima de avaliações considerada relevante
m = resumo["total_avaliacoes"].quantile(0.75)

# cálculo do score bayesiano
resumo["score_bayesiano"] = (
    resumo["total_avaliacoes"] / (resumo["total_avaliacoes"] + m)
) * resumo["rating_medio"] + (m / (resumo["total_avaliacoes"] + m)) * C

# score final
resumo["score_final"] = (
    0.5 * resumo["score_bayesiano"]
    + 0.3 * np.log1p(resumo["total_avaliacoes"])
    + 0.2 * np.log1p(resumo["valor_total_vendas"])
)


# MÉTRICAS GERAIS

st.subheader(" Visão Geral")

col1, col2, col3, col4 = st.columns(4)

col1.metric(" Produtos", df_filtrado.shape[0])
col2.metric(" Avaliações", int(df_filtrado["qtd_avaliacoes"].sum()))
col3.metric(" Categorias", df_filtrado["categoria"].nunique())

valor = df_filtrado["preco_desconto"].mean()

valor_formatado = (
    f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)

col4.metric("Ticket Médio", valor_formatado)


# COMENTÁRIOS GERAIS

st.subheader(" Observações da Análise")

top_categoria = resumo.sort_values(
    by="score_final",
    ascending=False
).iloc[0]

top_receita = resumo.sort_values(
    by="valor_total_vendas",
    ascending=False
).iloc[0]

top_avaliacao = resumo.sort_values(
    by="rating_medio",
    ascending=False
).iloc[0]

top_popularidade = resumo.sort_values(
    by="total_avaliacoes",
    ascending=False
).iloc[0]


st.write(
    f"A categoria com melhor desempenho geral foi "
    f"**{top_categoria['categoria']}**, considerando "
    "avaliação, popularidade e vendas."
)

st.write(
    f"A categoria **{top_receita['categoria']}** apresentou "
    "o maior valor estimado de vendas dentro da base analisada."
)

st.write(
    f"A categoria **{top_avaliacao['categoria']}** apresentou "
    f"a maior média de avaliações ({top_avaliacao['rating_medio']:.2f})."
)

st.write(
    f"A categoria **{top_popularidade['categoria']}** concentrou "
    "o maior número de avaliações dos usuários."
)

st.write(
    "De forma geral, categorias com maior quantidade de avaliações "
    "também apresentaram maior volume estimado de vendas."
)

# RANKING DE CATEGORIAS

st.subheader(" Ranking de Categorias - Top 5")

top = resumo.sort_values(by="score_final", ascending=False)

st.dataframe(top.head(5))


# GRÁFICOS PRINCIPAIS

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


# RELAÇÃO ENTRE DADOS

st.subheader(" Avaliação vs Popularidade")

st.scatter_chart(df_filtrado, x="qtd_avaliacoes", y="avaliacao")

st.subheader(" Desconto vs Avaliação")

st.scatter_chart(df_filtrado, x="perc_desconto", y="avaliacao")


# RECEITA POR CATEGORIA

st.subheader(" Receita Estimada por Categoria")

st.bar_chart(resumo.set_index("categoria")["valor_total_vendas"])


# TOP PRODUTOS

st.subheader(" Top Produtos")

top_produtos = df_filtrado.sort_values(by="valor_total_vendas", ascending=False).head(
    10
)

st.dataframe(
    top_produtos[
        [
            "produto",
            "categoria",
            "tipo_produto",
            "preco_desconto",
            "avaliacao",
            "valor_total_vendas",
        ]
    ]
)


# RANKING COMPLETO

st.subheader(" Ranking Geral Completo")

st.dataframe(resumo.sort_values(by="score_final", ascending=False))

# DADOS DETALHADOS

with st.expander(" Ver dados detalhados"):
    st.dataframe(df_filtrado)

