def calc_new_road(track, r):

    rows = len(track)
    y = track[0][1]
    x = track[0][2]
    calc = [[r[y][x], y , x, 1]]

    # plus = value = 1, minus = value = 0
    value = 0
    for i in range(1, rows):
            y = track[i][1]
            x = track[i][2]
            #print(r[y][x])
            calc.append([r[y][x], y , x, value])
            if i%2 == 0:
                value = 0
            else:
                value = 1

    find_minus = [[calc[1][0], calc[1][1], calc[1][2]]]
    for i in range(2, rows):
        if calc[i][3] == 0:
            find_minus.append([calc[i][0], calc[i][1], calc[i][2]])

    minimum = find_minus[0][0]
    dane = [minimum, 0, 0]
    rows = len(find_minus)

    for i in range(rows):
        if minimum > find_minus[i][0]:
            minimum = find_minus[i][0]
            dane = [minimum, find_minus[i][1], find_minus[i][2]]

    #print(dane)

    rows = len(track)
    for i in range(rows):
        if i == 0:
            calc[i][0] = calc[i][0] + dane[0]
        elif i%2 == 0:
            calc[i][0] = calc[i][0] + dane[0]
        else:
            calc[i][0] = calc[i][0] - dane[0]

    for i in range(rows):
        y = track[i][1]
        x = track[i][2]
        r[y][x] = calc[i][0]

    return r











