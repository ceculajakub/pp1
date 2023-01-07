
def separate(array):
    even_arr = []
    odd_arr = []
    for i in array:
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
    return even_arr + odd_arr

print(separate([1,2,3,4,5,6,7,8,9]))