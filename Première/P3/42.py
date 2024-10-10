lancer1 = int(input("Nombre de quilles tombées au lancer 1 :"))
if not 0<=lancer1<=10 :
    print("!")
else :
    if lancer1 == 10:
        print("X")
    else :
        lancer2 = int(input("Nombre de quilles tombées au lancer 2 :"))
        if not 0<=lancer2<=lancer1+lancer2<=10 :
            print("!")
        else:
            if lancer1+lancer2 == 10:
                print("/")
            else :
                print(lancer1+lancer2)
