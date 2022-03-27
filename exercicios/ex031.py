distancia = int(input('qual a distância da sua viagem em km?: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('você esta preste a iniciar uma viagem de {}Km.'.format(distancia))
print('e o preço de sua viagem sera de {}'.format(valor))