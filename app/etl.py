import pandas as pd

bd = pd.read_csv('data/amazonOriginal.csv')

#limpa as colunas que serão deletadas do banco de dados, about_product, user_id ,user_name, review_id .review_title, review_content, img_link, product_link
bd.drop(['about_product', 'user_id', 'user_name', 'review_id', 'review_title', 'review_content', 'img_link', 'product_link'], axis=1, inplace=True)
#lista as colunas do banco de dados
print(bd.columns)
#remove o simbolo ₹ da coluna actual_price 
bd['actual_price'] = bd['actual_price'].str.replace('₹', '')
#remove o simbolo ₹ da coluna discount_price
bd['discounted_price'] = bd['discounted_price'].str.replace('₹', '')
#transforma as colunas em numéricas
bd["discounted_price"] = pd.to_numeric(bd["discounted_price"], errors='coerce')
bd["actual_price"] = pd.to_numeric(bd["actual_price"], errors='coerce')