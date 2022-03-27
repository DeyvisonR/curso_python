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
if jogada == n:
    print('EMPATE')
elif jogada == 1 and n == 2:
    print('COMPUTADOR VENCEU')
elif jogada == 1 and n == 3:
    print('JOGADOR VENCEU')
elif jogada == 2 and n == 1:
    print('JOGADOR VENCEU')
elif jogada == 2 and n == 3:
    print('COMPUTADOR VENCEU')
elif jogada == 3 and n == 1:
    print('COMPUTADOR VENCEU')
elif jogada == 3 and n == 2:
    print('JOGADOR VENCEU')
