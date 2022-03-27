n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
if n1 >= n2 and n1 >= n3:
    maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
    # verificando quem e o maior
if n1 <= n2 and n1 <= n3:
    menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3
    # verificando quem e o menor
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))
