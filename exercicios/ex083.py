expressão = str(input('digite uma expressão: '))
if expressão.count('(') == expressão.count(')'):
    print('a expressão e valida')
else:
    print('a expressão e invalida')
