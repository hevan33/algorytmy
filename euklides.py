def euklides(a,b):
    while a!=b:
        if a>b:
            a = a- b 
        else:
            b = b-a 
            return a
    return a
print(euklides(9,18))
