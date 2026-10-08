produits = [ "Pc" , "Souris" ]
prix = [ 800 ,40 ] 

for p ,P in zip(produits,prix) : 
    print (f" {p} vaut : {P} dh ")

print ("\n === EXERCICE 2 === \n")

dico = dict(zip(produits,prix))

print (dico)
 
# ici on obtient une liste de tuples 

listes = list(zip(produits,prix))

print(listes)