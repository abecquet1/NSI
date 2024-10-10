import csv

f = open("184.csv", 'r')
table = list(csv.DictReader(f))
f.close()

def valide(com):
    r = com["réf"]
    d = com["désignation"]
    p = float(com["prix"])
    q = int(com["qté"])
    return {"réf":r, "désignation":d, "prix":p, "qté":q}

table_valide = [valide(com) for com in table]

for com in table:
    print(com)

for com in table_valide:
    print(com)
