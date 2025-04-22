peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/(altura*altura)
if imc < 18.6:
    print("Abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("Peso Ideal (Parabéns)")
elif 25 <= imc <= 29.9:
    print("Levemente acima do peso")
elif 30 <= imc <= 34.9:
    print("Obesidade grau 1")
elif 35 <= imc <= 39.9:
    print("Obesidade grau 2 (Severa)")
else:
    print("Obesidade grau 3 (Mórbida)")