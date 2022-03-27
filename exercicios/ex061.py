print('=' * 50)
print(f"{'10 TERMOS DE UMA PA':^50}")
print('=' * 50)
pt = int(input('digite o primeiro termo: '))
razao = int(input('razão: '))
termo = pt
cont = 1
while cont < 11:
    print(termo, end=' > ')
    termo = termo + razao
    cont = cont + 1
print('FIM')
