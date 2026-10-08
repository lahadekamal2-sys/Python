N = int(input("Saisir n : "))

for n in range(1, N + 1):
    M = 13 * n
    
    # Si M est un multiple de 7, on affiche
    if M % 7 == 0:
        print(f"Multiple = {M}")
   
