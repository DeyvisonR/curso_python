print('-=-' * 20)
print(f'{"aproveitamento de um jogador de fotebol":^60}')
print('-=-' * 20)
dicionario = {}
listadegols = []
somadegols = 0
listadetudo = []
a = True
while a == True:
    dicionario['nome'] = str(input('nome do jogador: '))
    partidas = int(input(f'quantas partidas o {dicionario["nome"]} jogou: '))
    dicionario['partidas'] = partidas
    for c in range(0, partidas):
        gols = int(input(f'você fez quantos gols na partida {c + 1}: '))
        listadegols.append(gols)
        somadegols = somadegols + gols
    dicionario['gols'] = listadegols[:]
    dicionario['total'] = somadegols
    listadetudo.append(dicionario.copy())
    dicionario.clear()
    listadegols.clear()
    somadegols = 0
    continuar = ' '
    while continuar[0] not in 'sn':
        continuar = str(input('quer continuar: ')).strip().lower()
        if continuar[0] not in 'sn':
            print('digito invalido. tente novamente')
        if continuar[0] == 'n':
            a = False
print('-=-' * 20)
print(f'{"cod":<10}{"nome":<15}{"gols":<20}{"total":<20}')
for c in range(0, len(listadetudo)):
    print(f'{c:<10}{listadetudo[c]["nome"]:<15}{listadetudo[c]["gols"]!s:<20s}{listadetudo[c]["total"]:<22}')
print('-=-' * 20)
njogador = 0
while njogador != 999:
    njogador = int(input('mostrar dados de qual jogador (999 para parar): '))
    if njogador <= len(listadetudo) - 1:
        print(f'  -- LEVANTAMENTO DO JOGADOR {listadetudo[njogador]["nome"]}:')
        for i, v in enumerate(listadetudo[njogador]['gols']):
            print(f'  =>  no jogo {i + 1} fez {v} gols')
        print('-' * 50)
    elif njogador > len(listadetudo) - 1:
        print(f'ERRO! não existe jogador com codigo {njogador}! tente novamente')
