import random

def rand_elem(array):
    random_index = random.randint(0, len(array))
    return array[random_index]

print(rand_elem([1,2,3,4,5,6]))
