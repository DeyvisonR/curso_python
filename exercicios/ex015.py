dias = int(input('quantos dias alugados?: '))
kmrodados = float((input('quantos KM rodados?: ')))
total = (dias * 60) + (0.15 * kmrodados)
print('o total a pagar é de: R${:.2f} '.format(total))
