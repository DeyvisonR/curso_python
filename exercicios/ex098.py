from time import sleep


def contador(a, b, c):
    a = 1
    b = 10
    c = 1
    cont = 0
    print(f'contagem de {a} até {b} de {c} em {c}')
    while cont < 10:
        print(f'{a} => ', end='')
        sleep(0.5)
        a = a + c
        cont = cont + 1
    print('Fim')
    a = 0
    cont = 0
    sleep(0.5)
    print(f'contagem de {b} até {a} de {c} em {c}')
    while cont < 6:
        print(f'{b} => ', end='')
        sleep(0.5)
        b = b - 2
        cont = cont + 1
    print('Fim')
    cont = 0
    print('agora e sua vez de personalizar a contagem!')
    a = int(input('Inicio: '))
    b = int(input('Fim: '))
    c = str(input('Passo: '))
    if c == 0:
        c = 1
    if len(c) == 2:
        c = int(c[1])
    print(f'contagem de {a} ate {b} de {c} em {c}')
    while a <= b or a >= b:
        print(f'{a} => ', end='')
        sleep(0.5)
        if a < b:
            cont = cont + 1
            a = a + c
            if a >= b:
                print(f'{b}')
                break
        elif a > b:
            cont = cont + 1
            a = a - c
            if a <= b:
                break
    if b == 0:
        print('0 => ', end='')
    print('FIM')
