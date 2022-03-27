# JOKENPO COM SPOCK E LARGATO
cores = {'branco': '\033[30m', # pegando todas as cores pra não ter trabalho depois
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'azulmarinho': '\033[36m',
         'cinza': '\033[37m',
         'fechar': '\033[m'}
from random import randint # importando a escolha do computador
from time import sleep # importando o time do JO KEN PO
items = ('pedra', 'papel', 'tesoura', 'largato', 'spock') # DEFININDO OS ITEMS
a = 'True' # definindo a como True
b = 'True'
print('-=' * 25)
print(f'{" JOKENPO ":=^50}')  # TITULO
print('-=' * 25)

while a == 'True':
    pergunta = str(input('você quer saber como o jogo funciona (S/N): ')).lower().strip()
    if pergunta[0] == 's':
        a = 'False'  # se a resposta for 's' o if vai definir o while para falso parando assim a repetição
        print('-=' * 33)
        print(f'''{cores['amarelo']}O jogo de pedra, papel, tesoura, lagarto e spock funciona assim:
Tesoura corta papel 
Papel cobre pedra 
Pedra esmaga lagarto 
Lagarto envenena Spock 
Spock esmaga (ou derrete) tesoura
Tesoura decapita lagarto 
Lagarto come papel 
Papel refuta Spock 
Spock vaporiza pedra 
Pedra quebra tesoura
O COMPUTADOR VAI JOGAR UM DESSES. TENTE JOGAR UM QUE GANHE O OUTRO{cores['fechar']}''')
        print('-=' * 33)
    elif pergunta[0] == 'n':  # se a resposta for 'n' o if vai definir o while para falso parando assim a repetição
        a = 'False'
    else:
        print(f'{cores["vermelho"]}RESPOSTA INVALIDA{cores["fechar"]}')  # se o valor não for nem s e nem n ele vai continuar a repetição
while b == 'True':
    if pergunta == 's' or pergunta == 'n':
        nada = 0
    else:
        print('-=' * 25)
        print(f'{" JOKENPO ":=^50}')  # TITULO
        print('-=' * 25)
        print('''suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
[ 4 ] LARGATO
[ 5 ] SPOCK''')
    jogada = int(input('qual e a sua jogada: '))
    computador = randint(1, 5) # a jogada do computador
    while jogada >= 6: # enquanto a jogada for maior que ou igual a 6 ele nao vai parar de repetir
        print(f'{cores["vermelho"]}JOGADA INVALIDA.tente novamente{cores["fechar"]}')
        jogada = int(input('qual e a sua jogada: '))
    sleep(0.7)
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO')
    win = 'COMPUTADOR VENCEU' # ja defino que o computador venceu para minimizar esforço e so mudar se o jogador vencer
    print('-=-' * 10) # nao deu pra colocar em baixo mais o items puxa o que tem dentro dos items
    print(f'''COMPUTADOR JOGOU {items[computador - 1]} 
JOGADOR jogou {items[jogada - 1]}''')
    print('-=-' * 10)
    if jogada == computador: # empate
        win = 'EMPATE'
    elif jogada == 1 and computador == 3:
        win = 'JOGADOR VENCEU'
    elif jogada == 1 and computador == 4:
        win = 'JOGADOR VENCEU'
    elif jogada == 2 and computador == 1:
        win = 'JOGADOR VENCEU'
    elif jogada == 2 and computador == 5:
        win = 'JOGADOR VENCEU'
    elif jogada == 3 and computador == 2:
        win = 'JOGADOR VENCEU'
    elif jogada == 3 and computador == 4:
        win = 'JOGADOR VENCEU'
    elif jogada == 4 and computador == 2:
        win = 'JOGADOR VENCEU'
    elif jogada == 4 and computador == 5:
        win = 'JOGADOR VENCEU'
    elif jogada == 5 and computador == 1:
        win = 'JOGADOR VENCEU'
    elif jogada == 5 and computador == 3: # isso aqui tudo e pra mudar o computador vence pra jogador vence
        win = 'JOGADOR VENCEU'
    print(win)
    c = 'True'
    while c == 'True':
        cont = str(input('você deseja continuar jogando?(S/N): ')).strip().lower()
        if cont[0] == 'n':
            b = 'False'
            c = 'False'
        elif cont[0] == 's':
            c = 'False'
        else:
            print(f'{cores["vermelho"]}RESPOSTA INVALIDA{cores["fechar"]}')
