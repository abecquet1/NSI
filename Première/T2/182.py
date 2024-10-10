import csv

def stats_csv(fichier):
    f = open(fichier, "r")
    table = list(csv.DictReader(f))
    f.close()

    print(len(table), "lignes.")
    print(len(table[0]), "colonnes.")

stats_csv("exemple.csv")

