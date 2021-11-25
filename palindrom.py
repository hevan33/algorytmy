slowo = "koccok"
for i in range (0,int(round(len(slowo)/2,0))):
    if slowo[i] == slowo[(i*(-1))-1]:
        pass
    else:
        print("nie jest palindromem")
        break
    if i == int(round(len(slowo)/2,0))-1:
        print("jest palindromem")