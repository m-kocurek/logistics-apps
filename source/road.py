def calc_road(sorted, lo, ld, popyt, podaz):

    r = [[0 for x in range(lo)] for y in range(ld)]  # trasa

    for i in range(lo * ld):

        rows = sorted[i][1]
        columns = sorted[i][2]

        if sorted[i][0] != 0:
            # if rows!=ld-1 or columns!=lo-1: #cos z tym nie tak, do sprawdzenia
            if popyt[columns] <= podaz[rows]:
                r[rows][columns] = popyt[columns]
                podaz[rows] = podaz[rows] - popyt[columns]
                popyt[columns] = 0

            else:
                r[rows][columns] = podaz[rows]
                popyt[columns] = popyt[columns] - podaz[rows]
                podaz[rows] = 0

    for i in range(lo * ld):

        rows = sorted[i][1]
        columns = sorted[i][2]

        # if rows==ld-1 or columns==lo-1: # do sprawdzenia
        if sorted[i][0] == 0:
            if popyt[columns] <= podaz[rows]:
                r[rows][columns] = popyt[columns]
                podaz[rows] = podaz[rows] - popyt[columns]
                popyt[columns] = 0

            else:
                r[rows][columns] = podaz[rows]
                popyt[columns] = popyt[columns] - podaz[rows]
                podaz[rows] = 0

    return r