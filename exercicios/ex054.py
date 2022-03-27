from datetime import date
contm = 0
contn = 0
atual = date.today().year
for c in range(1, 8):
    nasc = int(input((f'em que ano a {c}ª pessoa nasceu: ')))
    idade = atual - nasc
    if idade >= 18:
        contm = contm + 1
    else:
        contn = contn + 1
print(f'ao todo tivemos {contm} pessoas maiores de idade')
print(f'e tambem tivemos {contn} pessoas menores de idade')
