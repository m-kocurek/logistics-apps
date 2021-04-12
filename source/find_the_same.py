def find(track, dane):
    zmienna = False #false gdy nie ma takie wartosci na trasie

    rows = len(track)

    for i in range(rows):
        if track[i][0] == dane[0] and track[i][1] == dane[1] and track[i][2] == dane[2]:
            zmienna = True
            break


    return zmienna