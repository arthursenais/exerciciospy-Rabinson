def main():
    def funcao():
        l = []
        i = 0
        soma = 0
        for n in range(20):
            i = int(input("--->"))
            if i >1000:
                print("invalido")
                return
            elif i < 0:
                print("invalido")
                return
            else:
                soma = soma + i
                l.append(i)
        print(l)
        print(f"o maior numero: {max(l)}")
        print(f"o menor numero: {min(l)}")
        print(f"soma = {soma}")
        repetir = input("repetir [y]")
        if repetir == "y":
            funcao()