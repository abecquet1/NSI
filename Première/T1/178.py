from random import randint, shuffle

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


# Test
print(occurrences("tagada"))

