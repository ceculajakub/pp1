
def comas(array):
    return str(array).lstrip("[").rstrip("]").strip(" ")


print(comas([1,2,3,4]))