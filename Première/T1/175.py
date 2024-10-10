# Tableau de n-uplets nommés
eleves = [
    {"nom" : "tata", "mois" : 1},
    {"nom" : "titi", "mois" : 12},
    {"nom" : "tutu", "mois" : 3},
    {"nom" : "tete", "mois" : 4},
    {"nom" : "toto", "mois" : 10}
]

# Programme
t = [0]*13  # une case par mois de 1 à 12 (0 non utilisé)
for eleve in eleves:
    m = eleve["mois"]
    t[m] += 1