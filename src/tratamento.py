import pandas as pd
#abaixo carregamos o arquivo original para tratamento 
def carregar_e_tratar():
    df = pd.read_csv("data/amazonOriginal.csv")


   #abaixo selecionamos somente as colunas que iremos usar para tratamento e criação do dashboard   
    df = df [
        ["product_id", "product_name", "category", 
             "discounted_price", "discount_percentage", 
             "rating", "rating_count",]
    ]

    #abaixo traduzimos do termo tecnico para linguagem comercial para fins de montagem do dashboard   
    df.columns = [
    "codigo",
    "produto",
    "categoria",
    "preco_desconto",
    "perc_desconto",
    "avaliacao",
    "qtd_avaliacoes"
      ]

    # converter avaliação para número, tratando erros

    df["avaliacao"] = pd.to_numeric(df["avaliacao"], errors="coerce")

    # remover símbolo de moeda e separador de milhar
    
    df["preco_desconto"] = df["preco_desconto"] \
    .str.replace("₹", "") \
    .str.replace(",", "") \
    .astype(float)
   
    # remover símbolo de porcentagem
    df["perc_desconto"] = df["perc_desconto"] \
    .str.replace("%", "") \
    .astype(float)

    # remover vírgula da quantidade de avaliações
    df["qtd_avaliacoes"] = df["qtd_avaliacoes"] \
    .str.replace(",", "") \
    .astype(float)

    # pegar só a categoria principal
    df["categoria"] = df["categoria"].str.split("|").str[0]

    # deixar mais legível
    df["categoria"] = df["categoria"].str.replace("&", " e ")

    # criar coluna de valor total de vendas (estimativa baseada no preço com desconto e quantidade de avaliações)

    df["valor_total_vendas"] = df["preco_desconto"] * df["qtd_avaliacoes"]


    # classificar tipo de produto
    
    # classificar tipo de produto (completo e sem sobrescrever)
    

    df["tipo_produto"] = "outros"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Cable|Cabo|Braided|Type-C|Lightning", case=False, na=False), "tipo_produto"] = "cabo"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Headphone|Earphone|Headset|Earbuds", case=False, na=False), "tipo_produto"] = "fone"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Speaker|Soundbar", case=False, na=False), "tipo_produto"] = "caixa de som"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Mouse|Keyboard|Webcam", case=False, na=False), "tipo_produto"] = "periferico"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Bag|Case|Cover|Pouch", case=False, na=False), "tipo_produto"] = "bolsa/acessorio"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("TV|Television|Smart TV", case=False, na=False), "tipo_produto"] = "tv"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Phone|Smartphone|Mobile|iPhone|Android", case=False, na=False), "tipo_produto"] = "celular"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Controller|Gamepad|Joystick", case=False, na=False), "tipo_produto"] = "controle"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Laptop|Computer|PC|Notebook", case=False, na=False), "tipo_produto"] = "computador"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Router|WiFi|Adapter|Modem", case=False, na=False), "tipo_produto"] = "rede"

    df.loc[(df["tipo_produto"] == "outros") & df["produto"].str.contains("Charger|Charging|Adapter", case=False, na=False), "tipo_produto"] = "carregador"



    # limpar texto
    df["produto"] = df["produto"].str.replace("&", " e ", regex=False)

    # padronizar (primeira letra maiúscula)
    df["produto"] = df["produto"].str.title()

    # 🔥 corrigir siglas depois
    df["produto"] = df["produto"].str.replace("Usb", "USB")
    df["produto"] = df["produto"].str.replace("Iphone", "iPhone")

    # remover espaços duplicados
    df["produto"] = df["produto"].str.replace(r"\s+", " ", regex=True).str.strip()

    # criar versão curta
    df["produto_curto"] = df["produto"].str[:50]
    
    


    # 📌 organizar colunas
    df = df[
        [
            "produto",
            "codigo",
            "categoria",
            "tipo_produto",
            "preco_desconto",
            "perc_desconto",
            "avaliacao",
            "qtd_avaliacoes",
            "valor_total_vendas"
        ]
    ]
    df["tipo_produto"] = df["tipo_produto"].str.title()
    
    print(list(df.columns))
    print(df.dtypes)
    print(df.head())
    print(df["categoria"].head())
    print(df["categoria"].unique())
    print(df["produto"].str.contains("USB|Charging|Cable", case=False).sum())
    print(df.columns)
    print(df["tipo_produto"].value_counts())
    print(df[["produto", "tipo_produto"]].head(10))



    #df.columns = df.columns.str.upper()
    df.columns = df.columns.str.lower()




    df.to_csv("data/amazon_tratado.csv", index=False)



    return df
    

if __name__ == "__main__":
    carregar_e_tratar()
