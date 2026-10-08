F = int(input(" Saisir N : " ))

if F==1 or F==0 : 
   print (f"Factorielle : 1")
else : 
   for  i in range(1,F+1) : 
     f = F*i

print (f"Factorielle : {f}")