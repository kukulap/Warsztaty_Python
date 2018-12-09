def bmi(masa, wzrost):
    BMI = masa / wzrost**2
    if BMI < 18.5:
        wynik = "niedowaga"
    elif BMI >= 18.5 and BMI < 25:
        wynik = "prawidlowe"
    else:
        wynik = "nadwaga"
    return wynik

"""
def komentarz():
    masa = float(input("Podaj wage w kg: "))
    wzrost = float(input("Podaj wzrost w m: "))
    rezultat = print("Twoj wynik BMI: ", bmi(masa, wzrost))

"""
