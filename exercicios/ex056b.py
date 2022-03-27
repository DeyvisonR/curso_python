soma = 0
cont = 0
maior = 0
mulher = 0
nomemaisvelho = ''
for p in range(1, 5):
    print(f'----- {p}ª pessoa -----')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().lower()
    soma = idade + soma
    cont = cont + 1
    if p == 1 and sexo == 'm':
        nomemaisvelho = nome
        maior = idade
    if sexo == 'm' and idade > maior:
        maior = idade
        nomemaisvelho = nome
    if sexo == 'f' or sexo == 'm':
        if sexo == 'f':
            if idade < 20:
                mulher = mulher + 1
    else:
        print('sexo invalido')
print(f'a media de idade do grupo è de {soma / cont}')
print(f'o homem mais velho do grupo e o {nomemaisvelho} que tem {maior} anos')
print(f'no registro de pessoas existem {mulher} mulheres com menos de 20 anos')
