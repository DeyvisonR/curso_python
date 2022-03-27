import random
al1 = str(input('primeiro aluno: '))
al2 = str(input('segundo aluno: '))
al3 = str(input('terceiro aluno: '))
al4 = str(input('quarto aluno: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('o aluno sorteado foi: {}'.format(escolhido))
