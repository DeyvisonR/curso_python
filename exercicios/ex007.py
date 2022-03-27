nome = str(input('nome do aluno: '))
n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
n3 = float(input('terceira nota do aluno: '))
n4 = float(input('quarta nota do aluno: '))
m = (n1 + n2 + n3 + n4) / 4
print('a media de {} e {} é igual a {}'.format(n1, n2, m))
if m >= 5.0:
    print(f'o aluno {nome} passou de ano parabens!!!')
else:
    print(f'o aluno {nome} foi reprovado ;-;')
