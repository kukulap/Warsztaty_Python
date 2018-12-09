import bmi

class Osoba:

    def __init__(self, imie, nazwisko, masa, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.masa = masa
        self.wzrost = wzrost

    def __str__(self):
        return "{0}: {1} {2}, BMI: {3}".format(str(self.__class__.__name__), self.imie, self.nazwisko, bmi.bmi(self.masa, self.wzrost))

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, masa, wzrost, pensja):
        Osoba.__init__(self, imie, nazwisko, masa, wzrost)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2

    """
    def __str__(self):
        return "Pracownik" + self.imie + " " + self.nazwisko
    """


class Kierownik(Pracownik):
    """
    def __init__(self, imie, nazwisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, pensja)
    """

    def wyplata(self):
        return super().wyplata() + 1200.0

o = Osoba("Jan",  "Kowalski", 90, 1.77)

p = Pracownik("Jan", "Nowak", 80, 1.75, 2250)
#print("{0} wypłata {1}".format(p, p.wyplata()))

k = Kierownik("Anna", "", 60, 1.65, 5000)
#print(k.wyplata())
print(k)
print(o)
print(p)

#p = Pracownik("Jan", "Nowak", 2250)
