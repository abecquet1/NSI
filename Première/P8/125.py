from random import randint

g = [[randint(1,9999) for j in range(30)] for i in range(30)]

# Test
def afficher(g):
    for ligne in g:
        print(ligne)
    print()

afficher(g)