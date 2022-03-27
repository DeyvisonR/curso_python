num = ()
num2 = ()
temp = ()
exita = ''
while True:
    print('''voce quer calcular a temperatura de:
[ 1 ] CELSIUS
[ 2 ] FAHRENHEINT
[ 3 ] KELVIN''')
    num = int(input('R: '))
    num2 = int(input('para: '))
    temp = float(input('digite a temperatura: '))
    cparaf = ((temp * 9) / 5) + 32
    cparak = (temp + 273.15)
    fparac = ((temp - 32) * 5) / 9
    fparak = (((temp - 32) * 5) / 9) + 273.15
    kparac = temp - 273.15
    kparaf = (((temp - 273.15) * 9) / 5) + 32
    if num == (1) and num2 == (2):
        print('a temperatura de {}C° e igual a {}F°!'.format(temp, cparaf))
    elif num == (1) and num2 == (3):
        print('a temperatura de {}C° e igual a {}K!'.format(temp, cparak))
    elif num == (2) and num2 == (1):
        print('a temperatura de {}F° e igual a {}C°!'.format(temp, fparac))
    elif num == (2) and num2 == (3):
        print('a temperatura de {}F° e igual a {}K!'.format(temp, fparak))
    elif num == (3) and num2 == (1):
        print('a temperatura de {}K e igual a {}C°!'.format(temp, kparac))
    elif num == (3) and num2 == (2):
        print('a temperatura de {}K e igual a {}F°!'.format(temp, kparaf))
    elif num >= (4) or num2 >= (4):
        print('não tem essa opção, por favor digite um número valido. thanks!!!')
    elif num == num2:
        print('não há oque converter ;-;')
    exita = input(str('voce deseja encerrar o programa? (S/N): ')).strip().upper()
    if exita == 'S':
        exit()
