N = int(input("Saisir n : "))

for n in range(1, N + 1):
    M = 7 * n
    
    # Si M est un multiple de 3, on met un astérisque devant
    if M % 3 == 0:
        print(f"*M = {M}")
    else:
        print(f"M = {M}")
