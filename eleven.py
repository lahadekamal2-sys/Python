note1=int(input(" Note : /20 "))
note2=int(input(" Note : /20 "))
note3=int(input(" Note : /20 "))

M=(note1+note2+note3)/3 

if M < 10 : 
    print ( " Insufisant " ) 
elif M >=10 and M <=12 :
    print ( "Passable ")
elif M >=12  and M <= 14 : 
   print (" Assez bien : " )
   
elif M >=14  and M <= 16 : 
   print (" bien : " )
else : 
    print (" tres bien " )
