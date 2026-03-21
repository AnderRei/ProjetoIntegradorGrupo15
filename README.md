## Projeto Integrador
  Desenvolvimento low code em ciência de dados

## Tema do projeto
  Análise de mercado sobre vendas de produtos da Amazon
  
## Integrantes
  - ANDERSON REICHARDT
  - GUSTAVO DAVI PACHECO DA MATA
  - LEONARDO GONCALVES NEIVA
  - ZECY DE CASTRO ALVES SALGADO JUNIOR

## Planejamento das tarefas

| Tarefa | Responsável | Cronograma |
|--------|------------|-----------|
| Criação do repositório no GitHub | Anderson Reichardt | 06/03/2026 |
| Definição da base de dados | Todos | 08/03/2026 |
| Contextualização da base de dados | Zecy de Castro Alves Salgado Junior | 12/03/2026 |
| Planejamento do projeto de ETL | Leonardo Gonçalves Neiva | 16/03/2026 |
| Planejamento do Dashboard | Gustavo Davi Pacheco da Mata | 20/03/2026 |
| Organização do README | Anderson Reichardt | 21/03/2026 |
| Revisão geral do trabalho | Todos | 22/03/2026 |
| Entrega da primeira etapa | Anderson Reichardt | 23/03/2026 |

## Tecnologias utilizadas
  - Python
  - pandas
  - Streamlit

## Base de dados escolhida
https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset/data

## Objetivo da análise
  Para a realização desta análise será utilizada uma base de dados contendo informações de mais de 1.000 produtos disponíveis na plataforma da Amazon. A escolha dessa base se justifica pela relevância da empresa no cenário global de comércio eletrônico, além da variedade e riqueza de dados disponíveis para análise. O conjunto de dados disponível neste banco de dados reúne informações detalhadas sobre produtos e a interação dos usuários com eles. Entre os principais atributos presentes na base, destacam-se: identificação e nome do produto, categoria, preço original e com desconto, percentual de desconto, avaliação média (rating), quantidade de avaliações (rating_count), além de descrições dos produtos e conteúdos de reviews feitos por usuários. O objetivo principal da análise é identificar quais setores (categorias de produtos) apresentam maior crescimento e melhor desempenho dentro da plataforma. Para isso, serão consideradas variáveis como volume de avaliações, notas atribuídas e características dos produtos, buscando gerar insights relevantes sobre o mercado. Além disso, o trabalho tem como propósito aplicar conceitos fundamentais da área de Ciência de Dados, incluindo limpeza e organização dos dados, análise exploratória e interpretação dos resultados. Com isso, pretende-se demonstrar como a análise de dados pode ser utilizada como ferramenta estratégica para compreensão de tendências e apoio à tomada de decisão.

## Planejamento do projeto de ETL
  O planejamento do processo de ETL, Extract, Transform e Load, Extração, Transformação e Carregamento, será estruturado para garantir a qualidade e organização dos dados utilizados na análise.
  Na Extração, os dados serão coletados a partir da base do Kaggle, sendo a importação do arquivo CSV para o ambiente Python e a leitura dos dados será utilizado a biblioteca pandas.
  Quanto a transformação, os dados serão tratados e preparados para análise, sendo as principais operações realizadas listadas a seguir: 
  1 – Remoção de valores nulos;
  2 – Tratamento de dados inconsistentes;
  3 – conversão de tipos de dados, exemplo, texto para numérico;
  4 – Padronização de colunas;
  5 – Criação de novas métricas, exemplo, média de avaliação por categoria;
  6 – Filtragem de dados relevantes;
  7 – Agrupamento por categorias de produtos.
  No Carregamento, será executado a exploração dos dados tratados para arquivos CSV e preparação dos dados para uso em ferramentas de visualização.
  A seguir apresento como será  o fluxo do ETL :
  Kaggle -> Extração -> Transformação (pandas) -> Dados tratados -> Dashboard

## Ideia inicial do dashboard
  O dashboard será planejado a partir de um banco de dados da Amazon que reúne informações básicas dos produtos, como código, nome, categoria, preços, quantidade do produto em estoque, percentual de desconto e avaliação dos clientes. A proposta do dashboard é organizar esses dados de forma simples e clara, facilitando a visualização e a comparação entre os produtos disponíveis. As métricas utilizadas serão compatíveis com as informações da base, incluindo o total de produtos analisados, o preço médio normal, o preço médio com desconto, a quantidade total de produtos em estoque, o desconto médio aplicado e a avaliação média dos consumidores, que serão apresentados como indicadores para oferecer uma visão geral dos dados. Para a parte visual, serão utilizados gráficos de barras para comparar as categorias em relação à quantidade de produtos, preços médios, descontos e avaliações dos clientes, além de um gráfico de pizza para mostrar a distribuição dos produtos por categoria e um gráfico de dispersão para observar a relação entre o preço com desconto e a avaliação do cliente. O dashboard terá interatividade, permitindo que o usuário aplique filtros e altere as visualizações, fazendo com que gráficos e indicadores se atualizem automaticamente conforme as escolhas realizadas, tornando a análise mais dinâmica e facilitando o entendimento das informações apresentadas.
