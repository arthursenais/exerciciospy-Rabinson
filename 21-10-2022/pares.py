def main():
    im = 0 #armazenar quantidade de numeros impares
    pa = 0 #armazenar quantidade de numeros pares
    im_lista = [] #lista usada para armazenar os numeros impares
    pa_lista = [] #lista usada para armazenar os numeros pares
    for numeros in range(10):
        n = int(input("-->")) 
        if n%2 == 0:
            print('par'); pa += 1; pa_lista.append(n)
        else:
            print('impar'); im+=1; im_lista.append(n)
    print(f"quantidade de numeros pares: {pa} --> {pa_lista}")
    print(f"quantidade de numeros impares: {im} --> {im_lista}")