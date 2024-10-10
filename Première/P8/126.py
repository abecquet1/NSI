from random import randint

g = [[randint(1,9999) for j in range(30)] for i in range(30)]

v_max = g[0][0]
for i in range(30):
    for j in range(30):
        if g[i][j] > v_max:
            v_max = g[i][j]

# Test
def afficher(g):
    for ligne in g:
        print(ligne)
    print()

afficher(g)
print("Valeur maximale :", v_max)