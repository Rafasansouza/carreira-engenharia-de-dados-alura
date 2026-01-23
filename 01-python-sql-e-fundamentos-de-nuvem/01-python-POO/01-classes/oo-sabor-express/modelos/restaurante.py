class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Comida Caseira'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

#exercicio 1
restaurante_praca.categoria = 'Italiana'
print(vars(restaurante_praca))