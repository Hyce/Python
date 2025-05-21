import json

chemin_fichier="data/utilisateurs.json"

try:
    with open(chemin_fichier,"r", encoding="utf-8")as f:
        donnees = json.load(f)
        for utilisateur in donnees:
            prenom = utilisateur["prenom"]
            age = utilisateur["age"]
            ville = utilisateur["ville"]
            print(f"{prenom} a {age} et habite à {ville}")
except FileNotFoundError:
    print("Fichier introuvable")