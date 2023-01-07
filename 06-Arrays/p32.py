def is_subset(array1, array2):
    if len(array1) > len(array2):
        return False
    is_correct = True
    for i in array1:
        if i not in array2:
            is_correct = False
    return is_correct

print(is_subset([1,2], [1,2,3]))