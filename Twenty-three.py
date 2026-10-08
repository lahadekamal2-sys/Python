from time import sleep
Liste = [ 'Ali' ,"Sara","Omar",]
 
print ("Premier element : " , Liste [0] )
 
nom = input(" Souhaitez vous remplacer Sara par qui ? ")
 
Liste [1] = nom
 
print ( " Remplacement..." )
 
 
sleep (2)
 
for indice , list in enumerate(Liste) : 
  print (f"[{indice}] ",list)      
 