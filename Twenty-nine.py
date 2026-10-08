score = { "joueur" : "lahade" , "level" : 50 }

niveau = score.get("level",1)

# pour eviter keyerror on ajoute une valeur defaut

print (f"{score["joueur"]} level  {niveau}")

