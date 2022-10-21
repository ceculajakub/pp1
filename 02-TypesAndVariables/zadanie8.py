#zadanie 8

#First way python syntax
x, y = 7, 34
x,y = y, x
print(f"Po zamianie wartość x wynosi: {x}, a wartość y wynosi: {y}")
#Second way temp variable
x, y = 7, 34
temp = x
x = y
y = temp
print(f"Po zamianie wartość x wynosi: {x}, a wartość y wynosi: {y}")
