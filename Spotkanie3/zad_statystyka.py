def statystyka(plik):
    Tekst = open(plik, 'r')
    tekst = Tekst.read().lower()

    for char in '-.,\n':
        text = tekst.replace(char, ' ')

    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
    lista_slow = text.split()
    slownik = {}

    # Count number of times each word comes up in list of words (in dictionary)
    for slowo in lista_slow:
        if slowo not in slownik:
            slownik[slowo] = 0
        slownik[slowo] += 1

    print(slownik)

slownik1 = statystyka("Romeo_i_Julia.txt")
slownik2 = statystyka("Sen_nocy_letniej.txt")