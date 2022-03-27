print(f'{"LOJAS IMAGINARIAS":=^40}')
preco = float(input('preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('qual é a opção: '))
if opcao == 1:
    desconto = preco - (preco * 10 / 100)
    print(f'sua compra de {preco} vai custar {desconto} com 10% de desconto')
elif opcao == 2:
    desconto = preco - (preco * 5 / 100)
    print(f'sua compra de {preco} vai custar {desconto} com 10% de desconto')
elif opcao == 3:
    print(f'sua compra de {preco} continuara custando {preco}')
elif opcao == 4:
    parcelas = int(input('quantas parcelas: '))
    npreco = preco + (preco * 20 / 100)
    parcela = npreco / parcelas
    print(f'sua compra de {preco} sera parcelada em {parcelas}x de R${parcela} com juros')
    print(f'e no total saira por {npreco}')
else:
    print('opção inexistente. tente novamente ')
