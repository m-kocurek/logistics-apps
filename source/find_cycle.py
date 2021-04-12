import find_the_same
def find(cycle, track, lo, ld, x, y):

    while True:
        rows = len(track)

        if rows < 2:
            if x < (lo - 1):
                dane = right(cycle, lo, ld, x, y)

                if find_the_same.find(track, dane) == False:

                    track.append([dane[0], dane[1], dane[2]])
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    # print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    break

            if y < (ld - 1):
                dane = down(cycle, lo, ld, x, y)

                if find_the_same.find(track, dane) == False:
                    track.append([dane[0], dane[1], dane[2]])
                    # print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    break

            if x > 0:
                dane = left(cycle, lo, ld, x, y)

                if find_the_same.find(track, dane) == False:
                    track.append([dane[0], dane[1], dane[2]])
                    # print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    break

            if y > 0:
                dane = up(cycle, lo, ld, x, y)

                if find_the_same.find(track, dane) == False:
                    track.append([dane[0], dane[1], dane[2]])
                    # print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    break

        else:
            # gdy oba sa pionowo to szukamy poziomo
            if track[rows-1][2] == track[rows-2][2]:

                if rows > 3:
                    dane = [track[rows-1][0], track[rows-1][1], track[rows-1][2]]
                    first = [track[0][0], track[0][1], track[0][2]]
                    if dane[1] == first[1]:
                        if first[2] > dane[2]:
                            check = right_end(cycle, track, lo, ld, x, y)
                            if check == True:
                                break
                        else:
                            check = left_end(cycle, track, lo, ld, x, y)
                            if check == True:
                                break


                if x < (lo-1):
                    dane = right(cycle, lo, ld, x, y)

                    #gdy znalazło mi znowu ostatni element sprawdam czy w tym wierszu nie konczymy obliczen
                    if find_the_same.find(track,dane) == True:
                        check = right_end(cycle, track, lo, ld, x, y)
                        if check == True:
                            break
                        #else:
                        #    track.pop()

                    else:
                        track.append([dane[0], dane[1], dane[2]])
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        break



                if x > 0:
                    dane = left(cycle, lo, ld, x, y)

                    if find_the_same.find(track, dane) == True:
                        check = left_end(cycle, track, lo, ld, x, y)
                        if check == True:
                            break

                    else:
                        track.append([dane[0], dane[1], dane[2]])
                        # print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        break

            elif track[rows - 1][1] == track[rows - 2][1]:

                if rows > 3:
                    dane = [track[rows-1][0], track[rows-1][1], track[rows-1][2]]
                    first = [track[0][0], track[0][1], track[0][2]]
                    if dane[2] == first[2]:
                        if first[1] > dane[1]:
                            check = down_end(cycle, track, lo, ld, x, y)
                            if check == True:
                                break
                        else:
                            check = up_end(cycle, track, lo, ld, x, y)
                            if check == True:
                                break


                if y < (ld-1):
                    dane = down(cycle, lo, ld, x, y)

                    if find_the_same.find(track, dane) == True:
                        check = down_end(cycle, track, lo, ld, x, y)
                        if check == True:
                            break

                    else:
                        track.append([dane[0], dane[1], dane[2]])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        break


                if y > 0:
                    dane = up(cycle, lo, ld, x, y)

                    if find_the_same.find(track, dane) == True:
                        check = up_end(cycle, track, lo, ld, x, y)
                        if check == True:
                            break

                    else:
                        track.append([dane[0], dane[1], dane[2]])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        break


    return track


def right(cycle, lo, ld, x, y):

    dane = [cycle[y][x], y, x]
    while x < lo-1:
        x = x + 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            #break

    return dane

def right_end(cycle, track, lo, ld, x, y):

    first = [track[0][0], track[0][1], track[0][2]]
    zmienna = False
    while x < lo - 1:
        x = x + 1
        if cycle[y][x] == first[0] and y == first[1] and x == first[2]:
            zmienna = True
            break

    return zmienna




def down(cycle, lo, ld, x, y):

    licznik = 0
    dane = [cycle[y][x], y, x]
    while y < (ld-1):
        y = y + 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            licznik += 1
            if licznik == 2:
                break

    return dane


def down_end(cycle, track, lo, ld, x, y):

    first = [track[0][0], track[0][1], track[0][2]]
    zmienna = False
    while y < (ld-1):
        y = y + 1
        if cycle[y][x] == first[0] and y == first[1] and x == first[2]:
            zmienna = True
            break

    return zmienna


def left(cycle, lo, ld, x, y):

    dane = [cycle[y][x], y, x]
    while x > 0:
        x = x - 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            #break

    return dane


def left_end(cycle, track, lo, ld, x, y):

    first = [track[0][0], track[0][1], track[0][2]]
    zmienna = False
    while x > 0:
        x = x - 1
        if cycle[y][x] == first[0] and y == first[1] and x == first[2]:
            zmienna = True
            break

    return zmienna


def up(cycle, lo, ld, x, y):

    dane = [cycle[y][x], y, x]
    while y > 0:
        y = y - 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            break

    return dane

def up_end(cycle, track, lo, ld, x, y):

    first = [track[0][0], track[0][1], track[0][2]]
    zmienna = False
    while y > 0:
        y = y - 1
        if cycle[y][x] == first[0] and y == first[1] and x == first[2]:
            zmienna = True
            break

    return zmienna

