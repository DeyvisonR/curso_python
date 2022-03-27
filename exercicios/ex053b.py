frase = str(input('digite uma frase: ')).strip().lower().replace(' ', '')
b = frase[::-1]
print(b)
if b == frase:
    print('a frase é um palíndromo')
else:
    print('a frase não é um palíndromo')
