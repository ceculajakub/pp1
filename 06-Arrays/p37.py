def multiplication_table():
    array = [[0 for _ in range(5)] for _ in range(5)]
    for row in range(5):
        for column in range(5):
            array[row][column] = (row+1)*(column+1)
    for row in array:
        print(' '.join([str(elem) for elem in row]))



print(multiplication_table())