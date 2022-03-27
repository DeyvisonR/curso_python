from random import randint
print('-=' * 25)
print(f'{"VAMOS JOGAR PAR OU IMPAR":^50}')
print('-=' * 25)
jogador = 0
computador = 0
cont = 0
while True:
    jogador = int(input('digite um número: '))
    opcao = ' '
    while opcao not in 'pi':
        opcao = str(input('você quer PAR ou IMPAR: ')).strip().lower()[0]
    computador = randint(1, 10)
    num = (jogador + computador) % 2
    print('-' * 50)
    print(f'você jogou {jogador} e o computador jogou {computador}')
    print('-' * 50)
    teste = '\033[31mcomputador ganhou\033[m'
    if opcao == 'p' and num == 0:
        print('vamos jogar novamente.....')
        teste = '\033[32mjogador ganhou\033[m'
        cont = cont + 1
    elif opcao == 'i' and num == 1:
        print('vamos jogar novamente.....')
        teste = '\033[32mjogador ganhou\033[m'
        cont = cont + 1
    print(f'{teste}')
    print('-=-' * 15)
    if teste == '\033[31mcomputador ganhou\033[m':
        break
print(f'GAME OVER. você venceu {cont} vezes')
