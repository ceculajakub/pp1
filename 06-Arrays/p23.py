
def occurs(number, array):
    if number in array:
        return True
    else:
        return False

def program():
    array = [15,38,7,23,14]
    number = int(input("Insert number: "))
    if(occurs(number, array)):
        print(f"number {number} appears in the array")
    else:
        print(f"number {number} does not appear in the array")

program()