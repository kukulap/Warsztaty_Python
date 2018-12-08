import random
import algorytm

def gra():
    #maksymalna liczba wylosowanych zapalek wynosi 50
    ilosc = random.randint(7, 50)
    print("Ilość zapałek w tej rundzie wynosi: ", ilosc)
    print("Zasady: możesz wyciągnąć 1, 2 lub 3 zapałki")
    while ilosc > 0:
        ilosc = ilosc - algorytm.alg()
        if ilosc <= 0:
            print("Przegraleś!")
            break
        komp = random.randint(1, 3)
        print("Komputer wylosował:", komp)
        ilosc = ilosc - komp
        if ilosc <= 0:
            print("Komputer przegrał, wygrałeś!")

        '''do sprawdzania poprawnosci kodu'''
        #print("Zostało ", ilosc, "zapałek")


gra()