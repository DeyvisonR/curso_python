from time import sleep
from random import randint
print('=' * 50)
print(f'{"JOGUE NA MEGA SENA":^50}')
print('=' * 50)
jogos = []
jogosqt = int(input('quantos jogos você quer que eu sorteie: '))
print(f'{f"   sorteando {jogosqt} jogos   ":=^50}')
cont = 0
cont2 = 0
sorteados = []
while cont2 < jogosqt:
    while cont < 6:
        num = randint(1, 60)
        if num not in sorteados:
            sorteados.append(num)
            cont = cont + 1
    if cont == 6:
        jogos.append(sorteados[:])
        sorteados.clear()
        cont = 0
        cont2 = cont2 + 1
for c in range(0, len(jogos)):
    jogos[c].sort()
    print(f'jogo {c + 1}: {jogos[c]}')
    sleep(1)
print('=' * 10, 'FIM DO PROGRAMA', '=' * 10)
