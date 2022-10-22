#zadanie 18

base_amount = int(input("Enter amount: "))
amount = base_amount

five_zloty_coins_counter = 0
two_zloty_coins_counter = 0
one_zloty_coins_counter = 0

if(amount >=5 ):
    amount //= 5
    five_zloty_coins_counter = amount
    amount = base_amount - five_zloty_coins_counter * 5
    base_amount = amount
if(amount >= 2):
    amount //= 2
    two_zloty_coins_counter = amount
    amount = base_amount - two_zloty_coins_counter * 2
    base_amount = amount
if(amount >= 1):
    one_zloty_coins_counter = amount

print("{0} in coins: \n 5 zloty coins: {1} \n 2 zloty coins: {2} \n 1 zloty coins: {3}".format(amount, five_zloty_coins_counter, two_zloty_coins_counter, one_zloty_coins_counter))
