def hamming(s1, s2):
    score = 0
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i]:
            score += 1
    score += abs(len(s1)-len(s2))
    return score

def disque(lexique, mot , rayon):
    res = []
    for m in lexique:
        if hamming(m, mot) <= rayon:
            res.append(m)
    return res

def plus_proche(lexique, mot):
    m_min = lexique[0]
    d_min = hamming(m_min, mot)
    for m in lexique:
        d = hamming(m, mot)
        if d < d_min:
            d_min = d
            m_min = m
    return m_min

def oubli(c, d):
    if len(d)!=len(c)+1:
        return False
    for i in range(len(d)):
        d2 = d[:i]+d[i+1:]
        if c==d2:
            return True
    return False
