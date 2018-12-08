def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23*suma, 2)
    return vat

zakupy = [0.8, 0.5, 4.59, 7]


def vat_paragon(lista):
    suma = 0
    for element in lista:
        vat = round(0.23 * element, 2)
        suma = suma + vat
    return suma
