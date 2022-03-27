def maior(* num):
    cont = 0
    for valor in num:
        cont = cont + 1
        if cont == 1:
            maiore = valor
        else:
            if valor > maiore:
                maiore = valor
    print(f'analizando os valores passados.....')
    print(f'{num} foram informados {len(num)} ao todo.')
    print(f'o maior valor informado foi {maiore}')


maior(9, 74, 20, 13, 17)
