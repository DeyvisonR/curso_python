matriz = []
tamanho = int(input('Qual será o tamanho da sua matriz? '))
somacolunas = []
#gerar as listas dentro da lista matriz
for c in range(0, tamanho):
    matriz.append([])
    somacolunas.append([0])
print(matriz)
print(somacolunas)

for l in range(0, tamanho):
    for c in range(0, tamanho):
        matriz[l].append(int(input(f'Digite um numero para a posiçao {l, c}: ')))
        somacolunas[c] = [matriz[l][c] + somacolunas[c][0]]

for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print()

for coluna in range(0, tamanho):
    print(f'A soma da coluna {coluna} é {somacolunas[coluna]}')
