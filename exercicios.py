import os
import string
import sys
os.system('cls')
menu = '1'
while menu != '0':
    def f1(p1,p2,p3):
        if min(p1,p2,p3) == 1:
            print(f"Você deve escolher o produto de {min(p1,p2,p3)} real")
        else:
            print(f"Você deve escolher o produto de {min(p1,p2,p3)} reais")
    def f2(p1,p2,p3):
        x = [p1,p2,p3]
        print(*sorted(x,reverse=True),sep=', ')
    def f3(m):
        if m == 'M':
            print("Bom Dia")
        elif m == 'V':
            print("Boa Tarde")
        elif m == 'N':
            print("Boa Noite")
        else:
            print("Valor inválido")
    os.system('cls')
    p1 = float(input("Preço do produto1: "))
    p2 = float(input("Preço do produto2: "))
    p3 = float(input("Preço do produto3: "))
    f1(p1,p2,p3)
    print("\nOrdem decrescente dos números escolhidos: ")
    f2(p1,p2,p3)
    m = input("Digite o turno: ").upper()
    f3(m)
    menu = string(input("\n1 para continuar, 0 para sair: "))
    os.system('cls')
sys.exit("saindo...")