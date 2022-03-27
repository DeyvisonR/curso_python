from random import randint
from time import sleep
from operator import itemgetter
dicionario = {}
dicionario['jogador 1'] = randint(1, 6)
dicionario['jogador 2'] = randint(1, 6)
dicionario['jogador 3'] = randint(1, 6)
dicionario['jogador 4'] = randint(1, 6)
print('Valores sorteados:')
for k, v in dicionario.items():
    sleep(1)
    print(f'o {k} tirou {v}')
print('RANKING DOS JOGADORES:')
ranking = {}
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for p, v in enumerate(ranking):
    print(f'{p + 1} lugar: {v[0]} com {v[1]}')
    sleep(1)
