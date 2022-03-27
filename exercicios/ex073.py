times = ('são paulo', 'atletico-mg', 'flamengo', 'internacional', 'gremio', 'palmeiras', 'fluminense', 'santos', 'corinthians', 'ceara', 'athletico', 'atletico-go', 'bragantino', 'fortaleza', 'sport recife', 'bahia', 'vasco da gama', 'goias', 'botafogo', 'coritiba')
print('-=-' * 20)
print(f'{" TIMES DO BRAZILEIRÃO ":^60}')
while True:
    print('-=-' * 20)
    while True:
        alt = input(('''menu:
[ 1 ] para ver a lista de times completa do brasileirão
[ 2 ] para ver os 5 primeiros times da lista
[ 3 ] para ver os ultimos 4 times da lista
[ 4 ] para ver os times em ordem alfabetica
[ 5 ] para localizar um time
[ 6 ] para finalizar o programa
opção: '''))
        if alt.isnumeric() == True:
            break
        else:
            print('digito invalido. tente novamente')
            print('-=-' * 20)
    alt = int(alt)
    print('-=-' * 20)
    if alt == 1:
        print(f'lista de times do brasileirão: {times}')
    elif alt == 2:
        print(f'os primeiros 5 times da lista são: {times[0:5]}')
    elif alt == 3:
        print(f'os ultimos 4 times da lista são: {times[-4:]}')
    elif alt == 4:
        print(f'times em ordem alfabetica: {sorted(times)}')
    elif alt == 5:
        timelo = ' '
        while timelo not in times:
            timelo = str(input('qual time você quer localizar: ')).lower().strip()
            if timelo in times:
                print(f'o time {timelo} esta na posição {times.index(timelo) + 1}ª')
            elif timelo not in times:
                print('time inesixtente! tente novamente')
                cancelar = ' '
                while cancelar not in 'sn':
                    cancelar = str(input('deseja cancelar a busca [S/N]: ')).strip().lower()[0]
                if cancelar == 's':
                    break
    elif alt == 6:
        print('PROGRAMA ENCERRADO')
        break
    else:
        print('alternativa invalida. tente novamente')
