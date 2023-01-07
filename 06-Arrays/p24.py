def nd_largest(array):
    largest = 0
    second_largest = 0
    for i in array:
        if i > largest:
            largest = i
        elif i < largest and i > second_largest:
            second_largest = i
    return second_largest

print(nd_largest([5,1,9,6,1]))