pessoas = []
maiorp = menorp = 0
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
print(f'o maior peso foi de {maiorp:.1f}Kg. peso de: ', end='')
for p in pessoas:
    if p[1] == maiorp:
        print(f'{p[0]}, ', end='')
print(f'\no menor peso foi de {menorp:.1f}Kg. peso de: ', end='')
for p in pessoas:
    if p[1] == menorp:
        print(f'{p[0]}, ')
