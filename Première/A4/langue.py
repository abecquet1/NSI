from random import choice

def hamming(s1, s2):
    score = 0
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i]:
            score += 1
    score += abs(len(s1)-len(s2))
    return score


def liv(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    t = [[0]*(n2+1) for _ in range(n1+1)]
    for i in range(n1+1):
        t[i][0] = i
    for j in range(n2+1):
        t[0][j] = j
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] = t[i-1][j-1]
            else:
                t[i][j] = 1+min(t[i-1][j], t[i][j-1], t[i-1][j-1])
    return t[n1][n2]







f = open("francais.txt", "r")
francais = [s[:-1].lower() for s in f.readlines()]
f.close()

f = open("anglais.txt", "r")
anglais = [s[:-1].lower() for s in f.readlines()]
f.close()




c = {}
while len(c)<1000:
    fr = choice(francais)
    c[fr] = 'F'
    an = choice(anglais)
    c[an] = 'A'

T = list(c)
d = liv


def knn (T , e , k , d) :
    t = sorted(T, key = lambda elt : d(e,elt))
    return t [0: k]


def classe_plus_frequente (t , c):
    occ = {}
    for e in t:
        if c[e] in occ:
            occ[c[e]]+=1
        else:
            occ[c[e]] = 1
    c_max = c[t[0]]
    occ_max = occ[c_max]
    for classe in occ:
        if occ[classe]>occ_max:
            c_max = classe
            occ_max = occ[classe]
    return c_max

def prediction_knn (T , c , e , k , d):
    t = knn (T , e , k , d)
    return classe_plus_frequente (t , c)



"""
score_max = 0
while score_max<15:

    c = {}
    while len(c)<1000:
        fr = choice(francais)
        c[fr] = 'F'
        an = choice(anglais)
        c[an] = 'A'

    T = list(c)
    test = T[:20]
    T2 = T[20:]

    print("Validation croisée")
    k = 1
    score_max = sum([1 for e in test if c[e] == prediction_knn(T2, c, e, 1, d)])
    print("\tscore pour k =", 1, ":", score_max)
    for i in range(2, 16):
        score = sum([1 for e in test if c[e] == prediction_knn(T2, c, e, i, d)])
        if score>=score_max:
            score_max = score
            k = i
        print("\tscore pour k =", i, ":", score)
    if score_max < 15:
        print("score maximal ({}) faible, on recommence ? (o/n)".format(score_max))
        if input() == 'n':
            score_max = 20
    else:
        print("k sélectionné :", k)
        print("Taux de réussite :", score_max/20)
"""
k = 10

def langue(m):
    return prediction_knn (T , c , m , k , d)

def analyse_knn(m):
    res = prediction_knn (T , c , m , k , d)
    t = knn (T , m , k , d)
    p = len([1 for m in t if c[m] == res])
    print("Voici les {} mots de la liste les plus proches de {} :".format(k, m))
    for mot in t:
        print("\t", mot, " "*(26-len(mot)), "langue:", c[mot], "\tdistance :", d(m, mot))
    print("Prédiction knn : {}".format(res))
    print("Sureté : {}/{}".format(p, k))




