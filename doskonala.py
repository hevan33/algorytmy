n = 496
wynik = 0
for i in range(1,n+1):
    if n%i ==0:
        wynik+=i
    if wynik == n:
        print("liczba jest doskonala")
        break
    if wynik>n:
        print("liczba jest niedoskonala")
        break
