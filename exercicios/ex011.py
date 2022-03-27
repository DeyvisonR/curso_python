largura = float(input('digite a largura da parede: '))
altura = float(input('digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m2')
print('para pintar essa parede, você precisara de {}l de tinta'.format(tinta))