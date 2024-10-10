def tri_insertion(t, key = lambda x : x):
    """tri par insertion, j'ai rajouté la possibilité de préciser la clé de tri (par défaut l'identité)"""
    for i in range(len(t)):
        j = i
        x = t[i]
        while j>=1 and key(t[j-1])>key(x):
            t[j]=t[j-1]
            j = j-1
        t[j] = x


# supposons que deux cases c1 < c2 (à lire c1 avant c2) de t aient la même valeur
# le tri commence par insérer c1, on a toujours c1 < c2
# le tri insère c2 et puisque les deux cases ont la même valeur
# la boucle while s'arrete (t[j-1]>x) au pire dès que l'indice j-1 correspond à c2
# on insère donc au pire c2 juste après c1 on a donc toujour c1<c2
# le reste des insertion ne change pas l'ordre relatif des cases


# petit test pour observer la stabilité  

t = [(i, "rouge") for i in range(3)] + [(i, "bleu") for i in range(3)]
print(t)

tri_insertion(t, key = lambda x:x[0])
print(t)
