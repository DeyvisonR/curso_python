matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = cont = somat = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = ' '
        while n.isnumeric() == False:
            n = input(f'digite um valor para [{l}, {c}]: ')
            if n.isnumeric() == False:
                print('o valor digitado não e um número')
        n = int(n)
        cont = cont + 1
        if n % 2 == 0:
            somap = somap + n
        if cont == 3 or cont == 6 or cont == 9:
            somat = somat + n
        if cont > 3 and cont < 7:
            if cont == 4:
                maior = n
            else:
                if n > maior:
                    maior = n
        matriz[l][c] = n
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'a soma de todos os valores pares digitados foi: {somap}')
print(f'a soma de todos os valores da terceira coluna e de {somat}')
print(f'o maior valor da segunda coluna e {maior}')
