def sortowanie_babelkowe(tab, lo, ld):

    n = ld * lo
    rows = []
    columns = []
    list = []

    lista = [[0 for x in range(3)] for y in range(n)]
    for i in range(ld):
        for j in range(lo):
            list.append(tab[i][j])
            rows.append(i)
            columns.append(j)

    for i in range(n):
        for j in range(3):
            if j == 0:
                lista[i][j] = list[i]
            elif j == 1:
                lista[i][j] = rows[i]
            else:
                lista[i][j] = columns[i]


    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if lista[l][0] < lista[l + 1][0]:
                lista[l][0], lista[l + 1][0] = lista[l + 1][0], lista[l][0]
                lista[l][1], lista[l + 1][1] = lista[l + 1][1], lista[l][1]
                lista[l][2], lista[l + 1][2] = lista[l + 1][2], lista[l][2]

                zamien = True

        n -= 1

        if zamien == False: break

    return lista



#while n > 1:
#    zamien = False
#    for l in range(0, n - 1):
#        if list[l] < list[l + 1]:
#            list[l], list[l + 1] = list[l + 1], list[l]
#            zamien = True

#    n -= 1

#    if zamien == False: break