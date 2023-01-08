def shopping():
    file = open("shopping.txt", "a")
    file.write(input("Inset product: ")+ "\n")
    file.close()
shopping()

