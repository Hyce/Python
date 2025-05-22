import json
import csv

chemin_fichier = "data/catalogue.json"
chemin_csv = "data/catalogue.csv"

try:
    with open(chemin_fichier, "r", encoding="utf-8") as ca:
        catalogue = json.load(ca)
        nom_articles = [article["nom"] for article in catalogue]
        
        print(f"Veuillez choisir un article à modifier : {', '.join(nom_articles)}")
        choix_article = input("Votre choix : ").strip()
        
        trouve = False
        for article in catalogue:
            if article["nom"] == choix_article:
                print(f"Vous avez choisi {article['nom']}, sa catégorie est {article['categorie']}, son stock de {article['stock']} et son prix de {article['prix']}.")
                
                modifier = input("Que voulez-vous modifier ? (nom/prix/stock/categorie) : ").strip()
                if modifier not in article:
                    print("Champ non reconnu")
                    break
                
                nouvelle_valeur = input(f"Nouvelle valeur pour {modifier} : ")
                
                # Conversion du type
                try:
                    if modifier == "prix":
                        nouvelle_valeur = float(nouvelle_valeur)
                    elif modifier == "stock":
                        nouvelle_valeur = int(nouvelle_valeur)
                except ValueError:
                    print("Type de valeur incorrect !")
                    break
                
                article[modifier] = nouvelle_valeur
                print("Article modifié avec succès !")
                trouve = True
                break  # Sortir de la boucle après modification
        
        if not trouve:
            print("Article introuvable ou modification annulée")
        else:
            # Sauvegarde JSON
            with open(chemin_fichier, "w", encoding="utf-8") as ca:
                json.dump(catalogue, ca, indent=2, ensure_ascii=False)
            
            # Export CSV
            with open(chemin_csv, "w", encoding="utf-8", newline='') as mod:
                writer = csv.DictWriter(mod, fieldnames=catalogue[0].keys())
                writer.writeheader()
                writer.writerows(catalogue)
            print("Catalogue exporté en CSV avec succès !")

except FileNotFoundError:
    print("Fichier catalogue.json introuvable")
except Exception as e:
    print(f"Erreur : {str(e)}")
