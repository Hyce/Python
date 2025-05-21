import csv

chemin_fichier = "data/notes.csv"
meilleure_moyenne=0
meilleur_nom=0
try : 
    with open(chemin_fichier, "r", encoding="utf-8")as mei:
        notes = csv.DictReader(mei)
        for note in notes:
            nom=note["nom"]
            maths=float(note["maths"])
            francais=float(note["francais"])
            anglais=float(note["anglais"])
            moyenne=(maths+francais+anglais)/3
            moyenne_arrondie=round(moyenne, 1)
            if moyenne>meilleure_moyenne:
                meilleure_moyenne = moyenne
                meilleur_nom = nom

        print(f"La meilleur moyenne est celle de {nom} est c'est celle de {meilleure_moyenne}")

except FileNotFoundError:
    print("Fichier Introuvbable")