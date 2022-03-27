lista = [[], []]
for c in range(1, 8):
    valor = ' '
    while valor.isnumeric() == False:
        valor = input(f'digite o {c}º número: ')
        if valor.isnumeric() == False:
            print('o valor digitado não e um número')
    valor = int(valor)
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
print(sorted(lista[0]))
print(sorted(lista[1]))
