n = int(input("Entrez la valeur de X : "))
while ( n < 0 ):
 n = int(input("Entrez une valeur  positive : "))
 if n > 0 : 
     break
f=1
if n==0 or n == 1 : 
    print (f" Factorielle de {n} est 1 ")
else : 
    for i in range (1,n+1,1):
     f= f * i 
print ( f" Factorille de {n} est {f}")     