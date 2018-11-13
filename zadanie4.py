p1 = 44490
p2 = 85528

def podatek(kwota):
    if kwota <= p1:
        wynik = 0.19 * kwota
        return wynik
    elif kwota > p1 and kwota <= p2:
        a = (kwota - p1) * 0.3
        b = p1 * 0.19
        wynik = a + b
        return wynik
    else:
        a = (kwota - p2) * 0.4
        b = (kwota - a) * 0.3
        c = p1 * 0.19
        wynik = a + b + c
        return wynik

print(podatek(40000))

def podatek2(kwota):
    wynik = 0
    if kwota <= p1:
        wynik = 0.19 * kwota
    elif kwota > p1 and kwota <= p2:
        a = (kwota - p1) * 0.3
        b = p1 * 0.19
        wynik = a + b
    else:
        a = (kwota - p2) * 0.4
        b = (kwota - a) * 0.3
        c = p1 * 0.19
        wynik = a + b + c
    print("Podatek od kwoty ", kwota, "wynosi: ", wynik, " zl.")
    return wynik

podatek2(45000)