# les liste regroupement d'element differents
# ils sont 
#├── ordonnée
#├── modifiable
#├── accepte les doublons
#└── utilise les []


# declaration 

notes =['lahade',1,2,3,4,5]

# chaque element possede un indice 
# print ( notes [2] ) = 3

# modifier

notes [2] = 3
 
#Ajouter 

notes.append(13)


# Supprimer 

notes.remove(13)

# la taille 

print (f"la taille est {len(notes)}")



# Afficher 

d=notes.pop()
print ( d )