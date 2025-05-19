# exercices/lire_prenoms.py

chemin_fichier = "data/prenoms.txt"  # adapte le chemin si besoin

try:
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        for numero, ligne in enumerate(f, 1):
            print(f"{numero}. {ligne.strip()}")
except FileNotFoundError:
    print("Le fichier 'prenoms.txt' est introuvable dans le dossier data/")
