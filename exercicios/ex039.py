import datetime
nasci = int(input('ano de nascimento: '))
anoat = datetime.date.today().year
idade = anoat - nasci
print('quem nasceu em {} tem {} anos em {}'.format(nasci, idade ,anoat))
if idade < 18:
    print('ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('seu alistamento será em {}'.format(18 - idade + anoat))
elif idade > 18:
    print('você ja deveria ter se alistado há {} anos'.format(idade - 18))
    print('seu alistamento foi em {}'.format(anoat - (idade - 18)))
else:
    print('você tem que se alistar IMEDIATAMENTE!!!')
