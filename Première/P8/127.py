from random import randint

def maximin(g):
    # On commence par calculer le min de chaque ligne (dans t_min)
    t_min = []
    for ligne in g:
        v_min = ligne[0]
        for v in ligne:
            if v < v_min:
                v_min = v
        t_min.append(v_min)

    # Puis on calcule le plus grand de ces minima
    v_max = t_min[0]
    for v in t_min:
        if v > v_max:
            v_max = v
    return v_max


# Test
def afficher(g):
    for ligne in g:
        print(ligne, "-> v_min =", min(ligne))
    print()

g = [[randint(10,99) for j in range(10)] for i in range(10)]

afficher(g)

print("Le maximin :", maximin(g))