from os import system
import _5numeros
import maiormenor
import pares
import range_

def main():
    print(f"[0] sair\t[1] 5 numeros\t[2] maior menor\t[3] pares\t[4] range")
    r = input("--->")
    if r == "1":
        _5numeros.main()
    elif r == "2":
        maiormenor.main()
    elif r == "3":
        pares.main()
    elif r == "4":
        range_.main()
    elif r == "0":
        return 0
    else:
        system("pause")
        main()
    main()
main()
