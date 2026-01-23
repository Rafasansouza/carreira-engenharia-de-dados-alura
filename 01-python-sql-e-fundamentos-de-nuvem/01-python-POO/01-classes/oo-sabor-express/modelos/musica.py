class musica:
    nome = ''
    banda = ''
    duracao = float(0)

musica_1 = musica()
musica_1.nome = 'Enter Sandman'
musica_1.banda = 'Metallica'
musica_1.duracao = 5.31

musica_2 = musica()
musica_2.nome = 'Nothing Else Matters'
musica_2.banda = 'Metallica'
musica_2.duracao = 6.28

musica_3 = musica()
musica_3.nome = 'The Unforgiven'
musica_3.banda = 'Metallica'
musica_3.duracao = 6.27

musicas = [musica_1, musica_2, musica_3]
print(vars(musica_1))
