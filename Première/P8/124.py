from random import randint

# Une grille 8x8
m = [[randint(10, 99) for j in range(8)] for i in range(8)]

t = []
for i in range(8):
    for j in range(8):
        t.append(m[i][j])

# Test
def afficher(g):
    for ligne in g:
        print(ligne)
    print()

afficher(m)
print(t)

