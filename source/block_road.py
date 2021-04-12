import sort
def calc_road(sorted, lo, ld, popyt, podaz, M, z):

    r = [[0 for x in range(lo)] for y in range(ld)]  # trasa
    block_column = M[1]
    block_tab = [[z[0][block_column], 0, block_column]]

    for i in range(1, ld):
        block_tab.append([z[i][block_column], i, block_column])

    block_tab = sort.sort(block_tab)
    #print(block_tab)
    lenght = len(block_tab)

    #obliczenie zablokowanej trasy
    for i in range(lenght):
        rows = block_tab[i][1]
        columns = block_tab[i][2]

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

        if sorted[i][0] != 0 and columns != block_column:
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
        if sorted[i][0] == 0 and columns != block_column:
            if popyt[columns] <= podaz[rows]:
                r[rows][columns] = popyt[columns]
                podaz[rows] = podaz[rows] - popyt[columns]
                popyt[columns] = 0

            else:
                r[rows][columns] = podaz[rows]
                popyt[columns] = popyt[columns] - podaz[rows]
                podaz[rows] = 0

    return r