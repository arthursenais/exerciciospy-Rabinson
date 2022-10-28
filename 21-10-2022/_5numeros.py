def main():
    numeros = []
    soma = 0
    print("digite 5 numeros:")
    for n in range(5):
        numero = int(input("--->"))
        soma = soma + numero
        numeros.append(numero)
    print("-------------------------")
    print(*numeros, sep=" + ", end=f" = {soma}\n")
    print(f"{soma} / 5 = {soma / 5}")