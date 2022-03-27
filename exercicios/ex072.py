numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')
continuar = 's'
while continuar == 's':
    n = int(input('digite um número de 0 a 20: '))
    if n < 0 or n > 20:
        print('\033[31mnumero invalido.\033[m tente novamente')
        print('=' * 30)
    else:
        print(f'você digitou o número {numeros[n]}')
        print('=' * 30)
        continuar = ' '
        while continuar not in 'sn':
            continuar = str(input('você quer ver outro valor por extenso [S/N]: ')).strip().lower()[0]
            if continuar not in 'sn':
                print('digito invalido. tente novamente')
            print('=' * 30)
