cores = {'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'azulmarinho': '\033[36m',
         'cinza': '\033[37m',
         'fechar': '\033[m'}
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
n4 = float(input('quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5.0:
    print('{}REPROVADO{}'.format(cores['vermelho'], cores['fechar']))
if media >= 3.0 and media < 5.0:
    print('o aluno esta em recuperção')
if media >= 5.0:
    print('{}APROVADO{}'.format(cores['verde'], cores['fechar']))
