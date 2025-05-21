import csv

chemin_fichier = "data/notes.csv"
try:
    with open(chemin_fichier, "r", encoding="utf-8") as moy:
        notes=csv.DictReader(moy)        
        meilleur_nom=[]
        meilleure_moyenne=0
        for note in notes:
            nom=note["nom"]
            maths=float(note["maths"])
            francais=float(note["francais"])
            anglais=float(note["anglais"])
            moyenne=(maths+francais+anglais)/3
            moyenne=round(moyenne,1)
            print(f"La Moyenne de {nom} est de {moyenne}")
            if moyenne>meilleure_moyenne:
                meilleure_moyenne=moyenne
                meilleur_nom=[nom]
            elif moyenne == meilleure_moyenne:
                meilleur_nom.append(nom)
            noms_formates=" et ".join(meilleur_nom)
            print(f"La ou les meilleurs moyennes sont celles de {noms_formates} et sont de {meilleure_moyenne}")

                
            
except FileNotFoundError:
    print("Fichier Introuvable")