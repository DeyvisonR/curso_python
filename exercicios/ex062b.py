print('=' * 50)
print(f'{"10 TERMOS DE UMA PA":^50}')
print('=' * 50)
primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
termo = primeiro
cont = 0
total = 0
question = 10
while question != 0:
    total = total + question
    while cont < total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA', end='')
    question = int(input('\nquantos termos você quer mostrar a mais [0 para parar]: '))
print(f'progressão finalizada com {cont} termos mostrados')
