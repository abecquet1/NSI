from math import sqrt

print("Résolution de l'équation ax^2+bx+c = 0 : ")
a = float(input("    a ? "))
b = float(input("    b ? "))
c = float(input("    c ? "))

if a == 0:
    if b == 0:
        # équation dégénérée (sans variable) :  c = 0
        if c == 0:
            print("-> L'ensemble solution est R.")
        else:
            print("-> Pas de solution.")

    else:
        # équation de degré 1
        print("-> Une seule solution :", -c/b)

else:
    # équation de degré 2
    delta = b**2-4*a*c

    if delta < 0:
        print("-> Pas de solution.")

    elif delta == 0:
        print("-> Une seule solution :", -b/(2*a))

    else:
        print("-> Deux solutions :")
        print("   ", (-b-sqrt(delta))/(2*a))
        print("   ", (-b+sqrt(delta))/(2*a))

