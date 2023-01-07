def sum2d(array):
    result = 0
    for row in array:
        result += row[-1]
    return result

print(sum2d([[1,2,3], [4,5,6], [7,8,9]]))
