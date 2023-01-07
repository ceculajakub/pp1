
def greater(number, array):
    counter = 0
    for i in array:
        if i > number:
            counter +=1
    return counter

print(greater(1, [0,-1,-3]))