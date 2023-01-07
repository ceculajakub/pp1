def median(array):
    array = bubblesort(array)
    if len(array) % 2 == 0:
        return (array[len(array)//2-1] + array[len(array)//2])/2
    else:
        return array[len(array)//2]




def bubblesort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                swapped = True
    return array

result = median([1,0,9,4,6])
print(result)