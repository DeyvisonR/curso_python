from time import sleep
print("-=" * 20)
print("{:=^50}".format("\033[1;30mTermos de uma PA\033[m"))
print("-=" * 20)
p1 = int(input("\033[1;35mPrimeiro Termo:\033[m "))
r = int(input("\033[1;34mRazao da PA:\033[m "))
a1 =[]
a1.append(p1)
fim = False
count = 0
print("\n\033[1;4;36m10 Primeiros termos da PA:\033[m")
for c in range(1,11):
    print(f"\033[30m{a1[c-1]} ->",end=" ")
    a1.append(a1[c-1] + r)
    count+=1
print("PAUSA\033[m")
sleep(0.5)
while not fim:
    op = str(input(f"""
\033[1;33m===========================
[ 1 ] + 10 Termos Desta PA
[ 2 ] + x Termos Desta PA
[ 3 ] Trocar o primeiro termo e a razão
[ 4 ] Achar Termo Desta PA ex: (a11= {a1[10]})
[ 5 ] Limpar Termos
[ 0 ] Sair do programa

\033[1;35mPrimeiro Termo = \033[m \033[1;30m{p1}\033[m
\033[1;34mRazão =\033[m \033[1;30m{r}\033[m
\033[1;36mTermos mostrados = \033[1;30m{count}\033[m
\033[1;33m===========================\033[m 
\033[1;32m>>>> Opção:\033[m """)).strip()
    if op == '1':
        for x in range(1,11):
            count += 1
            print(f"{a1[count-1]} ->",end=" ")
            a1.append(a1[count-1] + r)
        print("PAUSA")
        sleep(0.5)
    elif op == '2':
        qtd = int(input("Quantos termos mais voce quer? "))
        print("\nProgressão Aritimetrica: ")
        for x in range(1,qtd+1):
            count += 1
            print(f"{a1[count -1]} ->",end=" ")
            a1.append(a1[count - 1] + r)
        print("PAUSA")
        sleep(0.5)
    elif op =='3':
        p1 = int(input("\033[1;35mPrimeiro Termo:\033[m "))
        a1 = []
        a1.append(p1)
        r = int(input("\033[1;34mRazão da PA:\033[m "))
        count = 0
        for x in range(1,11):
            count+=1
            print(f"{a1[count -1]} ->",end=" ")
            a1.append(a1[count-1]+r)
        print("PAUSA")
        sleep(0.5)
    elif op == '4':
        loc = int(input("Qual termo que voce quer encontrar ?"))
        if loc <= count:
            print(f"O termo \033[1;31ma{loc} = {a1[loc-1]}\033[m")
            sleep(0.5)
        else:
            dif = loc - count
            for x in range(1, dif+1):
                count += 1
                a1.append(a1[count - 1] + r)
            print(f"O termo \033[1;31ma{loc} = {a1[loc-1]}\033[m")
            sleep(0.5)
    elif op =='5':
        a1=[]
        a1.append(p1)
        count = 0
        for x in range(1, 11):
            count += 1
            print(f"{a1[count - 1]} ->", end=" ")
            a1.append(a1[count - 1] + r)
        print("PAUSA")
        sleep(0.5)
    elif op == '0':
        fim = True
    else:
        print("Opção Invalida. Digite outra opção")
        sleep(0.5)
print(f"\033[1;4;31mFIM DO PROGRAMA. Ao total {count} Termos foram mostrados\033[m")
