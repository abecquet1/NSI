def rot13(s):
    res = ""
    for c in s:
        if 97<=ord(c)<123:
            c = chr(97+(ord(c)-97+13)%26)
        res+=c
    return res

print(rot13('python pour les nuls MAIS NE MARCHE PAS POUR LES MAJUSCULES OU LES CARACTèRES ACCENTUéS'))
