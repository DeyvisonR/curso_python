a = ''
frase = str(input('digite uma frase: ')).strip().lower().replace(' ', '')
for c in range(1, len(frase) + 1):
    a = a + frase[::-c]
b = a[0:len(frase)]
if b == frase:
    print('a frase é um palíndromo')
else:
    print('a frase não é um palíndromo')
