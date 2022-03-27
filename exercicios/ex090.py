dicionario = {}
lista = []
dicionario['nome'] = str(input('digite seu nome: '))
dicionario['nota 1'] = float(input('digite a sua primeira nota: '))
dicionario['nota 2'] = float(input('digite a sua segunda nota: '))
dicionario['media'] = (dicionario['nota 1'] + dicionario['nota 2']) / 2
if dicionario['media'] >= 7:
    dicionario['situação'] = 'aprovado'
else:
    dicionario['situação'] = 'reprovado'
lista.append(dicionario.copy())
for k, v in dicionario.items():
    print(f'{k} e igual a {v}')
