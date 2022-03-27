print('-=-' * 10)
print(f'{" sequencia de fibonacci ":^30}')
print('-=-' * 10)
n = int(input('quantos elementos da sequencia de fibonacci você quer ver: '))
t1 = 0
t2 = 1
cont = 2
print(f'{t1} > {t2} > ', end='')
while cont < n:
    t3 = t1 + t2
    print(f'{t3} > ', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM')
