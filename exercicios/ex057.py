sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('\033[31mdados invalidos.\n\033[mpor favor, informe seu sexo [M/F]: ')).strip().upper()
print(f'sexo {sexo[0]} registrado com sucesso')
