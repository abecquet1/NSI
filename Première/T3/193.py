def plus_proche(x, y, registre):
    e_min = registre[0]
    carre_min = (e_min["lat"]-x)**2+(e_min["long"]-y)**2
    for e in registre[1:]:
        carre = (e["lat"]-x)**2+(e["long"]-y)**2
        if carre < carre_min:
            carre_min = carre
            e_min = e
    return e_min

def dans_un_rayon_de(r,x,y,registre):
    return [e for e in registre if (e["lat"]-x)**2+(e["long"]-y)**2 <= r**2]

def prix_carre_dans_un_rayon_de(r,x,y,registre):
    return [{"lat":e["lat"], "long":e["long"], "ppm2":e["prix"]/e["surface"]} for e in registre if (e["lat"]-x)**2+(e["long"]-y)**2 <= r**2]



#test

registre = [
    {"lat":48.6938 , "long":6.1893, "surface":91 , "prix": 169000},
    {"lat":48.6907 , "long":6.1809, "surface":19 , "prix": 55000},
    {"lat":48.6955 , "long":6.1811, "surface":75 , "prix": 176000},
    {"lat":48.6822 , "long":6.1901, "surface":65 , "prix": 99000},
    {"lat":48.7001 , "long":6.1799, "surface":72 , "prix": 130000},
]


print(plus_proche(49,6.18,registre))
print(dans_un_rayon_de(10, 48, 6.2, registre))
print(prix_carre_dans_un_rayon_de(0.69, 48, 6.2, registre))
print(prix_carre_dans_un_rayon_de(0.7, 48, 6.2, registre))
