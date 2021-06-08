import sort, road, zysk, iteration, block_road

def main_():
    #ld = 2 # docelowo 4
    #lo = 3 # docelowo 2

    ld = 4
    lo = 2

    z = [[0 for x in range(lo)] for y in range(ld)] # jednostkowy zysk
    c = [0 for x in range(lo)] # ceny sprzedazy
    kz = [0 for x in range(ld)] # koszty zakupu
    kt = [[0 for x in range(lo)] for y in range(ld)] # koszty jednostkowego transportu

    popyt = [0 for x in range(lo)]
    podaz = [0 for x in range(ld)]

    #beta = [0 for x in range(lo)] #po ustaleniu czy mamy fikcyjnych dostawcow/odbiorcow czy nie tworze nowe alfa i beta
    #alfa = [0 for x in range(ld)]

    jk = [[0 for x in range(lo)] for y in range(ld)]

    #popyt = [10, 28, 27]
    #podaz = [20, 30]

    #kt = [[8,14,17], [12,9,19]]
    #kz = [10, 12]
    #c = [30, 25, 30]

    popyt = [20, 40]
    podaz = [16, 12, 24, 15]

    kt = [[4, 8], [7, 10], [2, 9], [1, 3]]
    kz = [5, 4, 8, 7]
    c = [12, 15]

    for i in range(0, ld):
        for j in range(0, lo):
            z[i][j] = c[j] - kz[i] - kt[i][j]

    print("\n1. koszty transportu")
    for row in kt:
      print(' '.join([str(elem) for elem in row]))

    print("\n1. zyski jednostkowe")
    for row in z:
        print(' '.join([str(elem) for elem in row]))

    suma1, suma2 = 0, 0

    for i in popyt:
        suma1 = suma1 + i

    #print ("calkowity popyt %d" % suma1)

    for i in podaz:
        suma2 = suma2 + i
    #print ("calkowita podaz %d" % suma2)

    #blokowanie tras
    M = [2, 0]

    if suma1 != suma2:
        nz = [[0 for x in range(lo+1)] for y in range(ld+1)] # wprowadzam fikcyjnego odbiorcę i dostawcę
        for i in range(0, ld+1):
            for j in range(0, lo+1):
                if j == lo:
                    nz[i][j] = 0
                elif i == ld:
                    nz[i][j] = 0
                else:
                    nz[i][j] = z[i][j]
        #nz[M[0]][M[1]] = float("-inf") #ustawiam blokade
        popyt.append(suma2)
        podaz.append(suma1)
        #print("\nzbilansowane")
        #for row in nz:
        #    print(' '.join([str(elem) for elem in row]))
        z = nz
        lo = lo + 1
        ld = ld + 1

    #z[M[0]][M[1]] = float("-inf")
    z[M[0]][M[1]] = -9999
    print("\nzbilansowane")
    for row in z:
        print(' '.join([str(elem) for elem in row]))

    #beta = [0 for x in range(lo)]
    #alfa = [0 for x in range(ld)]

    #obliczanie trasy za pomoca metody maksymalnego elementu macierzy

    sorted = sort.sortowanie_babelkowe(z, lo, ld)
    sorted = sort.sortowanie_babelkowe(z, lo, ld)
    # sorted_r = sort.sortowanie_babelkowe(r, lo, ld)
    # print(sorted)

    # r = road.calc_road(sorted, lo, ld, popyt, podaz) #opcja bez blokowania tras

    # zmienna = get_alfa_beta.alfa_beta(sorted_r, r, z, ld, lo)

    # blokowanie tras
    r = block_road.calc_road(sorted, lo, ld, popyt, podaz, M, z)

    print("obliczona trasa")
    for row in r:
        print(' '.join([str(elem) for elem in row]))

    # obliczanie zysku

    zyski = [zysk.calc_zysk(z, r, lo, ld)]
    print("\nzysk_1: %d" % zyski[0])

    # profit to zysk posrednika
    profit, r = iteration.calc_iteration(r, z, lo, ld, zyski)
    print(profit)

    print("\n************************************")
    print("\nzyski jednostkowe")
    for row in z:
        print(' '.join([str(elem) for elem in row]))

    print("\nostateczna trasa")
    for row in r:
        print(' '.join([str(elem) for elem in row]))

    rows = len(kt)
    columns = len(kt[0])

    # calkowite koszty transportu
    ckt = 0
    for i in range(rows):
        for j in range(columns):
            ckt += kt[i][j] * r[i][j]

    # calkowite koszty zakupu
    ckz = 0
    suma = 0
    for i in range(rows):
        for j in range(columns):
            suma += r[i][j]
        ckz += suma * kz[i]
        suma = 0

    # calkowite koszty
    kc = ckz + ckt

    # calkowity przychod
    pc = 0
    suma = 0
    for i in range(columns):
        for j in range(rows):
            suma += r[j][i]
        pc += suma * c[i]
        suma = 0

    # calkowity_zysk = pc - kc #obliczenia muszą sie zgadzac z obliczonym maksymalnym profitem

    # print(calkowity_zysk)
    rows = len(profit)
    z[M[0]][M[1]] = float("-inf")

    return z, r, profit[rows - 1], kc, pc


z, r, max_zysk, kc, pc = main_()

print("\nmaksymalny zysk: %d" % max_zysk)
print("calkowity przychod: %d" % pc)
print("calkowite koszty: %d" % kc)