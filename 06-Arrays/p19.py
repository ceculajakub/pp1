
def star(n):
    return n*"*"

def numbers_to_stars (tab):
    for number in tab:
        print(str(number) + ": " +star(number) )

numbers_to_stars([12, 6, 4, 9, 10])