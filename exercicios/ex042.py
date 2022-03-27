print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar um triângulo!')
    teste = 'True'
else:
    print('os segmentos acima não podem formar um triângulo!')
    teste = 'False'
if teste == 'True':
    if r1 == r2 and r1 == r3:
        print('os seguimentos formam um triângulo equilátero')
    elif r1 == r3 or r1 == r2 or r2 == r3:
        print('os segmentos formam um triângulo isóceles')
    else:
        print('os segmentos formam um triângulo escaleno')
