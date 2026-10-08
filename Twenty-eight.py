produit = {"nom": "Clavier", "prix": 150}
print (produit["prix"])

print ( " Modifaication du prix : \n")

produit ["prix"] =120

print (produit)

print ("\n === EXERCICE 2 === \n")

user = { "Login" : "Ali" , "role" : "admis"}

user ["email"] = "Ali@test.com"

del user["role"]

for cle, val in user.items() : 
    print (f" {cle} : {val} ")
    

    