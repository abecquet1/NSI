def prix_m2_max(registre):
    return max([e["prix"]/e["surface"] for e in registre])

def prix_moyen(registre):
    return sum([e["prix"] for e in registre])/len(registre)

def prix_moyen_familial(registre):
    return sum([e["prix"] for e in registre if 70<=e["surface"]<=100])/len(registre)


#test

registre = [
    {"lat":48.6938 , "long":6.1893, "surface":91 , "prix": 169000},
    {"lat":48.6907 , "long":6.1809, "surface":19 , "prix": 55000},
    {"lat":48.6955 , "long":6.1811, "surface":75 , "prix": 176000},
    {"lat":48.6822 , "long":6.1901, "surface":65 , "prix": 99000},
    {"lat":48.7001 , "long":6.1799, "surface":72 , "prix": 130000},
]

print(prix_m2_max(registre))
print(prix_moyen(registre))
print(prix_moyen_familial(registre))
