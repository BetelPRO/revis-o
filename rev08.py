i, cont = 1, 0
while i != 500:
    if i%2==1 and cont<41:
        print(i, end=" ")
        cont += 1
    else:
        if i%2==1 and cont == 41:
            print(f"\n{i}", end=" ")
            cont = 0
    i += 1