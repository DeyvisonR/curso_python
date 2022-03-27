from datetime import date
dicionario = {}
dicionario['nome'] = str(input('Nome: ')).strip()
anoatual = date.today().year
anodena = int(input('Ano de nascimento: '))
dicionario['idade'] = anoatual - anodena
ctps = int(input('Carteira de trabalho (0 não tem): '))
dicionario['ctps'] = ctps
if ctps > 0:
    dicionario['contratação'] = int(input('ano de contratação: '))
    dicionario['salário'] = str(input(f'Salário: '))
    aposentadoria = ((dicionario['contratação'] + 35) - anoatual) + dicionario['idade']
    dicionario['aposentadoria'] = aposentadoria
print('-=' * 20)
print(dicionario)
for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')
