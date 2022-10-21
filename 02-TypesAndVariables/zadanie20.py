#zadanie 20
from random import randint, randrange


first_roll = randint(1, 6)
second_roll = randint(1, 6)
third_roll = randint(1, 6)
sum_of_rolls = first_roll + second_roll + third_roll
print("First roll: {0} Second roll: {1} Third roll: {2} \n Sum of rolls: {3} ".format(first_roll, second_roll, third_roll, sum_of_rolls))

