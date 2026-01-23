class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self._nome} | Categoria: {self._categoria} | Status: {self.ativo}'
    
    def listar_restaurantes():
        print(f'{'Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
restaurante_praca = Restaurante('praça', 'pomida Caseira')
Restaurante.listar_restaurantes()