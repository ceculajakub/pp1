def reverse(tab):
    # return tab[::-1]
    # for i in range (len(tab)-1, -1, -1):
    #     yield tab[i]
    result = []
    i = len(tab)-1
    while i>=0:
        result += [tab[i]]
        i-=1
    return result

    

print(reverse([1,2,3]))