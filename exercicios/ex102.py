def fatorial(num, show=False):
    '''
        -> calcula o fatorial de um número
    :param num: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor fatorial de um número num
    '''
    f = 1
    for c in range(num, 0, -1):
        f = f * c
        if show == True:
                print(f'{c}', end='')
                print(' x ' if c >= 2 else ' = ', end='')
    return f


n = int(input('você quer ver o fatorial de qual número?: '))
resp = ' '
while resp not in 'sn':
    resp = str(input('você quer ver o calculo?: ')).lower().strip()[0]
    if resp == 's':
        print(fatorial(n, show=True))
    else:
        print(fatorial(n))
