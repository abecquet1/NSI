def encodage(c):
    code_bin = bin(ord(c))[2:]
    n = len(code_bin)
    if n<8:         #1 octet
        code_bin = "0"*(8-n)+code_bin
        return code_bin
    elif n<12:      #2 octets
        code_bin = "0"*(11-n)+code_bin
        return "110"+code_bin[:5]+" 10"+code_bin[5:]
    elif n<17:      #3 octets
        code_bin = "0"*(16-n)+code_bin
        return "1110"+code_bin[:4]+" 10"+code_bin[4:10]+" 10"+code_bin[10:]
    elif n<22:      #4 octets
        code_bin = "0"*(21-n)+code_bin
        return "1110"+code_bin[:3]+" 10"+code_bin[3:9]+" 10"+code_bin[9:15]+" 10"+code_bin[15:]
    else:
        raise ValueError("Point de code trop grand pour être encodé en UTF-8")
        

def unicode(s):
    for c in s:
        print(c, ":")
        print("\tPoint de code :", ord(c), "=", hex(ord(c))[2:])
        print("\tEncodage :", encodage(c))
