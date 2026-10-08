nombre =[ 1,2,34,]

carrer = [ i**2 for i in nombre ]

print (carrer)

print ("\n === EXERCICE 2 === \n")

motes = [ 12,20,15,3,4,5]

admis = [ i for i in motes if i>=10 ]

print (f" les admis sont : \n {admis}")

print ("\n === EXERCICE 3 === \n")

mots = {"python" , "code"}

maj =  { element for element in mots element.upper()}

print (maj)

