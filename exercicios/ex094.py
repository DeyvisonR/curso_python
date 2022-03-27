continuar = ' '
dicionario = {}
lista = []
while continuar != 'n':
    dicionario['nome'] = str(input('Nome: '))
    sexo = ' '
    while sexo[0] not in 'mf':
        sexo = str(input('Sexo: ')).strip().lower()
        if sexo[0] not in 'mf':
            print('valor invalido. tente novamente')
        if sexo[0] in 'mf':
            dicionario['sexo'] = sexo
    idade = ' '
    while idade.isnumeric() == False:
        idade = input('Idade: ')
        if idade.isnumeric() == False:
            print('o valor digitado não e um número')
    idade = int(idade)
    dicionario['idade'] = idade
    continuar = ' '
    while continuar[0] not in 'sn':
        continuar = str(input('você quer continuar: ')).strip().lower()
    lista.append([dicionario.copy()])
    dicionario.clear()
print(f'ao todo foram cadastradas {len(lista)} pessoas')
soma = 0
listademulheres = []
pessoasacmedia = []
for c in range(0, len(lista)):
        soma = soma + lista[c][0]['idade']
        if lista[c][0]['sexo'][0] == 'f':
            listademulheres.append(lista[c][0]['nome'])
media = soma / len(lista)
print(f'a media de idade do grupo e de {media:.0f} anos')
if len(listademulheres) >= 1:
    print(f'todas as mulheres cadastradas: {listademulheres}')
else:
    print('não foi cadastrada nem uma mulher')
for c in range(0, len(lista)):
    if lista[c][0]['idade'] > media:
        pessoasacmedia.append(lista[c][0]['nome'])
if len(pessoasacmedia) >= 1:
    print(f'pessoas com a idade acima da media: {pessoasacmedia}')
else:
    print('todas as pessoas tem a idade abaixo da media')
