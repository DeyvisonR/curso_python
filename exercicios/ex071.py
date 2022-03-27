print('=' * 50)
print(f'{"BANCO DA PROGRAMAÇÃO":^50}')
print('=' * 50)
valor = int(input('que valor você quer sacar: '))
if valor >= 1:
    valor50 = valor // 50
    print(f'total de {valor50} notas de 50')
    valor = valor % 50
    valor20 = valor // 20
    if valor20 >= 1:
        print(f'total de {valor20} notas de 20')
    valor = valor % 20
    valor10 = valor // 10
    if valor10 >= 1:
        print(f'total de {valor10} notas de 10')
    valor = valor % 10
    valor1 = valor
    if valor1 >= 1:
        print(f'total de {valor1} notas de 1')
else:
    print('\033[31mvalor invalido.\033[m digite um valor acima de 1 real')
print('volte sempre ao banco da programação! tenha um bom dia!!')
