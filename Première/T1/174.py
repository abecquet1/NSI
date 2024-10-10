from random import randint

# Focntions

def doublon(t):
    """Teste si t admet des doublons."""
    s = set()
    for x in t:
        s.add(x)
    return len(s) != len(t)

def genere_groupe(n = 23, nb_jours = 365):
    """Génère un tableau de n dates (entre 1 et nb_jours)."""
    return [randint(1, nb_jours) for i in range(n)]

# Programme

compteur = 0
for i in range(1000):
    groupe = genere_groupe()
    if doublon(groupe):
        compteur += 1
print("Sur 1000 groupes aléatoires,", compteur, "comportent des doublons")

