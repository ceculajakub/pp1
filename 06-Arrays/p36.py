def create_2d_arr(x,y):
    array = [[0 for i in range(x)] for i in range(y)]
    return array
    
def correct_display(array):
    for row in array:
        for elem in row:
            print(elem, end = " ")
        print()
print(correct_display(create_2d_arr(3,5)))