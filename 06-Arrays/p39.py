
array= [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,]]

def swap_rows(array):
    array[0], array[-1] = array[-1], array[0]
    return array

def correct_display(array):
    for row in array:
        for elem in row:
            print(elem, end = " ")
        print()
correct_display(swap_rows(array))



