cont = 0
n = int(input('digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mo número {n} foi divisível {cont} vezes')
if cont >= 3:
    print('O NÚMERO NÃO E PRIMO')
else:
    print('O NÚMERO E PRIMO')
