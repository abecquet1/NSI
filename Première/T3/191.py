def surface_sup(s, registre):
    return [e for e in registre if e["surface"]>=s]

def prix_inf(p, registre):
    return [e for e in registre if e["prix"]<=p]

def surface_sup_prix_inf(s,p, registre):
    return [e for e in registre if e["prix"]<=p and e["surface"]>=s]


#test

registre = [
    {"lat":48.6938 , "long":6.1893, "surface":91 , "prix": 169000},
    {"lat":48.6907 , "long":6.1809, "surface":19 , "prix": 55000},
    {"lat":48.6955 , "long":6.1811, "surface":75 , "prix": 176000},
    {"lat":48.6822 , "long":6.1901, "surface":65 , "prix": 99000},
    {"lat":48.7001 , "long":6.1799, "surface":72 , "prix": 130000},
]

print(surface_sup(50, registre))
print(surface_sup(70, registre))
print(prix_inf(150000, registre))
print(prix_inf(100000, registre))
print(surface_sup_prix_inf(60, 100000, registre))

