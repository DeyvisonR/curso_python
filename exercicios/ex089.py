lista = []
continuar = ' '
while continuar not in 'n':
    nome = str(input('nome do aluno: '))
    while True:
        nota1 = float(input('nota 1: '))
        if nota1 < 10.1:
            break
    while True:
        nota2 = float(input('nota 2: '))
        if nota2 < 10.1:
            break
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('quer continuar [S/N]: ')).strip().lower()[0]
        if continuar not in 'sn':
            print('digito invalido. tente novamente')
print('-=' * 20)
print(f'{"N°"} {"nome":^30} {"media":>5}')
print('-=' * 20)
for c in range(0, len(lista)):
    print(f'{c:} {lista[c][0]:^30} {lista[c][2]:>5}')
while True:
    notas = int(input('mostrar notas de qual aluno (999 para parar): '))
    print('-=' * 20)
    if notas == 999:
        break
    elif notas > len(lista) - 1:
        print('valor invalido. tente novamente')
    if notas <= len(lista) - 1:
        print(f'as notas de {lista[notas][0]} são {lista[notas][1][0]} e {lista[notas][1][1]}')
        print('-=' * 20)
