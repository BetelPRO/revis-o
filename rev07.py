cont = 0
for i in range(1, 501):
    if i%2 == 1 and cont < 41:
        print(i, end=" ")
        cont +=1
    else:
        if i%2 == 1 and cont == 41:
            print(f"\n{i}", end=" ")
            cont = 0