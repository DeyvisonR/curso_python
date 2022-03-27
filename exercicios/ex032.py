import datetime
ano = int(input('que ano você quer analizar? coloque o número 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {} é bisexto'.format(ano))
else:
    print('o ano de {} não e bisexto'.format(ano))
