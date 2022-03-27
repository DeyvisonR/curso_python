matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somavaloter = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = ' '
        while n.isnumeric() == False:
            n = input(f'digite um valor para [{l}, {c}]: ')
            if n.isnumeric() == False:
                print('o valor digitado não e um número')
        n = int(n)
        matriz[l][c] = n
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap = somap + matriz[l][c]
    print()
for c in range(0, 3):
    somavaloter = somavaloter + matriz[c][2]
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'a soma de todos os valores pares digitados e de {somap}')
print(f'a soma de todos os valores da terceira coluna e de {somavaloter}')
print(f'o maior valor da segunda linha foi {maior}')
