def count_lines():
    name = input("Insert name: ")
    file = open(name, "r")
    counter = 0
    for line in file:
        counter+=1
    file.close()
    print(f"File name: {name} ")
    print(f"Number of lines: {counter} ")
count_lines()