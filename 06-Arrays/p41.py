def identity_matrix(n):
    array = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        array[i][i] = 1
    return array
def correct_display(array):
    for row in array:
        for elem in row:
            print(elem, end = " ")
        print()
def program():
    correct_display(identity_matrix(3))
    print()
    correct_display(identity_matrix(5))
    print()
    correct_display(identity_matrix(8))


program()
