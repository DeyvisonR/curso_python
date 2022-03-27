def notas(*n, sit=False):
    '''
        -> função para analizar notas e situações de varios alunos
    :param n: uma ou mais notas do aluno (aceita varias notas)
    :param sit: valor opcional, indicando se deve ou não mostrar a situação
    :return: dicionario com varias informações sobre a situação da turma
    '''
    cont = maior = menor = soma = 0
    dicionario = {}
    for nota in n:
        cont = cont + 1
        soma = soma + nota
        if cont == 1:
            maior = menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
    dicionario['total'] = cont
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = cont / soma
    if sit == True:
        if dicionario['media'] < 5:
            dicionario['situação'] = 'Reprovado'
        elif dicionario['media'] >= 5 and dicionario['media'] <= 6.9:
            dicionario['situação'] = 'Recuperação'
        else:
            dicionario['situação'] = 'Aprovado'
    return dicionario


notas(2.5, 7.4, 3.5, 7, sit=True)
