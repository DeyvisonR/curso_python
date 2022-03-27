soma = 0
cont = 0
valores = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'setimo')
for c in range(0, 7):
    n = int(input(f'digite o {valores[c]} número: '))
    if n % 2 == 0:
        soma = n + soma
        cont = cont + 1
print(f'você informou {cont} números pares e a soma de todos os valores e igual a {soma}')
