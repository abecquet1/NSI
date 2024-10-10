# Fonctions

def occurrences(t):
    """Renvoie le dictionnaire des occurences de t."""
    d = {}
    for x in t:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

def plus_frequent(d, k):
    """Renvoie la clé de k lettres de d ayant la plus grande valeur."""
    s_max = ""
    v_max = 0
    for s in d:
        if len(s) == k and d[s]>v_max:
            s_max = s
            v_max = d[s]
    return s_max


# Test

t = ["à", "un", "de", "de", "un", "un", "coucou", "salut"]
d = occurrences(t)

for k in range(1,7):
    print("k =", k, "plus freq =", plus_frequent(d, k))
