import json

chemin_fichier = "data/utilisateurs_amis.json"

try:
    with open(chemin_fichier,"r", encoding="utf-8")as facebook:
        amigos = json.load(facebook)
        max_amis=0
        nb_amis=[]
        for amigo in amigos:
            prenom=amigo["prenom"]
            amis=amigo["amis"]
            if len(amis)== 0:
                print(f"{prenom} a 0 amis")
            elif len(amis)>0 and len(amis)<2:
                print(f"{prenom} a {len(amis)} ami et son nom est {', '.join(amis)}")
            elif len(amis)>1:
                print(f"{prenom} a {len(amis)} amis et leurs noms sont {', '.join(amis)}")
            if len(amis) > max_amis:
                max_amis=len(amis)
                print(f"La personne ayant le maximum d'amis en a {max_amis}")
            if len(amis)==max_amis:
                nb_amis.append(prenom)
        print(f"{' et '.join(nb_amis)} ont le plus d'amis au nombre de  {max_amis}.")




        
except FileNotFoundError:
    print("Fichier Introuvable")