print('-=-' * 20)
print('conversor de bases numericas')
print('-=-' * 20)
n = int(input('digite um número inteiro: '))
print('você quer converter para')
print('''[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
nc = int(input('digite o número para qual deseja converter: '))
if nc == 1:
    print('o número {} em BINARIO é {}'.format(n, bin(n)[2:]))
elif nc == 2:
    print('o número {} em OCTAL é {}'.format(n, oct(n)[2:]))
elif nc == 3:
    print('o número {} em HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('opção inexistente. tente novamente')