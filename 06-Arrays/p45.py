def convert_to_1d(array):
    result = array[0]
    for i in range(1, len(array)):
        for j in range(len(array[0])):
            result.append(array[i][j])
    return result

print(convert_to_1d([[2,3],[1,5]]))