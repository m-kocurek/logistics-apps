def find_max(tab, lo, ld):

    maksimum = tab[0][0]
    dane = [maksimum, 0, 0]
    for i in range(0, ld):
        for j in range(0, lo):
            if maksimum < tab[i][j]:
                maksimum = tab[i][j]
                dane = [maksimum, i, j]

    return dane


def find_min(tab, lo, ld):

    minimum = tab[0][0]
    dane = [minimum, 0, 0]
    for i in range(0, ld):
        for j in range(0, lo):
            if minimum > tab[i][j]:
                minimum = tab[i][j]
                dane = [minimum, i, j]

    return dane




