def premier(x):
    # Les nombres <= 1 ne sont pas premiers
    if x <= 1:
        print(f"Le nombre {x} n'est pas premier")
        return

    # On vérifie s'il existe un diviseur entre 2 et x - 1
    est_premier = True
    for i in range(2, x):
        if x % i == 0:
            est_premier = False
            break  # On a trouvé un diviseur, pas besoin de continuer

    if est_premier:
        print(f"Le nombre {x} est premier")
    else:
        print(f"Le nombre {x} n'est pas premier")

x = int(input("Saisissez un entier positif : "))
premier(x)