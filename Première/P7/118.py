# Fonctions

def recherche(x, t):
    for i in range(len(t)):
        if t[i] == x:
            return True
    return False

def inclus1(t1, t2):
    for i in range(len(t1)):
        if not recherche(t1[i], t2):
            return False
    return True

def inclus2(t1, t2):
    for i in range(len(t1)):
        dedans = False
        for j in range(len(t2)):
            if t1[i] == t2[j]:
                dedans = True
        if not dedans:
            return False
    return True

# Test

t1 = [1,2,3]
t2 = [1,2,2,3,4,0]

print(inclus1(t1, t2))
print(inclus1(t2, t1))
print(inclus2(t1, t2))
print(inclus2(t2, t1))



