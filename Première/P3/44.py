print("Donner les trois côtés d'un triangle, du plus petit au plus grand :")

a = float(input("    Côté 1 ? "))
b = float(input("    Côté 2 ? "))
c = float(input("    Côté 3 ? "))

possible = (c<a+b)
equilateral = (a==b==c)
isocele = (a==b or b==c or c==a)
rectangle = (c**2==a**2+b**2)

if possible:
    if equilateral:
        print("Triangle équilatéral.")
    elif isocele and rectangle :
        print("Triangle isocèle rectangle.")
    elif isocele:
        print("Triangle isocèle.")
    elif rectangle:
        print("Triangle rectangle.")
    else:
        print("Triangle scalène.")
else:
    print("Triangle impossible !")
