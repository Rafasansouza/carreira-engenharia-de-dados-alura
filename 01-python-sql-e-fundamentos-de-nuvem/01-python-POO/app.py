from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Restaurante da Praça', 'Comida Caseira')
restaurante_praca.adicionar_avaliacao('Alice', 5)
restaurante_praca.adicionar_avaliacao('Bob', 4)
restaurante_praca.adicionar_avaliacao('Charlie', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()