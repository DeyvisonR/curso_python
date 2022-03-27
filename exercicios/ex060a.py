f = 1
print('calculando fatorial')
n = int(input('digite um número: '))
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = c * f
print(f)
