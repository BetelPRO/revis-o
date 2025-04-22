valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))

somAB = valorA + valorB
if somAB > valorC:
    print("Não, a soma de A + B é maior que o C")
elif somAB == valorC:
    print("Eles são iguais")
else:
    print("SIM, o valor de C é maior que a soma de A e B")