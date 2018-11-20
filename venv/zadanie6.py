def suma_dzielnikow(n):
    suma = 0
    lista = []
    i = 1
    while i <= (n-1):
        if n % i == 0:
            suma = suma + i
            lista.append(i)
        i = i+1
    print("Suma dzielnikow liczby", n, "wynosi:", suma)
    print(lista)

suma_dzielnikow(10)