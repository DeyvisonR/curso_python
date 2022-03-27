opcao = 0
n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
while opcao != 5:
    print('''[ 1 ] soma
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('qual e a sua escolha: '))
    if opcao == 1:
        print('-=-' * 10)
        print(f'a soma de {n1} + {n2} e igual a {n1 + n2}')
        print('-=-' * 10)
    elif opcao == 2:
        print('-=-' * 10)
        print(f'a soma de {n1} x {n2} e igual a {n1 * n2}')
        print('-=-' * 10)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('-=-' * 10)
        print(f'o maior número digitado foi {maior}')
        print('-=-' * 10)
    elif opcao == 4:
        n1 = int(input('digite um novo número: '))
        n2 = int(input('digite outro novo número: '))
    elif opcao == 5:
        break
    else:
        print('\033[31mopção invalida\033[m')
