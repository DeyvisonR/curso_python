import random
from time import sleep
print('\033[33m-=-' * 20)
print('\033[34mvou pensar em um número entre 0 e 5. tente adivinhar...')
print('\033[33m-=-\033[m' * 20)
npc = random.randint(1, 5) # faz o computador pensar de um número de 1 a 5
n = int(input('em que número eu pensei?: ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if n == npc: # testa se o jogador ganhou
    print('\033[32mparabens você ganhou, eu pensei no número {}'.format(npc))
else: # se ele perdeu
    print('\033[31mganhei! eu pensei no número {} e não no {}!'.format(npc, n))
