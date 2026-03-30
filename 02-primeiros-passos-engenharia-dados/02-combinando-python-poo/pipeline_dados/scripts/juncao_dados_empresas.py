
import json
import csv

def carregar_dados_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    
    return dados_json

def carregar_dados_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados_csv.append(row)
    
    return dados_csv

def carregar_dados(path, tipo_arquivo):
    if tipo_arquivo == 'json':
        dados = carregar_dados_json(path)
    
    elif tipo_arquivo == 'csv':
        dados = carregar_dados_csv(path)
    
    else:
        raise ValueError("Tipo de arquivo não suportado. Use 'json' ou 'csv'.")
    
    return dados

def get_columns(dados):
    return list(dados[0].keys())

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        new_dict_temp = {}
        for old_key, new_key in old_dict.items():
            new_dict_temp[key_mapping[old_key]] = new_key
        new_dados_csv.append(new_dict_temp)
    return new_dados_csv

def size_data(dados):
    return len(dados)

def join_data(dados_A, dados_B):
    combined_list = []
    combined_list.extend(dados_A)
    combined_list.extend(dados_B)
    return combined_list

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
    
dados_json = carregar_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
print(f"nome_colunas_json: {nome_colunas_json}")

dados_csv = carregar_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
print(f"nome_colunas_csv: {nome_colunas_csv}")

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Valor do Produto',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f"nome_colunas_csv_renomeadas: {nome_colunas_csv}")

dados_join = join_data(dados_json, dados_csv)
tamanho_join = size_data(dados_join)
print(tamanho_join)