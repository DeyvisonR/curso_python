cont = 0
from random import randint
print('-=-' * 18)
print(f'{"vou pensar em um número entre 0 e 10. TENTE ADIVINHAR":^40}')
print('-=-' * 18)
computador = randint(0, 10)
jogador = int(input('em que número eu pensei: '))
if computador == jogador:
    print(f'\033[32mvocê acertou de primeira. eu pensei no número {computador}\033[m')
else:
    while computador != jogador:
        if computador > jogador:
            a = 'maior'
        else:
            a = 'menor'
        print(f'você errou eu pensei em um numero {a}. tente novamente')
        jogador = int(input('qual seu palpite: '))
        cont = cont + 1
print(f'\033[32mparabense você acertou eu pensei no número {computador} e você precisou de {cont + 1} tentativas\033[m')
