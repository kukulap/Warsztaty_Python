def statystyka(plik):
    with open(plik, 'r') as fh:
        tekst = fh.read()

statystyka("Romeo_i_Julia.txt")