from time import sleep


def contador(a, b, c):
    print(f'contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} => ', end='')
            sleep(0.5)
            cont = cont + c
        print('FIM')
    if a > b:
        cont = a
        while cont >= b:
            print(f'{cont} => ', end='')
            sleep(0.5)
            cont = cont - c
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('agora e sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = str(input('Passo: '))
if c == 0:
    c = 1
if len(c) == 2:
    c = c[1]
c = int(c)
contador(a, b, c)
