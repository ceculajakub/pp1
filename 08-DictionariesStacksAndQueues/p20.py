import stack

def binary():
    number = int(input("Enter num: "))
    while number != 0:
        stack.push(number%2)
        number//=2
    stack.display()
    result =""
    while len(stack.stack) != 0:
        result += str(stack.pop())
    return result

print(binary())