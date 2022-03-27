soma = 0
cont = 0
maior = 0
menor = 0
quest = ' '
while quest != 'n':
    n = int(input('digite um número: '))
    soma = soma + n
    cont = cont + 1
    quest = str(input('você quer continuar [S/N]: ')).lower().strip()[0]
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'a media entre todos os {cont} valores e de {soma / cont}')
print(f'o maior número digitado foi {maior} e o menor número digitado foi {menor}')
