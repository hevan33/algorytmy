liczba_1 = 12
liczba_2 = 4127
liczba_3 = 7
liczba_4 = 1
liczba_5 = 87
tablica = [liczba_1,liczba_2,liczba_3,liczba_4,liczba_5]


def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True
for n in tablica:
    print(czy_pierwsza(n))

