def purge_commande(bon):
    return [e for e in bon if e["qte"]>0]

def prix(bon):
    bp = purge_commande(bon)
    return sum([e["prix"]*e["qte"] for e in bp])



#test

bon = [
    {"qte":-5, "prix":1.5},
    {"qte":1, "prix":2.5},
    {"qte":2, "prix":4.2},
    {"qte":3, "prix":1.3},
    {"qte":2, "prix":5.1},
    {"qte":1, "prix":12.5},
    {"qte":10, "prix":0.5}
    ]

print(purge_commande(bon))
print(prix(bon))
