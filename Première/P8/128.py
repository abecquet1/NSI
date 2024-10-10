from random import randint


def grille_vide():
    """Renvoie une grille vide de puissance 4."""
    return [[0]*7 for i in range(6)]

# Tableau permettant de convertir une valeur de grille
# ... en caractère à afficher
# ... 0 -> '.'
# ... 1 -> 'X'
# ... 2 -> 'O'
SYMB = ['.', 'X', 'O']

def afficher(g):
    """Affiche une grille de puissance 4."""
    for i in range(6):
        print('|', end = '')
        for j in range(7):
            print(SYMB[g[5-i][j]], end = "")
        print('|')
    print(" "+"\u203e"*7)

def coup_possible(g, c):
    """Teste s'il est autorisé de jouer sur la colonne de g."""
    return 0 <= c < 7 and g[5][c] == 0

def jouer(g, j, c):
    """Ajoute un pion du joueur j dans la colonne c de g."""
    l = 5
    while l>0 and g[l-1][c] == 0:
        l = l-1
    g[l][c] = j

def horiz(g, j, l, c):
    """Teste s'il y a un alignement horizontal à droite de la case (l,c)."""
    if c > 3:
        return False
    return j == g[l][c] == g[l][c+1] == g[l][c+2] == g[l][c+3]

def vert(g, j, l, c):
    """Teste s'il y a un alignement vertical au dessus de la case (l,c)."""
    if l > 2:
        return False
    return j == g[l][c] == g[l+1][c] == g[l+2][c] == g[l+3][c]

def diag_mont(g, j, l, c):
    """Teste s'il y a un alignement diagonnale montante
    à partir de la case (l,c).
    """
    if l > 2 or c > 3:
        return False
    return j == g[l][c] == g[l+1][c+1] == g[l+2][c+2] == g[l+3][c+3]

def diag_desc(g, j, l, c):
    """Teste s'il y a un alignement diagonnale descendante
    à partir de la case (l,c).
    """
    if l < 3 or c > 3:
        return False
    return j == g[l][c] == g[l-1][c+1] == g[l-2][c+2] == g[l-3][c+3]

def victoire(g, j):
    """Teste si je jouer j a gagné."""
    for l in range(6):
        for c in range(7):
            if horiz(g, j, l, c) or vert(g, j, l, c) or diag_mont(g, j, l, c) or diag_desc(g, j, l, c):
                return True
    return False

def match_nul(g):
    """Teste si le match est nul. Potentiellement inutil car match sul au bout de 42 coups."""
    for c in range(7):
        if g[5][c] == 0:
            return False
    return True

def coup_aleatoire(g, j):
    """Le joueur j joue aléatoirement."""
    c = randint(0,6)
    while not coup_possible(g, c):
        c = randint(0,6)
    jouer(g, j, c)
    return c

def showmatch(affichage = True):
    """Simule une partie entre deux joueurs jouant aléatoirement
    et renvoie le numéro du vainqueur (0 si match nul).

    Arguments optionnels :
        affichage -- affiche ou non le détail de la partie (défaut : True)
    """
    g = grille_vide()

    for k in range(6*7):
        j = 1+(k%2)  # Pour alterner entre 1 et 2
        c = coup_aleatoire(g, j)
        if affichage:
            print("Le joueur", j, "joue en", c, ":")
            afficher(g)
        if victoire(g, j):
            if affichage:
                print("Victoire du joueur", j, "("+SYMB[j]+").")
            return j  # On stoppe la fonction en cas de victoire
    if affichage:
        print("Match nul.")
    return 0


def match_contre_ia(joueur = 1):
    """Lance une partie contre une IA qui joue aléatoirement

    Arguments optionnels :
        jouer -- choix du joueur (défaut : 1)
    """
    assert joueur in [1,2], "joueur invalide (1 ou 2)"
    g = grille_vide()
    afficher(g)
    for k in range(6*7):
        j = 1+(k%2)  # Pour alterner entre 1 et 2
        if j == joueur:
            print("À vous de jouer !")
            c = int(input("Entrez un numéro de colonne (entre 0 et 6) : "))
            while not coup_possible(g, c):
                c = int(input("Coup invalide, recommencez : "))
            jouer(g, j, c)
        else:
            c = coup_aleatoire(g, j)
            print("Le joueur", j, "joue en", c, ":")
        afficher(g)
        if victoire(g, j):
            print("Victoire du joueur", j, "("+SYMB[j]+").")
            return None
    print("Match nul.")



# Tests
def plein_de_parties(N):
    N = 100
    print("Simulation de", N, "parties...")
    for i in range(100):
        victoires = [0,0,0]
        for i in range(100):
            gagnant = showmatch(False)
            victoires[gagnant] += 1
    print()
    print("Résultats :")
    print("    Joueur 1 :", victoires[1])
    print("    Joueur 2 :", victoires[2])
    print("    Nuls :    ", victoires[0])

#showmatch()
#plein_de_parties(100)
#partie_contre_ia()







