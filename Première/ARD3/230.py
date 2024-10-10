"""on suppose que b est directement donnée en binaire"""

def longueur(b):
    n = 0   #nombre de caractère 
    i = 0   #position dans la chaîne
    while i < len(b):
        n+=1
        
        if b[i] == '0': #caractère sur 1 octet  
            i+=8        #on saute au caractère suivant 
            
        else:
            k = 0       #nombre d'octets de l'encodage du caractère
            while b[i+k] == '1':
                k+=1
            i+=8*k      #on saute au caractère suivant
    return n


def longueur(b):
    #plus simple mais moins drole
    n = 0
    i = 0
    while i<len(b):
        if (b[i], b[i+1]) != ('1', '0'):
            n+=1
        i+=8
    return n
        


def bin8(n):
    """renvoie l'écriture binaire 8 bits de n<256"""
    s = bin(n)[2:]
    return (8-len(s))*"0"+s


#reprise des encodages valides de l'exercice 229 (1 et 3)
chaine1 = bin8(126)+bin8(64)+bin8(100)
chaine2 = bin8(227)+bin8(180)+bin8(140)

print(longueur(chaine1))
print(longueur(chaine2))

    
