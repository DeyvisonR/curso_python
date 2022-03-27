cont = 0
n = int(input('digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mo número {n} foi divisivel por {cont} vezes')
if cont == 2:
    print('E POR ISSO O NÚMERO E PRIMO')
else:
    print('E POR ISSO O NÚMERO NÃO E PRIMO')
