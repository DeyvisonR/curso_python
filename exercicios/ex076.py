tupla = ('lápis', 1.75, 'borracha', 2.00, 'caderno', 15.90,
         'estojo', 25.00, 'transferidor', 4.20,
         'compasso', 9.99, 'mochila', 120.32,
         'canetas', 22.30, 'livros', 34.90)
print('=' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('=' * 50)
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<40}R${tupla[c+1]:>8.2f}')
print('=' * 50)
