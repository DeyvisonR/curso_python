pessoas = []
maiorp = 0
menorp = 0
while True:
    nome = str(input('digite seu nome: '))
    peso = float(input('digite seu peso: '))
    pessoas.append([nome, peso])
    if len(pessoas) == 1:
        maiorp = menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('quer continuar [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'{len(pessoas)} pessoas foram cadastradas.')
pessoasml = []
pessoasmp = []
for p in pessoas:
    if p[1] == menorp:
        pessoasml.append(p[0])
    elif p[1] == maiorp:
        pessoasmp.append(p[0])
print(f'o maior peso foi de {maiorp:.1f}Kg. peso de: {pessoasmp}')
print(f'o menor peso foi de {menorp:.1f}Kg. peso de {pessoasml}')
