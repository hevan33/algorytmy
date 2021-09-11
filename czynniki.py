def czynniki(n):
    dzielniki = []

    y = n

    for i in range (2,n+1):
        
        if y <= 1 :
            break
        else:
            if y % i == 0:
                for a in range(2,n+1): 
                    if y % i == 0:
                        dzielniki.append(i)
                        y = y/i
                        
            else:
                continue
    print(dzielniki)
tab = [32,434,12,421,2,8,314]
for g in tab:
    print(czynniki(g))