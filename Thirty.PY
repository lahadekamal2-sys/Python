capitales = {"Maroc": "Rabat", "Espagne": "Madrid", "France": "Paris"}

for cle , val in capitales.items()  : 
    print (f" La capitale de {cle} est {val} ")
    
print ("\n === EXERCICE BONUS === \n")
etudiants = [
    {"nom": "Ali", "note": 14},
    {"nom": "Sara", "note": 8},
    {"nom": "Omar", "note": 12}
]

for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"])
        
print (etudiants[0]["nom"])