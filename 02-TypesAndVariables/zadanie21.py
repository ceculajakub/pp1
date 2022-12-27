#zadanie 21
from random import randint


computer_roll = randint(1, 6)
player_guess = int(input("Enter your dice roll guess: "))
print(f"{computer_roll == player_guess}")