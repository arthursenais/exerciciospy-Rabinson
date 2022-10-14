from os import *
while True:
    def dsemana(m):
        if m == '1':
            print('domingo')
        elif m == '2':
            print('segunda')
        elif m == '3':
            print('terça')
        elif m == '4':
            print('quarta')
        elif m == '5':
            print('quinta')
        elif m == '6':
            print('sexta')
        elif m == '7':
            print('sábado')
        else:
            print("invalido")
    m = input("--> ")
    dsemana(m)