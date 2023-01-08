with open("films.txt", "r") as f:
    for line in f:
        print(line, end="")
    f.close()
