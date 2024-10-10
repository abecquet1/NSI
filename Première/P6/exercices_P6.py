from random import randint

### exercice 90 ###

def nb_chiffre(n,b=10):
    assert 0<b, "non"
    puissance = b
    res = 1
    while puissance <= n :
        puissance = puissance*b
        res = res+1
    return res



### exercice 91 ###

def syracuse1(n):
    print(n)
    while n !=1:
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        print(n)


### exercice 92 ###

def syracuse2(n):
    a = n
    compteur = 0
    maxi = n
    while n !=1:
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        compteur = compteur+1
        if n>maxi:
            maxi = n
    print("Altitude initiale :", a)
    print("Temps de vol :", compteur)
    print("Altitude maximale :", maxi)



### exercice 93 ###


def syracuse3(n):
    a = n
    compteur = 0
    maxi = n
    while n !=1:
        if n%2==0:
            n = n//2
        else:
            n = 3*n+1
        compteur = compteur+1
        if n>maxi:
            maxi = n
    return (compteur, maxi)



def syracuse_en_folie(n):
    n_max, a_max = syracuse3(1)
    for i in range(2, n+1):
        n, a = syracuse3(i)
        if n>n_max:
            n_max = n
        if a>a_max:
            a_max = a
    return n_max, a_max

### exercice 94 ###

def fibo(s=1000):
    a = 0
    b = 1
    while a<s:
        print(a)
        (a,b) = (b,a+b)




### exercice 95 ###

def digramme(a, b, tab):
    present = False
    i = 0
    while i<len(tab)-1:
        if t[i] == a and t[i+1] == b:
            present = True
        i=i+1
    return present



def sous_mot(a, b, tab):
    # 1 - trouver la premiere apparition de a
    i = 0
    present_a = False
    while i < len(t) and not(present_a):
        if t[i] == a:
            present_a = True
        i = i+1

    # 2 - à partir de cette position, chercher la première apparition de b d
    present_b = False
    while i < len(t) and not(present_b):
        if t[i] == b:
            present_b = True
        i = i+1

    return present_a and present_b









### exercice 96 ###

def sous_mot(a, b, tab):
    present_a = False
    i = 0
    while i<len(tab) and not(present_a):
        if t[i] == a:
            present_a = True
        i=i+1
    if not(present_a):
        return False
    else:
        present_b = False
        while i<len(tab) and not(present_b):
            if t[i] == b:
                present_b = tab[i]==b
            i=i+1
        return present_b


def sous_mot(mot1, mot2):
    i = 0 # indice pour se balader dans mot1
    j = 0 # indice pour se balader dans mot2

    # pour chaque élément de mot1
    while i < len(mot1):
        # trouver sa premiere position dans tab2
        while j< len(mot2) and mot2[j] != mot1[i]:
            j = j+1

        # passer à l'élément suivant de tab1
        i = i + 1

    return j != len(mot2)






### exercice 98 ###


def pgs_mono(e, tab):

    score = 0
    maxi = 0
    i = 0
    while i<len(tab):

        if tab[i]==e:
            score = score + 1
        else:
            score = 0

        if score>maxi:
            maxi = score
        i=i+1

    return maxi



### exercice 99 ###

def pgs(tab):
    candidat = tab[0]
    score = 1
    maxi = 1
    i = 1
    while i<len(tab):
        if tab[i]==candidat:
            score = score + 1

        else:
            score = 1
            candidat = tab[i]

        if score>maxi:
            maxi = score

        i=i+1
    return maxi

### exercice 100 ###

def pgpc(t1,t2):
    i = 0
    pareil = True
    while i < min(len(t1), len(t2)) and pareil :
        if t1[i] != t2[i]:
            pareil = False
        else :
            i = i+1
    return i


### exercice 101 ###

def ordre(m1, m2):
        i = 0
        pareil = True
        while i < min(len(m1), len(m2)) and pareil :
            if ord(m1[i]) != ord(m2[i]):
                pareil = False
            else :
                i = i+1
        #à la fin de cette boucle i est le premier indice
        #sur lequel t1 et t2 sont différents (éventuellement oob)
        if i == len(m1):
            #m1 est un prefixe (large) de m2
            return True
        elif i == len(m2):
            #m2 est un prefixe (strict) de m1
            return False
        else:
            #sinon la comparaison de le premiere lettre non commune donne le résultat
            return ord(m1[i]) <= ord(m2[i])


### exercice 102 ###
"""
Dans le premier programme, b est un variant de boucle strictement décroissant
car il diminue de 1 à chaque passage. Ainsi, à un moment, la condition b>0 ne
sera plus vraie et la boucle terminera.

Dans le deuxième programme, i est un variant de boucle strictement croissant
car il augmente de 1 à chaque passage. Ainsi, à un moment, la condition i<b ne
sera plus vraie et la boucle terminera.
"""

### exercice 103 ###

"""
Dans le premier programme, a est un variant de boucle strictement décroissant
car il est divisé par dix à chaque passage (*). Ainsi, à un moment, la condition
a>0 ne sera plus vraie et la boucle terminera.

(*) on utilise ici le fait que a//10 < a quelque soit a>0 ce qu'on peut démontrer :
supposons a>0, alors 9a>0 et 10a>a donc a > a/10 >= a//10


Dans le deuxième programme, k est un variant de boucle strictement croissant
car il est multiplié par 10 à chaque passage (**). Ainsi, à un moment, la
condition k<a+1 ne sera plus vraie et la boucle terminera.

(**) k>0 donc 9k>0 et donc 10k>k
"""


### exercice 104 ###

"""
i est un invariant strictement croissant de la boucle while car il augmente de
un à chaque passage. Ainsi la condition i<len(t) ne sera plus vraie au bout d'un
moment et la boucle terminera.
"""

### exercice 105 ###

"""
soient n1 = len(t1) et n2 = len(t2)
(P1) si i1<n1 et i2<n2 alors i1+i2<n1+n2
contraposée
(P2) si i1+i2>=n1+n2 alors non(i1<n1 et i2<n2)
condition de la boucle
(P3) si i1+i2>=n1+n2 alors la boucle s'arrète

i1+i2 est un variant strictement croissant de la boucle while car à chaque étape
i1 ou i2 augmente toujours. Or lorsque i1+i2 depasse n1+n2, donc la boucle s'arrête
par (P3)
"""

### exercice 106 ###
"""
la condition i<j peut se réécrire j-i>0, or j-i est un invariant strictement décroissant
de la boucle car à chaque passage, ou bien j diminue, ou bien i augmente. On en déduit qu'à
un moment i<j n'est plus vraie et donc la boucle s'arrête.
"""

### exercice 107 ###


def ex107():
    nb = randint(1,1000)
    nb_joueur = int(input("Devine le nombre !\n"))
    while nb_joueur != nb:
        if nb_joueur < nb:
            print("C'est plus !")
        else:
            print("C'est moins !")
        nb_joueur = int(input())
    print("Bravo, le nombre était bien", nb)
















def ex107_bis():
    print("pensez à un nombre entre 1 et 1000...")
    a = 1
    b = 500
    c = 1000
    trouve = False
    while a!=c and not(trouve):
        rep = input("Est-ce {} ? (o/n)".format(b))
        if rep == 'o':
            trouve = True
        else:
            rep = input("Zut ! Est-ce plus ou moins que {} ? (+/-)".format(b))
            if rep == '+':
                (a,b,c) = (b,(b+c)//2,c)
            else:
                (a,b,c) = (a,(a+b)//2,b)
    print("Votre nombre est {} !".format(b))




### exercice 108 ###

def ex108_1():
    allumette = 21
    while allumette > 0:
        print("il y a", allumette, "alumettes.")
        n_joueur = int(input("combien en prenez-vous ? "))
        allumette -= n_joueur

        n_ia = min(allumette,randint(1,3))
        allumette -= n_ia
        print("je prends", n_ia, "alumettes")






def ex108_2():
    allumette = 21
    while allumette > 0:
        print("il y a", allumette, "alumettes.")
        n_joueur = int(input("combien en prenez-vous ? "))
        allumette -= n_joueur
        if allumette <= 0:
            print("vous avez perdu !")
            break
        n_ia = min(allumette,randint(1,3))
        allumette -= n_ia
        print("je prends", n_ia, "alumettes")
        if allumette <= 0:
            print("j'ai perdu, bien joué !")
            break








def ex108_3():
    allumette = 21
    while allumette > 0:
        print("il y a", allumette, "alumettes.")
        n_joueur = int(input("combien en prenez-vous ? "))
        while not(1<=n_joueur<=3):
            n_joueur = int(input("Valeur incorrecte, recommencez : "))
        allumette -= n_joueur
        if allumette <= 0:
            print("vous avez perdu !")
            break
        n_ia = min(allumette,randint(1,3))
        allumette -= n_ia
        print("je prends", n_ia, "alumettes")
        if allumette <= 0:
            print("j'ai perdu, bien joué !")
            break





def ex108_4():
    allumette = 21
    while allumette > 0:
        print("il y a", allumette, "alumettes.")
        n_joueur = int(input("combien en prenez-vous ?"))
        while not(1<=n_joueur<=3):
            n_joueur = int(input("Valeur incorrecte, recommencez :"))
        allumette -= n_joueur
        if allumette <= 0:
            print("vous avez perdu !")
            break
        n_ia = 4-n_joueur
        allumette -= n_ia
        print("je prends", n_ia, "alumettes")
        if allumette <= 0:
            print("j'ai perdu, bien joué (et vous avez triché) !")
            break









