class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo=False): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

Restaurante.listar_restaurantes()
