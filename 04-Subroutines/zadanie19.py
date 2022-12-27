def Is_In_Range(number, x_border, y_border):
    if number >= x_border and number <= y_border:
        return True
    return False

def zad_19():
    return Is_In_Range(2, 1, 5)
    
print(zad_19())