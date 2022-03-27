lista = []
continuar = ' '
cont = 0
while continuar != 'n':
    n = ' '
    while n.isnumeric() == False:
        n = input('digite um número: ')
        if n.isnumeric() == False:
            print('o valor digitado não e um número')
    n = int(n)
    lista.append(n)
    cont = cont + 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('quer continuar [S/N]: ')).strip().lower()[0]
print(f'você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'os valores digitados em ordem decrescente: {lista}')
if 5 in lista:
    print(f'o número 5 foi encontrado na lista na posição {lista.index(5) + 1}')
else:
    print(f'o número 5 não foi encontrado')
