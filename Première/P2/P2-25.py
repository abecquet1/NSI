s = float(input("Somme initiale : "))
t = float(input("Taux d'intérêt (en pourcentage) : "))
n = int(input("Nombre d'années : "))

for i in range(1, n+1):
    interets = s*t/100
    print("Intérêts gagnés à l'année", i, ":", interets)
    s = s+interets

print("Somme finale :", s)
