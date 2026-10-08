notes = [12, 14, 9, 15, 10]

for note in notes:
    if note == 10:
        print(f"{note} : Passable")
    elif 12 <= note <= 13: 
        print(f"{note} : Assez Bien")
    elif 14 <= note <= 16:
        print(f"{note} : Bien")
    else:
        print(f"{note} : Insuffisant")
