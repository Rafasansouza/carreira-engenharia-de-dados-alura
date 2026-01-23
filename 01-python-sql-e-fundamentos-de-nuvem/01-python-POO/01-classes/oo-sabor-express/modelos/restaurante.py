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

#exercicio 2
print(restaurante_praca.nome)

#exercicio 3
if restaurante_pizza.ativo:
    print(f'O restaurante {restaurante_pizza.nome} está ativo') 
else:
    print(f'O restaurante {restaurante_pizza.nome} está inativo')
