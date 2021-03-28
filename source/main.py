import sort, road, zysk

ld = 2 # docelowo 4
lo = 3 # docelowo 2


z = [[0 for x in range(lo)] for y in range(ld)] # jednostkowy zysk
c = [0 for x in range(lo)] # ceny sprzedazy
kz = [0 for x in range(ld)] # koszty zakupu
kt = [[0 for x in range(lo)] for y in range(ld)] # koszty jednostkowego transportu

popyt = [0 for x in range(lo)]
podaz = [0 for x in range(ld)]

beta = [0 for x in range(lo)]
alfa = [0 for x in range(ld)]

jk = [[0 for x in range(lo)] for y in range(ld)]

popyt = [10, 28, 27]
podaz = [20, 30]

kt = [[8,14,17], [12,9,19]]
kz = [10, 12]
c = [30, 25, 30]


for i in range(0, ld):
    for j in range(0, lo):
        z[i][j] = c[j] - kz[i] - kt[i][j]

#for row in kt:
    #print(' '.join([str(elem) for elem in row]))

#for row in z:
    #print(' '.join([str(elem) for elem in row]))


suma1, suma2 = 0, 0

for i in popyt:
    suma1 = suma1 + i

#print ("calkowity popyt %d" % suma1)

for i in podaz:
    suma2 = suma2 + i
#print ("calkowita podaz %d" % suma2)


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
    popyt.append(suma2)
    podaz.append(suma1)
    #for row in nz:
        #print(' '.join([str(elem) for elem in row]))
    z = nz
    lo = lo + 1
    ld = ld + 1

#obliczanie trasy za pomoca metody maksymalnego elementu macierzy

sorted = sort.sortowanie_babelkowe(z, lo, ld)
#print(sorted)

r = road.calc_road(sorted, lo, ld, popyt, podaz)

for row in r:
    print(' '.join([str(elem) for elem in row]))

#obliczanie zysku

zysk = zysk.zysk(z, r, lo, ld)
print("zysk %d" % zysk)

#obliczanie zmiennych dualnych

alfa[0] = 0
i, j = 0, 0

if r[i][j] != 0:
    if i == 0:
        beta[j] = z[i][j] - alfa[0]
    print("beta_0 %d" % beta[j])

if r[i][j] != 0:
    if beta[i] != 0:
        beta[j] = z[i][j] - alfa[0]
    print("beta_0 %d" % beta[j])

#beta[0] = r[0][0] - alfa[0]
#for i in range(ld):
#    for j in range(lo):
#        zysk += z[i][j]*r[i][j]