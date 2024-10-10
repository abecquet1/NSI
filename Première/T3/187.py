def poids_commande(bon, pp):
    return sum([pp[e["ref"]]*e["qte"] for e in bon if e["qte"]>0])


def articles_lourds(bon, pp):
    return [e for e in bon if pp[e["ref"]]>200]

#test

bon = [
    {"ref":"a", "qte":-5, "prix":1.5},
    {"ref":"b", "qte":1, "prix":2.5},
    {"ref":"c", "qte":2, "prix":4.2},
    {"ref":"d", "qte":3, "prix":1.3},
    {"ref":"e", "qte":2, "prix":5.1},
    {"ref":"f", "qte":1, "prix":12.5},
    {"ref":"g", "qte":1, "prix":0.5}
    ]

poids_produits = {
    "a":0.2,
    "b":0.1,
    "c":0.3,
    "d":0.4,
    "e":0.1,
    "f":300,
    "g":500,
    }

print(poids_commande(bon, poids_produits))
print(articles_lourds(bon, poids_produits))


