# Par modification de cases
g1 = [[0]*11 for i in range(11)]
for i in range(11):
    for j in range(11):
        g1[i][j] = i*j

# Par ajout de lignes
g2 = []
for i in range(11):
    ligne = []
    for j in range(11):
        ligne.append(i*j)
    g2.append(ligne)

# Par compréhention
g3 = [[i*j for j in range(11)] for i in range(11)]

# Affichage
for i in range(11):
    print("Table de", i, ":")
    for j in range(11):
        print("   ", i, "x", j, "=", g3[i][j])  # On peut mettre g1, g2 ou g3 ici
    print()