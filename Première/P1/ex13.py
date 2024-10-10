
#s = int(input("Nombre de secondes ? "))
s = 123

m = s//60   #nombre de paquets de 60  faisables avec s
s = s%60    #ce qu'il reste

h = m//60
m = m%60    #idem

print(h, "heures", m, "minutes", s, "secondes")
