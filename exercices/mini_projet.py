import json

chemin_json = "data/catalogue.json"
chemin_envoie = "data/catalogue_envoie.json"

try:
    with open(chemin_json, "r", encoding="utf-8") as cata:
        
        prix_min=float('inf')
        prix_max=0
        somme_prix=0

        catal=json.load(cata)
        '''''''''''
        for cat in catal:
            prix=cat["prix"]
            if prix>prix_max:
                prix_max=prix
            if prix<prix_min:
                prix_min=prix
            somme_prix+=prix
        moyenne=somme_prix/len(catal)
        moyenne=round(moyenne, 2)
        print(f"Le produit le moins cher coûte {prix_min}€")
        print(f"Le produit le plus cher coûte {prix_max}€")
        print(f"La moyenne des prix est de {moyenne}€")
        categories = list(set([cat["categorie"] for cat in catal]))
        choix_categorie=input(f"Choisissez une Catégorie : {', '.join(categories)} :")
        produits_trouves=[]
        for cat in catal:
            if choix_categorie.lower() == cat["categorie"].lower() :
                produits_trouves.append(cat["nom"])
        if produits_trouves:
            print(f"Vous avez choisi la catégorie {choix_categorie} et les produits associées sont {', '.join(produits_trouves)}")
        else:
            print("Ce n'est pas une catégorie")
        try:
            choix_stock=input(f"Choisissez le stock maximum qu'un produit peut avoir :")
            choix_stock=int(choix_stock)
            nom_stockinf=[]
            for cat in catal:
                stock=cat["stock"]
                if stock < choix_stock:
                    nom_stockinf.append(cat["nom"])
            print(f"Les produits avec ce stock maximum sont {', '.join(nom_stockinf)}")
        except:
            print("Ce n'est pas un nombre entier")
        '''''''''
        
        print("Créons un nouveau produit :")
        try:
            nom1=input("Choissez son nom : ")
            nom1=str(nom1)
        except:
            print("Ce doit être un mot")
        try:    
            stock1=input("Choisissez son stock : ")
            stock1=int(stock1)
        except:
            print("Ce n'est pas un nombre")
        try:
            prix1=input("Choisissez son prix : ")
            prix1=float(prix1)
        except:
            print("Ce n'est pas un nombre")
        try:
            categorie1=input("Chosissez sa categorie : ")
            categorie1=str(categorie1)
        except:
            print("Ce doit être un mot")
        nouveau_produit={
            "nom": nom1,
            "prix": prix1,
            "stock": stock1,
            "categorie": categorie1
        }
        catal.append(nouveau_produit)
        with open(chemin_json,"w", encoding="utf-8") as send:
            json.dump(catal, send, indent=2, ensure_ascii=False)
            
except FileNotFoundError:
    print ("Fichier Introuvable")