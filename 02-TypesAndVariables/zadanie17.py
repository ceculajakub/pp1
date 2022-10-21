#zadanie17
from math import floor


height_cm = 170
height_feet = floor(170*0.032808)
inches = round((170*0.032808 - height_feet)*12)


print("I am {0}cm tall, i.e. {1} feet and {2} inches".format(height_cm, height_feet, inches))