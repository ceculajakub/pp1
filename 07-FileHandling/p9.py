def sum_integers_file():
    result = 0
    file = open("numbers.txt", "r")
    for line in file:
        result += int(line)
    file.close()
    return result

print(sum_integers_file())

    
