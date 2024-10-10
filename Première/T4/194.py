def afficher_table(table):
    for e in table:
        print(e)

eleves = [
    {"nom": "Tata", "annee" : 2004, "jour": 12, "mois" :1 },
    {"nom": "Titi", "annee" : 2005, "jour": 13, "mois" :2 },
    {"nom": "Tutu", "annee" : 2004, "jour": 15, "mois" :2 },
    {"nom": "Tete", "annee" : 2003, "jour": 1, "mois" :3 },
    {"nom": "Toto", "annee" : 2001, "jour": 30, "mois" :7 },
    ]


tri1 = sorted(eleves, key = lambda e: e["mois"])
tri2 = sorted(eleves, key = lambda e: (e["mois"], e["jour"]))
tri3 = sorted(eleves, key = lambda e: (e["annee"], e["mois"], e["jour"]))

afficher_table(tri1)
print()
afficher_table(tri2)
print()
afficher_table(tri3)
