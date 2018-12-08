from pakiet import VAT

def zakupy(cennik, lista):
    suma = 0
    paragon = []
    for towar in cennik:
        for produkt in lista:
            if produkt == towar:
                paragon.append(cennik[towar] * lista[produkt])
                suma += cennik[towar] * lista[produkt]
    return suma + VAT.vat_paragon(paragon)



cennik = {'kawa': 14.99, 'pomarańcze': 3.49, 'olej': 4.99}
lista = {'olej': 2, 'kawa': 1}

print("Kwota brutto:", zakupy(cennik, lista))