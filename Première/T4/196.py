def sac_poids(table, p_max):
    triee = sorted(table, key = lambda objet: objet["poids"])
    p = 0
    res = []
    for objet in table:
        if p + objet["poids"] <= p_max:
            res.append(objet)
    return res

def sac_valeur(table, p_max):
    triee = sorted(table, key = lambda objet: objet["valeur"], reverse = True)
    p = 0
    res = []
    for objet in table:
        if p + objet["poids"] <= p_max:
            res.append(objet)
    return res


def sac_valeur(table, p_max):
    triee = sorted(table, key = lambda objet: objet["valeur"]/objet["poids"], reverse = True)
    p = 0
    res = []
    for objet in table:
        if p + objet["poids"] <= p_max:
            res.append(objet)
    return res
