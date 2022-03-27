def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade >= 18 and idade < 65:
        return f'com {idade} anos: voto OBRIGATÓRIO'
    elif idade < 18:
        return f'com {idade} anos: não vota'
    elif idade > 65:
        return f'com {idade} anos: voto OPCIONAL'


anodenasc = int(input('em que ano você nasceu: '))
print(voto(anodenasc))
