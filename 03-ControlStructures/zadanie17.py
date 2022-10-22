#zadanie 17

x = int(input("Enter x axis coordinate: "))
y = int(input("Enter y axis coordinate: "))

first_quadrant = x < 0 and y > 0
second_quadrant = x < 0 and y < 0
third_quadrant = x > 0 and y < 0
fourth_quadrant = x > 0 and y > 0

if(first_quadrant):
    print("Point P({0}, {1}) is located in the first quadrant".format(x, y))
elif(second_quadrant):
    print("Point P({0}, {1}) is located in the second quadrant".format(x, y))
elif(third_quadrant):
    print("Point P({0}, {1}) is located in the third quadrant".format(x, y))
elif(fourth_quadrant):
    print("Point P({0}, {1}) is located in the fourth quadrant".format(x, y))
else:
    print("Point P({0}, {1}) is exactly the ({0}, {1}) point".format(x, y))





