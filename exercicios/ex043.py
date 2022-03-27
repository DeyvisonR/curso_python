peso = float(input('qual e se peso: '))
altura = float(input('qual e sua altura: '))
imc = peso / (altura * altura)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('você esta abaixo do peso')
elif imc >= 18.5:
    print('você esta no peso ideal')
elif imc < 30:
    print('você esta no sobrepeso')
elif imc < 40:
    print('você esta na obesidade')
else:
    print('você esta na obesidade mórbida')
