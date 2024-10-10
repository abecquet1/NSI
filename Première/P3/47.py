k = int(input("nombre de lettres ? "))

compteur_0 = 0
compteur_1 = 0

for i in range(k):
    print("lettre n°", i, " (0 ou 1) : ", end = "")
    lettre = input()

    if lettre == "0":
        compteur_0 += 1
    else:
        compteur_1 += 1

if compteur_1>compteur_0:
    print('1')
elif compteur_1<compteur_0:
    print('0')
else:
    print('X')


