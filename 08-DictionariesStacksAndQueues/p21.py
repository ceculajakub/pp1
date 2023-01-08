import stack


def calculate_rpn():
    expression = input("Enter expression")
    operators = ["+","-","/","*"]
    for i in expression:
        if i.isdigit():
            stack.push(i)
        elif i in operators:
            first = stack.pop()
            second = stack.pop()
            result = str(eval(f"{first}{i}{second}"))
            stack.push(result)
        elif i == "=":
            result = stack.pop()
            return result



print(calculate_rpn())