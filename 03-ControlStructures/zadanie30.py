def zad_30(n):
    counter = 1
    yield 2
    i = 3
    while counter != n:
        j = 2
        is_prime = True
        while j <= i**0.5:
            if i % j == 0:
                is_prime = False
                break 
            j += 1
        if is_prime:
            counter +=1 
            yield i
        i+=2
for i in zad_30(10):
    print(i)