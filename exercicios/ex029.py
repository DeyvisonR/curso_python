vkm = int(input('qual e a velocidade atual do carro em KM: '))
multa = (vkm - 80) * 7.00
if vkm >= 81:
    print('\033[31mMUTADO! você exedeu o limite permitido que é de 80Km/h')
    print('você deve pagar uma multa de {:.2f}'.format(multa))
print('\033[32mtenha um bom dia! dirija com segurança!')
