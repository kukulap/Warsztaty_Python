import csv

with open('gielda.csv', newline='') as plik:
    klucze = ["Nazwa", "Jednostki", "Kurs"]
    reader = csv.DictReader(plik, fieldnames=klucze)

    akcje = {}
    suma = 0
    for row in reader:
        suma += float(row["Kurs"]) * float(row["Jednostki"])

        akcje[row["Nazwa"]] = row["Jednostki"]

    print(akcje)
    print("Wartość twoich akcji wynosi: ", round(suma,2))
