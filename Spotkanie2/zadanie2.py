def odsetki(oproc, czas, kwota):
    wynik = kwota * 0.01 * oproc * (czas/12)
    kwota = kwota + wynik
    print("Odsetki wynosza: ", kwota)

odsetki(3, 12, 1000)


def odsetki2(oproc, czas, kwota):
    for i in range (12//czas):
        ods = kwota * 0.01 * oproc * (czas / 12)
        kwota = kwota + ods
    print("Odsetki wynosza: ", kwota)

odsetki2(3, 3, 1000)