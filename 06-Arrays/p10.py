def sum(array):
    result = 0
    for i in array:
        result+=i
    return result
def array2str(array):
    return ' '.join(map(str, array))
    
print(array2str([4, 3, 7, 1, 3]))
print(sum([4, 3, 7, 1, 3]))