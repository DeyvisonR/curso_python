print('=' * 50)
print(f"{'10 TERMOS DE UMA PA':^50}")
print('=' * 50)
pt = int(input('digite o primeiro termo: '))
razao = int(input('razão: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo + 1, razao):
    print(f'{c} > ', end='')
print('ACABOU')
