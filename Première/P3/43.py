print("Donner les trois côtés d'un triangle, du plus petit au plus grand :")

a = float(input("    Côté 1 ? "))
b = float(input("    Côté 2 ? "))
c = float(input("    Côté 3 ? "))

if c < a+b :
    if a==b or b==c or c==a:
        if a==b==c:
            print("Triangle équilatéral.")
        else:
            print("Triangle isocèle.")
    else:
        print("Triangle scalène.")
else:
    print("Triangle impossible !")
