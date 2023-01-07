

def unique_elements(tab):
    unique_list = []

    for i in tab:
        if i not in unique_list:
            unique_list.append(i)
        else:
            unique_list.remove(i)
    return unique_list

print(unique_elements([2,3,2,5,8,1,9,8]))