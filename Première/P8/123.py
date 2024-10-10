from random import randint

# Un tableau de taille 64
t = [randint(10, 99) for k in range(64)]


# Il y a plein de réponses possibles

# En parcourant la grille...
m1 = [[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        m1[i][j] = t[8*i+j]

m2 = []
for i in range(8):
    ligne = []
    for j in range(8):
        ligne.append(t[8*i+j])
    m2.append(ligne)

m3 = [[t[8*i+j] for j in range(8)] for i in range(8)]

# Ou en parcourant le tableau...
m4 = [[0]*8 for i in range(8)]
for k in range(64):
    m4[k//8][k%8] = t[k]


# Tests
def afficher(g):
    for ligne in g:
        print(ligne)
    print()

print("Tableau de départ : ")
print(t)
print()

afficher(m1)
afficher(m2)
afficher(m3)
afficher(m4)
