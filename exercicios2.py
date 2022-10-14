import sys
from os import *
while True:
    def f3(m):
        if m == 'M':
            print("Bom Dia")
        elif m == 'V':
            print("Boa Tarde")
        elif m == 'N':
            print("Boa Noite")
        elif m == '0':
            system("cls")
            sys.exit()
        else:
            print("Valor inválido")
    m = input("--> ").upper()
    f3(m)