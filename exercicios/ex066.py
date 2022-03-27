n = 0
cont = 0
soma = 0
while True:
    n = int(input('digite um número [999 para parar]: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'você digitou {cont} números e a soma deles e igual a {soma}')
