print('-=-' * 7)
print('calculando fatorial')
print('-=-' * 7)
f = 1
n = int(input('digite um número: '))
c = n
print(f'{n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)
