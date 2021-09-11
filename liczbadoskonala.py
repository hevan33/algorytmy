n = 6

tab = [5,214,5,6,124,28]

def czy_doskonala(n):
    wynik = 0    
    for i in range(1,n+1):
        if n % i ==0:
            wynik = wynik + i
        else:
            continue
    wynik = wynik - n
    
    if wynik == n:
        print(n)
        print("jest liczbą doskonałą")


for n in tab:
    czy_doskonala(n)
