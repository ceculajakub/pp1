def power(x, n):
    if n == 1:
        return x
    return x * power(x, n-1)

def zad_20():
    return power(5, 3)
print(zad_20())