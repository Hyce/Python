import csv

chemin_fichier = "data/livres.csv"

try:
    with open(chemin_fichier, "r", encoding="utf-8") as lec:
        livre=csv.DictReader(lec)
        for ligne in livre:
            titre=ligne["titre"]
            auteur=ligne["auteur"]
            annee=ligne["annee"]
            print(f"L'auteur {auteur} a publié {titre} en {annee}.")

except FileNotFoundError:
    print("Le fichier 'livres.csv' est introuvable dans le dossier data/")