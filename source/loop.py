import find_the_same
def find(cycle, track, lo, ld, x, y):

    while True:
        rows = len(track)

        if x < (lo-1):
            dane = right(cycle, lo, ld, x, y)

            if (dane[2] + 1) == track[0][2] and dane[1] == track[0][1]:
                break

            elif find_the_same.find(track,dane) == False:

                if rows > 1:

                    if track[rows-2][1] != dane[1] and track[rows-2][2] != dane[2]:
                        track.append([dane[0], dane[1], dane[2]])
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        break
                else:
                    track.append([dane[0], dane[1], dane[2]])
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    break


        if y < (ld-1):
            dane = down(cycle, lo, ld, x, y)

            if (dane[1]+1) == track[0][1] and dane[2] == track[0][2]:
                break

            elif find_the_same.find(track,dane) == False:
                if rows > 1:

                    if track[rows-2][1] != dane[1] and track[rows-2][2] != dane[2]:
                        track.append([dane[0], dane[1], dane[2]])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        break
                else:
                    track.append([dane[0], dane[1], dane[2]])
                    #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    break


        if x > 0:
            dane = left(cycle, lo, ld, x, y)

            if dane[1] == track[0][1] and (dane[2] - 1) == track[0][2]:
                break

            elif dane[2] != track[rows-1][2]:
                if rows > 1:

                    if track[rows-2][1] != dane[1] and track[rows-2][2] != dane[2]:
                        track.append([dane[0], dane[1], dane[2]])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                        break
                else:
                    track.append([dane[0], dane[1], dane[2]])
                    #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                    find(cycle, track, lo, ld, track[rows][2], track[rows][1])
                    break


        if y > 0:
            dane = up(cycle, lo, ld, x, y)

            if (dane[1] - 1) == track[0][1] and dane[2] == track[0][2]:
                break

            elif dane[1] != track[rows-1][1]:
                if rows > 1:

                    if track[rows-2][1] != dane[1] and track[rows-2][2] != dane[2]:
                        track.append([dane[0], dane[1], dane[2]])
                        #print("value = %d  y = %d  x = %d" % (track[rows][0], track[rows][1], track[rows][2]))
                        find(cycle, track, lo, ld, track[rows][2], track[rows][1])
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
            break

    return dane


def down(cycle, lo, ld, x, y):

    dane = [cycle[y][x], y, x]
    while y < (ld-1):
        y = y + 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            break


    return dane


def left(cycle, lo, ld, x, y):

    dane = [cycle[y][x], y, x]
    while x > 0:
        x = x - 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            break

    return dane


def up(cycle, lo, ld, x, y):

    dane = [cycle[y][x], y, x]
    while y > 0:
        y = y - 1
        if cycle[y][x] == 0:
            dane = [cycle[y][x], y, x]
            break

    return dane

