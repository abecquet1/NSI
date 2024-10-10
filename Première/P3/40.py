lancer1 = int(input("Nombre de quilles tombées au lancer 1 :"))
lancer2 = int(input("Nombre de quilles tombées au lancer 2 :"))

if lancer1 == 10:
    print("X")
elif lancer1+lancer2 == 10:
    print("/")
else :
    print(lancer1+lancer2)
