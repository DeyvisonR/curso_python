lista = []
cont = 0
maior = []
menor = []
for n in range(0, 6):
    num = (int(input(f'digite um número para a posição {n}: ')))
    cont = cont + 1
    lista.append(num)
    if cont == 1:
        maiorn = num
        menorn = num
    else:
        if num > maiorn:
            maiorn = num
        if num < menorn:
            menorn = num
for p, v in enumerate(lista):
    if v == maiorn:
        maior.append(p)
    if v == menorn:
        menor.append(p)
print(f'você digitou os valores {lista}')
print(f'o maior valor foi {max(lista)} e ele apareceu na posição: ', end='')
for c in maior:
    print(c, end=' ')
print(f'\no menor valor foi {min(lista)} e ele apareceu na posição: ', end='')
for e in menor:
    print(e, end=' ')
