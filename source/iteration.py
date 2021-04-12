import max_min, find_cycle, new_road, zysk
def calc_iteration(r, z, lo, ld, profit):

    alfa = [None] * ld
    beta = [None] * lo

    alfa[0] = 0

    for k in range(ld):
        for i in range(lo):
            if r[k][i] != 0:
                if alfa[k] != None:
                    beta[i] = z[k][i] - alfa[k]
                    for j in range(ld):
                        if r[j][i] != 0:
                            if beta[i] != None:
                                alfa[j] = z[j][i] - beta[i]


    cycle = [[0 for x in range(lo)] for y in range(ld)]

    for i in range(ld):
        for j in range(lo):
            if r[i][j] > 10:
                cycle[i][j] = 0
            else:
                cycle[i][j] = z[i][j] - alfa[i] - beta[j]

    maksimum = max_min.find_max(cycle, lo, ld)
    #print(maksimum)

    #print("\n")
    #for row in cycle:
    #    print(' '.join([str(elem) for elem in row]))

    if maksimum[0] > 0:

        y = maksimum[1]  # ld
        x = maksimum[2]  # lo

        dane = [[cycle[y][x], y, x]]
        track = find_cycle.find(cycle, dane, lo, ld, x, y)

        r = new_road.calc_new_road(track, r)

        #print("\n")
        #for row in r:
        #    print(' '.join([str(elem) for elem in row]))

        profit.append(zysk.calc_zysk(z, r, lo, ld))

        #niepotrzebne
        #if zyski != profit:
        #    zyski_tab.append(zyski)
        #    calc_iteration(r, z, lo, ld, zyski, zyski_tab)


    return profit

