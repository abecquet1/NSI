#fonctions

def verifie_quantites(bon):
    for e in bon:
        if e["qte"] < 0:
            return False
    return True

def nombre_produit(bon):
    total = 0
    for e in bon:
        if e["qte"]>0:
            total+=e["qte"]
    return total

#test


bon = [
    {"qte":-5},
    {"qte":1},
    {"qte":2},
    {"qte":3},
    {"qte":2},
    {"qte":1},
    {"qte":10}
    ]

print(verifie_quantites(bon))
print(verifie_quantites(bon[1:]))
print(nombre_produit(bon))
