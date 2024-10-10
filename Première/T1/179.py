from random import choice
import math
# Fonctions

def inverse_clavier(clavier):
    """Renvoie un dictionnaire qui à chaque touche du clavier associe ses coordonnées."""
    inv = {}
    for i in range(len(clavier)):
        for j in range(len(clavier[i])):
            touche = clavier[i][j]
            inv[touche] = (i, j)
    return inv

def distance_touches(touche1, touche2, clavier):
    """Renvoie la distance entre deux touches du clavier."""
    inv = inverse_clavier(clavier)
    i1, j1 = inv[touche1]
    i2, j2 = inv[touche2]
    return math.sqrt((i2-i1)**2+(j2-j1)**2)

# Tests

azerty = [['a','z','e','r','t','y','u','i','o','p'],
          ['q','s','d','f','g','h','j','k','l','m'],
          ['<','w','x','c','v','b','n',',',';',':']]

for i in range(10):
    touche1 = choice(choice(azerty))
    touche2 = choice(choice(azerty))
    print("distance azerty entre", touche1, "et", touche2, ":", distance_touches(touche1, touche2, azerty))

