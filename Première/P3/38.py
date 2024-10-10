n = int(input("Entrer un entier pour connaître ses diviseurs :"))
compteur = 0
for d in range(1,n+1):
    if n%d==0:
        print(d, "divise", n)
        compteur = compteur +1
if compteur == 2:
    print(n, "est un nombre premier")
