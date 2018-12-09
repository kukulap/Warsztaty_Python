class Wyrazenie:
    pass

class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return stan[self.nazwa]


class Dodawanie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " + " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) + self.prawy.oblicz(stan)

class Mnozenie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " * " + str(self.prawy)

    def oblicz(self, stan):
        return self.lewy.oblicz(stan) * self.prawy.oblicz(stan)

stan = {'x' : 1, 'y' : 4, 'z' : 3}
wyrazenie = Dodawanie(Dodawanie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
print("{0} = {1}".format(wyrazenie, wyrazenie.oblicz(stan)))

mnozenie = Mnozenie(Mnozenie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
print("{0} = {1}".format(mnozenie, mnozenie.oblicz(stan)))

