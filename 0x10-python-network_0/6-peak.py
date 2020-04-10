#!/usr/bin/python3
'''finds a peak in a list of unsorted integers'''
def find_peak(list_of_integers):

    longitud = len(list_of_integers)
    n = longitud // 2
    x = 0
    while x < longitud:
        x += 1
        if n == 0:
            gtl = True
        else:
            gtl = False
        if n == longitud - 1:
            gtr = True
        else:
            gtr = False
        if n > 0:
            if list_of_integers[n - 1] < list_of_integers[n]:
                gtl = True
        if n < longitud - 1:
            if list_of_integers[n] > list_of_integers[n + 1]:
                gtr = True
        if gtl and gtr:
            return list_of_integers[n]
        if not gtr:
            n += (longitud - n) // 2
        elif not gtl:
            n -= n // 2
