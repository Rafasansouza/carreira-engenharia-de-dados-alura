class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria: {self.categoria} | Status: {self.ativo}'
    
    def listar_restaurantes():
        print(f'{'Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
restaurante_praca = Restaurante('Praça', 'Comida Caseira')
Restaurante.listar_restaurantes()