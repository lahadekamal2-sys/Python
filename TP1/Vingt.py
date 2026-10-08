import math
from time import sleep

def fonction(a, b, c): 
    D = b**2 - 4 * a * c

    print("Calcul de Delta...\n")
    sleep(2)

    print("Delta =", D) 
    sleep(2) 

    # Traitement selon la valeur de Delta
    if D > 0:
        print("Delta est positif : deux solutions distinctes.\n")
        sleep(1)
        
        print("Calcul des solutions...\n")
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        sleep(2)
        print("X1 =", x1)
        print("X2 =", x2)

    elif D == 0:
        print("Delta est nul : une solution unique (double).\n")
        sleep(1)
        
        print("Calcul de la solution...\n")
        x0 = -b / (2 * a)
        sleep(1)
        print("X0 =", x0)

    else:
        print("Delta est négatif : aucune solution réelle.")



