class Restaurante:
    def __init__(self, nome, categoria, ativo=False): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

restaurante_praca = Restaurante('Praça', 'Comida Caseira')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

print(vars(restaurante_praca))
print(vars(restaurante_pizza))