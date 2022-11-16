def zad_29():

    quantity = 0
    sum_numbers = 0
    arithmetic_numbers = 0
    input_num = int(input("Enter number: "))
    
    while input_num != 0:
        quantity += 1
        sum_numbers += input_num
        arithmetic_numbers = sum_numbers/quantity
        input_num = int(input("Enter number: "))

    return(f"RESULT: Quantity={quantity}, Sum ={sum_numbers}, Mean={arithmetic_numbers}")
print(zad_29())        

