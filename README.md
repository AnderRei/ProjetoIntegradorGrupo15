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
  Para a realização desta análise será utilizada uma base de dados contendo informações de mais de 1.000 produtos disponíveis na plataforma da Amazon. A escolha dessa base se justifica pela relevância da empresa no cenário global de comércio eletrônico, além da variedade e riqueza de dados disponíveis para análise. O conjunto de dados disponível neste banco de dados reúne informações detalhadas sobre produtos e a interação dos usuários com eles. Entre os principais atributos presentes na base, destacam-se: identificação e nome do produto, categoria, preço original e com desconto, percentual de desconto, avaliação média (rating), quantidade de avaliações (rating_count), além de descrições dos produtos e conteúdos de reviews feitos por usuários. O objetivo principal da análise é identificar quais setores (categorias de produtos) apresentam maior potencial de crescimento, com maior popularidade, volume e qualidade de avaliações. Para isso, serão consideradas variáveis como volume de avaliações, notas atribuídas e características dos produtos, buscando gerar insights relevantes sobre o mercado. Além disso, o trabalho tem como propósito aplicar conceitos fundamentais da área de Ciência de Dados, incluindo limpeza e organização dos dados, análise exploratória e interpretação dos resultados. Com isso, pretende-se demonstrar como a análise de dados pode ser utilizada como ferramenta estratégica para compreensão de tendências e apoio à tomada de decisão.

## Problemas encontrados

- Preços estão como texto com símbolo de moeda (₹)
- preços estão em rupias indianas
- rating_count contém vírgulas
- discount_percentage está como texto (%)
- category contém múltiplos níveis (separados por |)
- Muitas colunas não relevantes (reviews, links, etc.)

## Tratamentos

- Converter preços para float e retirar simbolo
- converter preços para moeda local 
- Converter rating_count para inteiro
- Converter discount_percentage para float e retirar simbolo
- Remover linhas com Nulos
- Remover colunas irrelevantes

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

## Dashboard Interativo
  Foi desenvolvido um dashboard interativo utilizando a biblioteca Streamlit com o objetivo de apresentar, de forma visual e analítica, os principais insights obtidos na análise dos dados da Amazon.

  A aplicação permite visualização dinâmica das informações, facilitando a interpretação dos resultados, identificação de padrões e apoio à tomada de decisão baseada em dados.
  
<img width="1508" height="673" alt="image" src="https://github.com/user-attachments/assets/41128230-65f1-4067-a3ef-11ff6588404a" />


### Filtro Interativos
  Foram implementados filtros interativos utilizando componentes nativos do Streamlit.

  O usuário pode filtrar os dados por:
     - Categoria de produto
     - Tipo de produto
  Essa funcionalidade permite explorar diferentes cenários, analisar segmentos específicos e compreender melhor o comportamento de cada grupo de produtos.

### Métricas Gerais
  Foram criadas métricas principais para fornecer uma visão geral do dataset:
    - Total de produtos analisados
    - Total de avaliações
    - Número de categorias
    - Ticket médio dos produtos
  Os valores monetários foram convertidos de Rúpia Indiana (INR) para Real Brasileiro (BRL), garantindo maior aderência ao contexto de análise.
  Essas métricas permitem rápida compreensão sobre volume, relevância e impacto financeiro dos dados.

### Agrupamento de Dados
  Os dados foram agrupados por categoria utilizando funções de agregação para calcular:
    - Média das avaliações (qualidade)
    - Soma da quantidade de avaliações (popularidade)
    - Quantidade total de produtos por categoria
    - Soma do valor total estimado de vendas
    - Ticket médio por categoria
Essa etapa permite comparação consistente entre diferentes categorias de produtos.

### Score Inteligente (Modelo Bayesiano)
 Foi implementado um modelo de pontuação baseado em abordagem bayesiana para ranquear categorias com maior robustez analítica.
  O score considera:
    - Qualidade (média das avaliações)
    - Popularidade (volume de avaliações)
    - Média global do dataset
  Esse modelo reduz distorções geradas por categorias com poucas avaliações e melhora a confiabilidade do ranking.
  Além disso, foi criado um score final composto por:
    - Score bayesiano
    - Volume de avaliações (escala logarítmica)
    - Valor total estimado de vendas (escala logarítmica)
  Essa abordagem proporciona análise mais equilibrada e orientada ao negócio.

### Ranking de Categoria
  Foi desenvolvido um ranking de categorias com base no score final.
  Esse ranking permite identificar rapidamente quais setores apresentam maior relevância, qualidade e potencial de mercado dentro da base analisada.

### Visualizações Gráficas
  Foram implementadas visualizações para facilitar análise exploratória e interpretação dos dados:
    - Gráfico de barras de popularidade por categoria
    - Gráfico de barras de avaliação média por categoria
    - Gráfico de barras de receita estimada por categoria
  Gráficos de dispersão:
    - Avaliação vs Popularidade
    - Desconto vs Avaliação
  Essas visualizações permitem identificar relações, padrões e oportunidades de mercado de forma intuitiva.

### Análise de Produtos
  O dashboard também apresenta análise individual de produtos, incluindo:
    - Ranking dos produtos com maior valor estimado de vendas
    - Categoria
    - Tipo de produto
    - Preço com desconto
    - Avaliação
  Essa análise permite visão mais granular além do agrupamento por categorias.

### Interação com Tratamento de Dados
  O dashboard foi desenvolvido de forma integrada com a etapa de tratamento e preparação dos dados (ETL).
  As colunas geradas durante o processo são utilizadas diretamente nas análises, incluindo:
    - tipo_produto
    - valor_total_vendas
    - preco_desconto
    - perc_desconto
  Além disso, foi realizada conversão monetária para garantir consistência analítica e adequação ao contexto brasileiro.
  Essa integração garante coerência entre as etapas do projeto e maior confiabilidade nos resultados.

### Viabilidade Técnica e Econômica

O projeto apresenta **alta viabilidade econômica**, uma vez que foi idealizado e desenvolvido integralmente com o uso de tecnologias de código aberto (*open source*) e plataformas gratuitas. A linguagem Python, juntamente com as bibliotecas nativas e externas (como Pandas e Streamlit), não exige custos de licenciamento. Além disso, o controle de versão e armazenamento do código são realizados gratuitamente via GitHub, e o *deploy* da aplicação pode ser hospedado na camada gratuita do Streamlit Community Cloud. Portanto, o custo operacional e de infraestrutura do projeto é zero.

Em relação à **viabilidade técnica**, o projeto é plenamente executável dentro do escopo estabelecido. A base de dados selecionada no Kaggle é estruturada, rica em atributos e adequada para o volume de processamento pretendido. A equipe detém os conhecimentos fundamentais adquiridos nas disciplinas de Práticas de Programação, Banco de Dados e Introdução à Ciência de Dados, o que garante a capacidade técnica para realizar os processos de extração, transformação e carga (ETL), bem como o desenvolvimento da interface interativa *low code* dentro do cronograma estipulado.

# Como Executar o Projeto


## 1. Clonar o repositório

Clone o projeto para sua máquina e acesse a pasta:

```bash
git clone https://github.com/AnderRei/ProjetoIntegradorGrupo15.git
cd ProjetoIntegradorGrupo15-main
```

---

## 2. Criar o ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

---

## 3. Ativar o ambiente virtual

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
venv\Scripts\activate.bat
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 4. Instalar as dependências

Instale todas as bibliotecas necessárias utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 5. Executar o tratamento de dados (Opcional)

Caso seja necessário gerar novamente a base de dados tratada:

```bash
python src/tratamento.py
```

---

## 6. Executar o dashboard

Para iniciar o dashboard interativo no navegador:

```bash
streamlit run app.py
```

O Streamlit exibirá no terminal um endereço semelhante a:

```text
http://localhost:8501
```

Após executar o comando, o projeto será aberto automaticamente no navegador padrão.

---

# Observações

- O projeto utiliza a biblioteca `Streamlit` para criação do dashboard interativo.
- O comando correto para iniciar a aplicação é:

```bash
streamlit run app.py
```

- Não é recomendado executar o arquivo diretamente com:

```bash
python app.py
```

pois aplicações Streamlit precisam ser iniciadas pelo servidor do framework, e executar o arquivo diretamente pode causar erros de funcionamento.


## Solução Publicada e Execução do Projeto

Para atender aos requisitos de desenvolvimento e validação da aplicação *low code*, o painel interativo foi publicado em nuvem, permitindo o acesso de qualquer dispositivo sem a necessidade de configurações locais.

link da solução publicada: https://projetointegradorgrupo15.streamlit.app/
