nome = str(input('nome do funcionário: '))
salario = float(input('salario do funcionário: '))
aumento = salario + (salario * 15 / 100)
print('o funcionario {} que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(nome, salario, aumento))
