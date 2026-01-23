class Restaurante:
    def __init__(self, nome, categoria, ativo=False): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'

restaurante_praca = Restaurante('Praça', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

print(restaurante_praca)
print(restaurante_pizza)
