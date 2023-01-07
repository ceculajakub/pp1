def minmax2d(array):
    largest = array[0][0]
    largest_index = (0,0)
    smallest = array[0][0]
    smallest_index = (0,0)
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] > largest:
                largest = array[i][j]
                largest_index = (i,j)
            if array[i][j] < smallest:
                smallest = array[i][j]
                smallest_index = (i,j)

    return [largest, largest_index], [smallest, smallest_index]



    


print(minmax2d([[-38, 19], [5,40],[-7,11],[29,16]]))
