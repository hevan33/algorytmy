# Podaj liczby parzyste od 35 do 107
a = 35 
b = 107
if a%2 ==1:
    a = a+1

for x in range(a,b+1,2):
    print(x)
# Podaj liczby nieparzyste od 35 do 107
a = 35 
b = 107
if a%2 ==0:
    a = a+1
for x in range(a,b+1,2):
    print(x)
# Podaj wszystkie liczby podzielne przez 7, z zakresy 71 do 148
a =  71
b = 148
podzielnik = 7
reszta = a%podzielnik
reszta = podzielnik - reszta
a = a + reszta
for x in range(a,b+1,7):
    print(x)

# Podaj wszystkie liczby podzielne przez 13, z zakresu 213 do 458
a = 213 
b = 458
p = 13
reszta = a%p 
reszta = p - reszta
a = a + reszta
for x in range(a,b,p):
    print(x)