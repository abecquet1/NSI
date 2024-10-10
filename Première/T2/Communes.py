import csv

f = open("Communes.csv", "r")
table = list(csv.DictReader(f, delimiter=';'))
f.close()



print("Attributs :", end = " ")
for k in table[0]:
    print(k, end = ", ")
print()

print("Nombre de villes :", len(table))

print("Villes de plus de 10000 habitants :")

for v in table:
    if int(v["PTOT"])>=100000:
        print(v["COM"])



