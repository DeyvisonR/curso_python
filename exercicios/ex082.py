continuar = ' '
lista = []
pares = []
impares = []
while continuar != 'n':
    n = ' '
    while n.isnumeric() == False:
        n = input('digite um valor: ')
        if n.isnumeric() == False:
            print('o valor digitado não e um número')
    n = int(n)
    lista.append(n)
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('você quer continuar [S/N]: ')).strip().lower()[0]
print(f'a lista de valores completa foi {lista}')
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    elif lista[c] % 2 == 1:
        impares.append(lista[c])
print(f'os valores pares foram {pares}')
print(f'os valores impares foram {impares}')
