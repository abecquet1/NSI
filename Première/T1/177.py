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

def compare_tableaux(t1, t2):
    return occurrences(t1) == occurrences(t2)

# Test

t1 = [randint(1,100) for i in range(50)]
t2 = t1.copy()  # Génère une copie indépendante de t1
shuffle(t2)     # Mélange les éléments de t2

t3 = [randint(1,100) for i in range(50)]
t4 = t1[0:-1]   # Copie de t1 sans sa dernière case

print(compare_tableaux(t1, t2))
print(compare_tableaux(t1, t3))
print(compare_tableaux(t1, t4))



