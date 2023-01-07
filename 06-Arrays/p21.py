
def unique_nums(array1, array2):
    for i in array1:
        if i in array2:
            continue
        print(i)
unique_nums([4,36,12,28,9,44,5], [5,1,36])
