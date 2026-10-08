A = int(input("A : "))
B = int(input("B : "))

# Si le produit est négatif,  signes contraires
if A * B < 0:
    print("produit  négatif : échange des valeurs de A et B.")
    
    # Sauvegarde de A dans C pour l'échange
    C = A
    A = B
    B = C
    
    print("Nouvelles valeurs -> A =", A, "| B =", B)
else:
    print("Le produit est positif ou nul : pas d'échange.")
    print("Valeurs conservées -> A =", A, "| B =", B)