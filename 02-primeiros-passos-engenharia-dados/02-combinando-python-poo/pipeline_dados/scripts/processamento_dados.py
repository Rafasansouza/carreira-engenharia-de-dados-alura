import json
import csv

class Dados:

    def __init__(self, path, tipo_arquivo, ):
        self.path = path
        self.tipo_arquivo = tipo_arquivo
        self.dados = self.carregar_dados()
        self.nome_colunas = self.consultar_colunas()
        self.qtd_linhas = self.size_data()
    
    def carregar_dados_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        
        return dados_json

    def carregar_dados_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dados_csv.append(row)
        
        return dados_csv

    def carregar_dados(self):
        if self.tipo_arquivo == 'json':
            dados = self.carregar_dados_json()
        
        elif self.tipo_arquivo == 'csv':
            dados = self.carregar_dados_csv()
        
        elif self.tipo_arquivo == 'list':
            dados = self.path
            self.path = 'lista em memória'
        
        else:
            raise ValueError("Tipo de arquivo não suportado. Use 'json' ou 'csv'.")
        
        return dados

    def consultar_colunas(self):
        return list(self.dados[-1].keys())
    
    def renomear_colunas(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            new_dict_temp = {}
            for old_key, new_key in old_dict.items():
                new_dict_temp[key_mapping[old_key]] = new_key
            new_dados.append(new_dict_temp)
        
        self.dados = new_dados
        self.nome_colunas = self.consultar_colunas()

    def size_data(self):
        return len(self.dados)
    
    def join_data(dados_A, dados_B):
        combined_list = []
        combined_list.extend(dados_A.dados)
        combined_list.extend(dados_B.dados)
        
        return Dados(combined_list, 'list')
    
    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def salvando_dados(self, path):
        dados_combinados_tabela = self.transformando_dados_tabela()
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
        print(f"Dados combinados salvos em {path}")