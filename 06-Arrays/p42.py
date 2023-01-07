def transpose_matrix(m):
    result = [[0 for i in range(len(m[0]))] for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result

def correct_display(array):
    for row in array:
        for elem in row:
            print(elem, end = " ")
        print()

correct_display(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]))