doublons = ["a", "b", "a", "c", "b"]

liste= list(set(doublons))



print(liste)

print ("\n === EXERCICE 2 === \n")

interdits = {"admin", "root", "system"}

if "admin" in interdits : 
    print ( " Acces refuser " )
    