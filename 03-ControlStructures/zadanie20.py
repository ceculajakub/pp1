#zadanie 20

number = int(input("Enter number: "))

for i in range(1, 11):
    print("{0} x {1} = {2} ".format(number, i, number*i))