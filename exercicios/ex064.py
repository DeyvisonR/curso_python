soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('digite um número. digite [999 para parar]: '))
    soma = n + soma
    cont = cont + 1
print(f'você digitou {cont - 1} números e a soma deles foi de {soma - 999}')
