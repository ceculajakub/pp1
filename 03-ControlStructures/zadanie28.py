def zad_28():
    x = 0
    y = 1 
    counter = 0 
    print(x)
    while counter < 50:
        print(y)
        tmp = y
        y = x + tmp
        x = tmp
        counter += 1

zad_28()