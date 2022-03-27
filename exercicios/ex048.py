soma = 0
valor = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = c + soma
        valor = valor + 1
print(f'a soma de todos os {valor} valores e igual a {soma}')