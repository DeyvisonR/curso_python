lista = []
cont = 0
maior = []
menor = []
for n in range(0, 6):
    lista.append(int(input(f'digite um número para a posição {n}: ')))
    cont = cont + 1
for p, v in enumerate(lista):
    if v == max(lista):
        maior.append(p)
    if v == min(lista):
        menor.append(p)
print(f'você digitou os valores {lista}')
print(f'o maior valor foi {max(lista)} e ele apareceu na posição: {maior}', end=' ')
print(f'\no menor valor foi {min(lista)} e ele apareceu na posição: {menor}', end='')
