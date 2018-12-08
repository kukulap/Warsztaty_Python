def portfel(kwota):
    nominaly = [1, 5, 2, 10, 20]
    nominaly.sort()
    nominaly.reverse()
    suma = 0
    print("Suma do zaplaty ", kwota, "zl")
    for element in nominaly:
        a = int(kwota / element)
        kwota = kwota % element
        print("Zaplac: ", a, " x ", element, "zl")

portfel(123)

portfel(597)