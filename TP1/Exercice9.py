N = int(input("Saisir n : "))
S=0

for i in range(1,N+1) : 
   S = 1/i + S
   print(f" 1/{i} \t ")

print(f"La somme est  : {format(S, ".2f")}" )