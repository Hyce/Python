import json
chemin_fichier = "data/utilisateurs.json"
chemin_fichier2 = "data/utilisateurs_25plus.json"
try :
    with open(chemin_fichier, "r", encoding="utf-8")as plus:
        compteur = 0
        vieu = json.load(plus)
        utilisateurs_filtres = []
        for vie in vieu:
            prenom = vie["prenom"]
            age = vie["age"]
            ville = vie["ville"]
            if age > 25:
                compteur=compteur+1
                print(f"{prenom} a {age} ans et habite à {ville}.")
                utilisateurs_filtres.append(vie) 
        print(f" Il y a {compteur} personnes qui ont plus de 25 ans")
        with open(chemin_fichier2, "w", encoding="utf-8") as fichier_sortie:
            json.dump(utilisateurs_filtres, fichier_sortie, ensure_ascii=False, indent=2)
            print("Le fichier utilisateurs_25plus.json a été créé avec succès.")
except FileNotFoundError:
    print("Fichier Introuvable")