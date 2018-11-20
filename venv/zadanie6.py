def suma_dzielnikow(n):
    suma = 0
    i = 1
    while i <= (n-1):
        if n % i == 0:
            suma = suma + i
        i = i+1
    print("Suma dzielnikow liczby", n, "wynosi:", suma)

suma_dzielnikow(6)