#zadanie 19
dog_age_human_years = int(input("Enter the dog's age in human years: "))

first_two_years_const = 2*10.5

if(dog_age_human_years <= 2):
    print("The dog's age in dog’s years is {0} years".format(dog_age_human_years*10.5))
else:
    dog_age_human_years -= 2
    print("The dog's age in dog’s years is {0} years".format(int(dog_age_human_years * 4 + first_two_years_const )))