n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
if n1 > n2:
    print('o número {} e maior'.format(n1))
elif n2 > n1:
    print('o número {} e maior'.format(n2))
else:
    print('os dois números são iguais')