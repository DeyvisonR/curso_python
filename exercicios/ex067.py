num = 0
while num >= 0:
    num = int(input('digite um número para ver a sua tabuada: '))
    cont = 0
    if num >= 0:
        while cont < 10:
            cont = cont + 1
            print(f'{num} x {cont} = {num * cont}')
