
array = [[1,2,3,4],[5,6,7,8]]
print(array)

def correct_display(array):
    for row in array:
        for elem in row:
            print(elem, end = " ")
        print()
correct_display(array)