def ficha(nome='<desconhecido>', gols=' '):
    if nome.isalpha() == False:
        nome = '<desconhecido>'
    if gols.isnumeric() == False:
        gols = 0
    else:
        gols = int(gols)
    print(f'o jogador {nome} fez {gols} gol(s) no campeonato.')


a = str(input('Nome do jogador: '))
b = str(input('Número de gols: '))
ficha(a, b)
