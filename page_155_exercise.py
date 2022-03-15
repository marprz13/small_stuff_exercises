import sys

def programik(lista):
    dlugosc_listy = len(lista)
    item = 0
    while item < dlugosc_listy:
        for i in lista:
            if item == dlugosc_listy -2:
                print(i, end = ' i ')
                item += 1
            elif item == dlugosc_listy -1:
                print(i)
                item += 1
            else:
                print(i, end = ', ')
                item += 1



spam = ['jeden', 'dwa', 'trzy', 'cztery', 'siedem']

programik(spam)
