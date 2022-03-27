nome = str(input('digite seu nome completo: '))
a = nome.split()
print('primeiro nome: {} '.format(a[0]))
print('ultimo nome: {}'.format(a[len(a) - 1]))
