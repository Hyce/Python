import csv

chemin_fichier = "data/notes.csv"

try:
    with open(chemin_fichier, "r", encoding="utf-8") as el:
        notes=csv.DictReader(el)
        for note in notes:
            nom=note["nom"]
            maths=float(note["maths"])
            francais=float(note["francais"])
            anglais=float(note["anglais"])
            moyenne = (maths+francais+anglais)/3
            moyenne_arrondie = round(moyenne, 1)
            print(f"{nom} a une moyenne de {moyenne_arrondie}")




except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")