eleves = [
    {"nom":"Toto", "annee":2004, "mois":11, "jour":3},
    {"nom":"Titi", "annee":2003, "mois":2, "jour":4},
    {"nom":"Tutu", "annee":2004, "mois":11, "jour":2},
    {"nom":"Tata", "annee":2005, "mois":2, "jour":29}
    ]

print(sorted(eleves,key = lambda x: x["nom"], reverse = True))
