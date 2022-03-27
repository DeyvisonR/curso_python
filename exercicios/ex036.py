valorc = float(input('valor da casa: '))
salario = float(input('quanto você recebe de salario: '))
anos = int(input('em quantos anos você pretende pagar: '))
mensalidade = valorc / (anos * 12)
salario30 = (salario * 30 / 100)
print('para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valorc, anos, mensalidade))
if salario30 < mensalidade:
    print('empréstimo negado')
else:
    print('empréstimo pode ser concedido!')
