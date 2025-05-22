import json

chemin_fichier = "data/produits.json"

try:
    with open(chemin_fichier, "r", encoding="utf-8") as pr:
        produits = json.load(pr)
        prix_min=10000000
        produit_min=[]
        for produit in produits:
            nom=produit["nom"]
            prix=produit["prix"]
            stock=produit["stock"]
            if prix<prix_min:
                prix_min=prix
                produit_min=[nom]
            elif prix==prix_min:
                produit_min.append(nom)
        print(f"Il y a {len(produit_min)} de produit au plus bas prix. C'est {" , ".join(produit_min)} au prix de {prix_min}.")



except FileNotFoundError:
    print("Fichier Introuvable")