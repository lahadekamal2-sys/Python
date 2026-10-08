import math

# Saisie des coordonnées des points A(xa, ya) et B(xb, yb)
xa = float(input("Saisir xa : "))
ya = float(input("Saisir ya : "))
xb = float(input("Saisir xb : "))
yb = float(input("Saisir yb : "))

# Calcul de la distance AB
distance = math.sqrt((xb - xa)**2 + (yb - ya)**2)

print("Distance :", format(distance, ".2f"))

print ("  Fin " )