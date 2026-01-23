class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    def __str__(self):
        return f'Música: {self.nome} | Artista: {self.artista} | Duração: {self.duracao} segundos'
    
musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

print(musica1)
print(musica2)
print(musica3)