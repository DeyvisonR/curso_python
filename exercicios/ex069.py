continuar = ' '
mvelho = 0
homens = 0
mulheresn = 0
while continuar != 'n':
    print('-=' * 20)
    print(f'{"CADASTRO DE PESSOAS":^40}')
    print('-=' * 20)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('sexo: ')).strip().lower()[0]
        if sexo not in 'mf':
            print('\033[31msexo invalido. tente novamente\033[m')
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('você quer continuar [S/N]: ')).strip().lower()[0]
        if continuar not in 'sn':
            print('\033[31mresposta invalida. tente novamente\033[m')
    if idade > 18:
        mvelho = mvelho + 1
    if sexo == 'm':
        homens = homens + 1
    if idade < 20:
        mulheresn = mulheresn + 1
print('-=-' * 10)
print(f'tem {mvelho} pessoas com mais de 18 anos')
print(f'tem {homens} homens cadastrados')
print(f'tem {mulheresn} mulheres com menos de 20 anos')
