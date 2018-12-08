def rozmien(portfel, kwota):
    portfel.reverse()
    nominaly = [0, 1, 2, 3, 4, 5]
    nominaly.reverse()
    for i in range(len(portfel)):
        if portfel[i] != 0:
            a = kwota // nominaly[i]
            if a > portfel[i]:
                kwota = kwota - (portfel[i] * nominaly[i])
                a = portfel[i]
            else:
                kwota = kwota % nominaly[i]
            print("Zapłać:", a, " x ", nominaly[i], "zl")


portfel = [0, 2, 3, 0, 0, 5]
rozmien(portfel, 29)

def rozmien2(portfel, kwota):
    wynik = [0] * len(portfel)
    zostalo = kwota
    for nominal in reversed(range(len(portfel))):
        if zostalo <= 0:
            break
        elif portfel[nominal] == 0:
            continue

        liczba_nominalow = min(zostalo // nominal, portfel[nominal])
        #zostalo = zostalo - liczba_nominalow * nominal
        zostalo -= liczba_nominalow * nominal
        portfel[nominal] -= liczba_nominalow
        wynik[nominal] = liczba_nominalow

    while zostalo > 0:
        if portfel == [0] * len(portfel):
            break
        for nominal in reversed(range(len(portfel))):
            if portfel[nominal] > 0:
                zostalo -= nominal
                portfel[nominal] -= 1
                wynik[nominal] += 1
    return wynik

rozmien2(portfel, 31)