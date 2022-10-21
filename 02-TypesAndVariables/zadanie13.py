#Zadanie 13
#First Way with Pi as a String Symbol

# Calculation of the area and circumference of a circle
##

# determine radius and PI
radius = 5
Pi = "π"
# calculate area 
area = radius**2
# calculate circumference 
circumference = 2*radius
# display results 
print(f"Pole wynosi: {area}{Pi}, obwód wynosi: {circumference}{Pi}")




#Second way with library
import math
# Calculation of the area and circumference of a circle
##

# determine radius and PI
radius = 5
Pi = math.pi

# calculate area 
area = Pi*radius**2
# calculate circumference 
circumference = 2*Pi*radius
# display results 
print(f"Pole wynosi: {area}, a obwód wynosi: {circumference} ")
