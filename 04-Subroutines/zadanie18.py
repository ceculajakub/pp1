def Sum_Digits(number):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number%10
        number //= 10
    return sum_of_digits

def zad_18():
    return Sum_Digits(7182)
print(zad_18())
