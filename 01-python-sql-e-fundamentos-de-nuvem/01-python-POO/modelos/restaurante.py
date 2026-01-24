from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self._nome} | Categoria: {self._categoria} | Status: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def adicionar_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtde_notas = len(self._avaliacao)
        media_notas = round(soma_notas / qtde_notas, 1)
        return media_notas