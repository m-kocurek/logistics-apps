def calc_zysk(z, r, lo, ld):
    zysk = 0
    for i in range(ld):
        for j in range(lo):
            zysk += z[i][j] * r[i][j]

    return zysk
