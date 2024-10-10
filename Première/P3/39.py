score = int(input("Entrer le score :"))
gain = int(input("entrer le gain :"))
nb_zero = int(input("nombre zéros déjà fait par le joueur :"))

nouveau_score = score+gain 


if score == 0:
    nb_zero = nb_zero+1

if nb_zero >=3:
    print("Perdu !")

else:   
    if nouveau_score < 51:
        print("Nouveau score :", nouveau_score)
    elif nouveau_score == 51:
        print("Gagne !")
    else:
        nouveau_score = 25
        print("Trop grand ! Nouveau score : 25")
    
print("Fin du tour")
