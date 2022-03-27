salario = float(input('qual e o salario do funcionario: '))
if salario >= 1251:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento))