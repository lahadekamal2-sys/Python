def positif(x):
    for i in range(0, 13, 1):
        M = i * x
        print(f"{i} * {x} = {M}")


X = int(input("X: "))

# Contrôle de saisie 
while X < 0:
    X = int(input("X doit être >= 0\nX: "))

# Calcul et affichage de la table
positif(X)

print("Merci de votre visite")