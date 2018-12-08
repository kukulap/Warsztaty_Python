def suma_dzielnikow(n):
    suma = 0
    lista = []
    i = 1
    while i <= (n-1):
        if n % i == 0:
            suma = suma + i
            lista.append(i)
        i = i+1
    return lista

print(suma_dzielnikow(4))

def pierwsza(n):
    if len(suma_dzielnikow(n)) > 1:
        return False
        #print("liczba ", n, "nie jest liczbą pierszą")
    else:
        return True
        #print("liczba ", n, "jest liczbą pierszą")

print(pierwsza(5))

def dzielniki_pierwsze(n):
    liczby_pierwsze = []
    for element in suma_dzielnikow(n):
        if pierwsza(element) == True:
            liczby_pierwsze.append(element)
    return liczby_pierwsze

print(dzielniki_pierwsze(16))

def doskonala(n):
