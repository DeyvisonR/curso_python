print('=' * 50)
print(f"{'10 TERMOS DE UMA PA':^50}")
print('=' * 50)
pt = int(input('digite o primeiro termo: '))
razao = int(input('razão: '))
termo = pt
cont = 1
cont2 = 0
while cont < 11:
    print(termo, end=' > ')
    termo = termo + razao
    cont = cont + 1
    cont2 = cont2 + 1
print('PAUSA', end='')
termo = termo - razao
a = 'True'
while a == 'True':
    quantos = int(input('\nquantos termos você quer ver a mais: '))
    if quantos >= 1:
        while quantos > 0:
            termo = termo + razao
            quantos = quantos - 1
            cont2 = cont2 + 1
            print(termo, end=' > ')
        print('PAUSA', end='')
    elif quantos == 0:
        a = 'False'
print(f'\033[4;31mFIM DO PROGRAMA. no total você viu {cont2} termos\033[m')
