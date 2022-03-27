lista = []
for c in range(0, 5):
    n = ' '
    while n.isnumeric() == False:
        n = input('digite um número: ')
        if n.isnumeric() == False:
            print('o valor digitado não e um número')
    n = int(n)
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado para o final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado para a posição {pos}')
                break
            pos = pos + 1
print(f'os valores digitados em ordem crescente: {lista}')
