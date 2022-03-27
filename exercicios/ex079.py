lista = []
continuar = ' '
while continuar != 'n':
    n = ' '
    while n.isnumeric() == False:
        n = input('digite um número: ')
        if n.isnumeric() == False:
            print('o valor digitado não e um número')
    n = int(n)
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado. ele não sera adicionado a lista')
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('você quer continuar [S/N]: ')).strip().lower()[0]
print(f'os valores digitados foram: {sorted(lista)}')
