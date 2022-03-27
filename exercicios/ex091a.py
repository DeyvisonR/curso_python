from random import randint
from time import sleep
lista = []
listadosnum = []
lista.append(['jogador 1', randint(1, 6), 'jogador 2', randint(1, 6),
              'jogador 3', randint(1, 6), 'jogador 4', randint(1, 6)])
listadosnum.append(lista[0][1])
listadosnum.append(lista[0][3])
listadosnum.append(lista[0][5])
listadosnum.append(lista[0][7])
listadosnum.sort(reverse=True)
print('Valores sorteados:')
for c in range(0, 8, 2):
    print(f'{lista[0][c]} tirou {lista[0][c + 1]}')
    sleep(1)
print('RANKING DOS JOGADORES:')
cont = 0
while cont < 4:
    for c in range(1, len(lista[0]), 2):
        if cont == 4:
            break
        if lista[0][c] == listadosnum[cont]:
            print(f'  -  {cont + 1} lugar: {lista[0][c - 1]} com {lista[0][c]}')
            sleep(1)
            cont = cont + 1
