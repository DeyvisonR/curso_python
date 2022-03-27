from random import randint


def sorteia(lst):
    for c in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
    print(f'sorteando 5 valores da lista: {lst}')


def Somapar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'somando os valores pares de {lst}, temos {soma}')

lista = []
sorteia(lista)
Somapar(lista)
