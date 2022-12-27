def f(arr1, arr2):
    # result = []
    # for i in arr1:
    #     flag = True
    #     for j in arr2:
    #         if i==j:
    #             flag = False
    #             break
    #     if flag:
    #         result+= [i]
    # return result
    # this method is faster than the one above, because set uses hashmaps to compare values
    arr2_s = set(arr2)
    result = [x for x in arr1 if x not in arr2_s ]
    return result
print(f([4,36,12,28,9,44,5],[5,1,36]))