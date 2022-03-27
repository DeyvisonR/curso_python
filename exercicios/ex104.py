def leiaint(a=' '):
    b = a
    while a.isnumeric() == False:
        a = input(b)
        if a.isnumeric() == False:
            print('\033[31mERRO! digite um número válido\033[m')
    a = int(a)
    return a


n = leiaint('digite um numero1: ')
print(f'você digitou o número {n} e {n} x {n} = {n * n}')
