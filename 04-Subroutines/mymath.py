#mymath.py

from random import randint

def read_number():
    x = input("Enter number: ")

    return int(x)

def generate_number():
    return randint(1,9)
