def program():
    array = [1,23,5,382,1,17,4,906]
    print(6*len(array)*"-")
    for i in range(0, len(array)):
        print(f"|   {array[i]}",end="")
        if i == len(array)-1:
            print("|")
    print(6*len(array)*"-")

program()