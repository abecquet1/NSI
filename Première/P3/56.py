from turtle import *

n = int(input("côté du damier ?"))
speed(0)

for ligne in range(n):
    # traitement d'une ligne

    blanc = (ligne%2 == 0)
    # blanc est un booléen (True ou False) disant si la case est blanche
    # on décide que les lignes pairs commencent par une case blanche
    for case in range(n):
        #traitement d'une case

        # couleur de remplissage
        if blanc:
            fillcolor("white")
        else:
            fillcolor("black")

        # le carré
        begin_fill()
        for i in range(4):
            forward(10)
            left(90)
        end_fill()

        # on se place pour la case suivante
        forward(10)

        # la case suivante a une couleur différence
        blanc = not blanc

    # on se place pour la ligne suivante
    backward(10*n)
    left(90)
    forward(10)
    right(90)
