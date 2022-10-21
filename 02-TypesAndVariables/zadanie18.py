#zadanie 18
a = int(input("Insert a: "))
b = int(input("Insert b: "))
c = int(input("Insert c: "))

p = (a+b+c)/2

area = (p*(p-a)*(p-b)*(p-c))**0.5
print("Area equals = {0}".format(area))