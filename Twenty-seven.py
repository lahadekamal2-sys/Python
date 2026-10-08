"""
import time  

price = [12, 34, 23, 4, 5, 95, 101, 44, 32, 54]

print(f"\nNous avons {len(price)} prix \n")

print("Trie par ordre croissant : \n")

price.sort()
print(price, "\n")

print("Calcule du total...")
time.sleep(1) 


s = sum(price)
print("Somme totale :", s, "\n")

print("Calcule de la moyenne...")
time.sleep(1) 



print("Moyenne =", s / len(price))
"""
## ou sinon faire : 

prix = [10, 20, 30]

moyenne = sum(prix) / len(prix)
print("Moyenne :", moyenne) 