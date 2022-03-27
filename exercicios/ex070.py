cont = ' '
total = 0
maior = 0
iniciar = 0
while cont != 'n':
    nome = str(input('digite o nome do produto: ')).strip()
    preço = float(input('digite o preço do produto: '))
    total = total + preço
    cont = ' '
    iniciar = iniciar + 1
    if iniciar == 1:
        menor = preço
        nomemb = nome
    else:
        if preço < menor:
            menor = preço
            nomemb = nome
    if preço > 1000:
        maior = maior + 1
    while cont not in 'sn':
        cont = str(input('você quer continuar [S/N]: ')).strip().lower()[0]
print(f'o total gasto na compra foi de {total:.2f}')
print(f'{maior} produtos custaram mais de 1000R$')
print(f'o produto mais barato foi o {nomemb} que custou {menor:.2f}')
