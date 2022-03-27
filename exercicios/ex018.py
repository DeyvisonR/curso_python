import math
angulo = float(input('digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o ângulo de {} tem o seno de: {:.2f}'.format(angulo, seno))
print('o ângulo de {} tem o coseno de: {:.2f}'.format(angulo, coseno))
print('o ângulo de {} tem a tangente de: {:.2f}'.format(angulo, tangente))
