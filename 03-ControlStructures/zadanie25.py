def zad_25(a, b):
    if a < b:
        tmp = b 
        b = a
        a = tmp 
    for i in range (0,b):
        if(i == 0 or i == b-1):
            print(a*"*")
            continue
        print("*" +(a-2)*" " +"*")
zad_25(4, 15)