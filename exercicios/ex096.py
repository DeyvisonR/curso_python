def calculararea(a, b):
    area = a * b
    print(f'a area de um terreno {a}x{b} e de {area}m²')


a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
calculararea(a, b)
