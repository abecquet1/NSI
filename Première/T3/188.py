def verifie_commande(bon, tarifs):
    for e in bon:
        if e["prix"] != tarifs[e["ref"]]:
            return False
    return True

def cherche_erreur(bon, tarifs):
    return [{"ref":e["ref"], "prix_bon":e["prix"], "prix_tarif":tarifs[e["ref"]]} for e in bon if e["prix"] != tarifs[e["ref"]]]

#test

bon = [
    {"ref":"b", "qte":1, "prix":2.5},
    {"ref":"c", "qte":2, "prix":4.2},
    {"ref":"d", "qte":3, "prix":1.3},
    {"ref":"e", "qte":2, "prix":5.1},
    {"ref":"f", "qte":1, "prix":12.5},
    {"ref":"g", "qte":1, "prix":0.5}
    ]

tarifs = {
    "b": 2.5,
    "c": 4.2,
    "d": 1.4,
    "e": 5.1,
    "f": 2.5,
    "g": 0.6 
}


print(verifie_commande(bon, tarifs))
print(cherche_erreur(bon, tarifs))



