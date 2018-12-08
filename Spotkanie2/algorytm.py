def alg():
    gracz = int(input("Ile zapałek bierzesz: "))
    if gracz > 3:
        print("Podałeś złą ilość. Musisz wziąć nie więcej niż 3 zapałki!")
        gracz = int(input("Ile zapałek bierzesz: "))
    return gracz