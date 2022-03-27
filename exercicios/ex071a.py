print('=' * 50)
print(f'{"BANCO DA PROGRAMAÇÃO":^50}')
print('=' * 50)
valor = int(input('que valor você quer sacar: '))
total = valor
ced = 50
contced = 0
while True:
    if total >= ced:
        total = total - ced
        contced = contced + 1
    else:
        print(f'total de {contced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
print('volte sempre!!!')
