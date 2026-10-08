x = int(input("Entrez la valeur de X : "))
S = 0

for i in range(1, x + 1):
    n = 1 / i
    print(f"Terme 1/{i} = {n:.2f}")
    S += n

print("La somme est :", round(S, 2))