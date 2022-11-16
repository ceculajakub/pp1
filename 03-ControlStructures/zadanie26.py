def zad_26():

    correct_pin = "0805"
    counter = 0 
    while counter < 3:
        input_pin = input("Please enter your pin: ")
        if input_pin != correct_pin:
            print("Incorrect...")
        else:
            print("Correct")
            return
        counter += 1
    print("Sorry, your payment card has been blocked.")
zad_26()
