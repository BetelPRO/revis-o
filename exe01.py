num = int(input("Digite um número: "))
for x in range(1, num+1):
    for y in range(0, x):
        print(x, end=" ")
    print()
for x in range(num-1, 0, -1):
    for y in range(x, 0, -1):
        print(x, end=" ")
    print()