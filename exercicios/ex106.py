from time import sleep
cores = {'branco': '\033[7;30m',
         'vermelho': '\033[0;30;41m',
         'verde': '\033[0;30;42m',
         'amarelo': '\033[0;30;43m',
         'azul': '\033[0;30;44m',
         'roxo': '\033[0;30;45m',
         'azulmarinho': '\033[0;30;46m',
         'cinza': '\033[0;30;47m',
         'fechar': '\033[m'}


def ajuda(comando):
    help(f'{comando}')


def titulo(txt, cor='fechar'):
    tam = len(txt)
    print(cores[f'{cor}'], end='')
    print(f'-=' * tam)
    print(f'{txt:^{tam * 2}}')
    print('-=' * tam)
    print(cores['fechar'], end='')


while True:
    titulo('SISTEMA DE AJUDA PYHELP', 'verde')
    sleep(1)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        titulo(f'ACESSANDO O MANUAL DO "{comando}" ', 'azul')
        sleep(1)
        print(cores['branco'], end='')
        ajuda(comando)
        print(cores['fechar'], end='')
sleep(1)
titulo('ATE LOGO', 'vermelho')
