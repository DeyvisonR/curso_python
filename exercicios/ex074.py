from random import randint
tupla = (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999))
print(f'os valores gerados na tupla foram: ', end='')
cont = 0
for valor in tupla:
    print(valor, end=' ')
    cont = cont + 1
    if cont == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print(f'\no menor valor gerado foi {menor}')
print(f'o maior valor gerado foi {maior}')