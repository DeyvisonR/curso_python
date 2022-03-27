tupla = (int(input('digite o primeiro valor: ')),
        int(input('digite o segundo valor: ')),
        int(input('digite o terceiro valor: ')),
        int(input('digite o quarto valor: ')))
print(f'você digitou os valores {tupla}')
print(f'o número 9 aparareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o número 3 apareceu na posição {tupla.index(3)+1}ª')
else:
    print('o valor 3 não foi digitado em nem uma posição')
print(f'os números pares digitados foram: ', end='')
cont = 0
for n in tupla:
    if n % 2 == 0:
        cont = cont + 1
        print(n, end='')
if cont == 0:
    print('não foram digitados valores pares')
