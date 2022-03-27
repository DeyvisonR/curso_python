print('-=-' * 20)
print(f'{"aproveitamento de um jogador de fotebol":^60}')
print('-=-' * 20)
dicionario = {}
listadegols = []
somadegols = 0
dicionario['nome'] = str(input('nome do jogador: '))
partidas = int(input(f'quantas partidas o {dicionario["nome"]} jogou: '))
for c in range(0, partidas):
    gols = int(input(f'você fez quantos gols na partida {c + 1}: '))
    listadegols.append(gols)
    somadegols = somadegols + gols
dicionario['gols'] = listadegols
dicionario['total'] = somadegols
print('-=-' * 20)
print(dicionario)
print('-=-' * 20)
for k, v in dicionario.items():
    print(f'o campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'o jogador {dicionario["nome"]} jogou {partidas} partidas')
for i, v in enumerate(listadegols):
    print(f'  =>  na partida {i + 1}, fez {v} gols')
print(f'foi um total de {dicionario["total"]} gols')
