from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Restaurante da Praça', 'Comida Caseira')
restaurante_mar = Restaurante('Restaurante do Mar', 'Frutos do Mar')
restaurante_mexicano = Restaurante('Restaurante Mexicano', 'Comida Mexicana')

restaurante_mar.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()