def silnia(n):
    wynik = 1
    i = 1
    while i < n:
        i = i + 1
        wynik = wynik * i
    return wynik

#print(silnia(3))
#print(silnia(5))

def suma_silni(n):
    for i in range(n):
        wynik = 1
        suma = 0
        i = 1
        while i < n:
            i = i + 1
            wynik = wynik * i
            suma = suma + wynik
        return wynik
        return suma

print(suma_silni(4))

for i in range(3,6):
    print("{0}: {1:4d}".format(i, suma_silni(i)))