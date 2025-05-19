import csv

chemin_fichier = "data/eleves.csv"

try:
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            prenom = ligne["prenom"]
            age = ligne["age"]
            ville = ligne["ville"]
            print(f"{prenom} a {age} ans et habite à {ville}.")
except FileNotFoundError:
    print("Le fichier 'eleves.csv' est introuvable dans le dossier data/")