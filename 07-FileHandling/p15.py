file = open("40lines.txt", "r")
i = 0 
for line in file:
    if i % 5 ==0 and i != 0:
        input("Press enter: ")
    print(line)
    i+=1
file.close()