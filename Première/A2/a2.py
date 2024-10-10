# Exercice 152

def recherche_dichotomique(t, v, etapes = False):
    """Renvoie l'indice de la valueur v si elle appraît dans t trié et None sinon """
    g = 0
    d = len(t)-1
    n = 0
    while g<=d:
        n+= 1
        m = (g+d)//2
        if v > t[m]:
            g = m+1
        elif v < t[m]:
            d = m-1
        else:
            if etapes:
                print(f"Calcul effectué en {n} étapes.")
            return m
    if etapes:
        print(f"Calcul effectué en {n} étapes.")
    return None

print(recherche_dichotomique([1,1,1,1,1,1,2,2,2,3,4,5,9,10], 8, True))

# Exercice 153

def nb_tours(n):
    k = 0
    p = 1
    while p<=n:
        k += 1
        p = p*2
    return k


# Exercice 154

# il faut nb_tours(100) = 7 étapes dans le pire cas

# Exercice 155

def devine(n):
    g = 0
    d = n
    rep = 'toto'
    while g<d and rep!= '=':
        m = (g+d)//2
        print(f"Proposition : {m}  (+/-/=)")
        rep = input()
        while rep not in ('+', '-', '='):
            print("Réponse invalide (+/-/=)...")
            rep = input()
        if rep == '+':
            g = m+1
        elif rep == '-':
            d = m-1
    if g == d:
        print(f"Ton nombre est {m}")
    elif rep == '=':
        print("Trop facile !")
    else:
        print("Tricheur...")



# Exercice 156


def tricheur(n):
    print(f"Je pense à un nombre entre 1 et {n}, sauras-tu le deviner ?")
    g = 1
    d = n
    while g<d:
        prop = int(input('Quelle est ta proposition ? '))
        if prop > d:
            print("C'est moins !")
        elif prop < g:
            print("C'est plus")
        elif prop <= (g+d)//2:
            print("C'est plus !")
            g = prop+1
        else:
            print("C'est moins !")
            d = prop-1
    rep = g
    while prop!=rep:
        prop = int(input('Quelle est ta proposition ? '))
        if prop < rep:
            print("C'est plus !")
        elif prop > rep:
            print("C'est moins !")
    print("Bravo tu as trouvé !")
