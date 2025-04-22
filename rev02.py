condict = "s"

while condict == "s":
    num = float(input("Digite qualquer número: "))

    if num%2 == 1:
        if num < 0:
            print("O número é Ímpar e Negativo")
        else:
            print("O número é Ímpar e Positivo")
    else:
        if num < 0:
            print("O número é Par e Negativo")
        else:
            print("O número é Par e Positivo")

    condict = input("Digite s para continuar ou outro caracter para parar: ")
