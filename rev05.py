salMin = float(input("Informe o salário mínimo: "))
salUsu = float(input("Informe o seu salário: "))
while salUsu != 0:
    quant = salUsu/salMin
    print(f"Você ganhha {quant:.2f} salários mínimos\n")
    salUsu = float(input("Informe o seu salário: "))
print("Programa encerrado")