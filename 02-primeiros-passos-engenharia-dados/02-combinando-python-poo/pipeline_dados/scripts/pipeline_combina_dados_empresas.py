from processamento_dados import Dados

# Extract

dados_empresaA = Dados('data_raw/dados_empresaA.json', 'json')
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

dados_empresaB = Dados('data_raw/dados_empresaB.csv', 'csv')
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

# Transform

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Valor do Produto',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.renomear_colunas(key_mapping)
print(dados_empresaB.nome_colunas)

dados_combinados = Dados.join_data(dados_empresaA, dados_empresaB)
print(dados_combinados.nome_colunas)
print(dados_combinados.qtd_linhas)

# Load 

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_combinados.salvando_dados(path_dados_combinados)