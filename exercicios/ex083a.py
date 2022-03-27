lista = []
abre = 0
fecha = 0
expressão = str(input('digite uma expressão: '))
lista.append(expressão)
for v in lista:
    for digito in v:
        if digito == '(':
            abre = abre + 1
        elif digito == ')':
            fecha = fecha + 1
if abre == fecha:
    print('a expressão e valida')
else:
    print('a expressão e invalida')