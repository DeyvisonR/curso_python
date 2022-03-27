import random
import time
items = ('pedra', 'papel', 'tesoura')
n = random.randint(1, 3)
print('-=' * 20)
print(f'{"JOKENPO":=^40}')
print('-=' * 20)
print('''suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada = int(input('qual e a sua jogada: '))
while jogada >= 4:
    print('jogada invalida. tente novamente')
    jogada = int(input('qual e a sua jogada: '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=-' * 10)
print(f'''COMPUTADOR jogou {items[n - 1]}
JOGADOR jogou {items[jogada - 1]}''')
print('-=-' * 10)
win = 'COMPUTADOR VENCEU'
if jogada == n:
    win = 'EMPATE'
elif jogada == 1 and n == 3:
    win = 'JOGADOR VENCEU'
elif jogada == 2 and n == 1:
    win = 'JOGADOR VENCEU'
elif jogada == 3 and n == 2:
    win = 'JOGADOR VENCEU'
print(win)
