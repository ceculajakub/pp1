file = open("p19_result.txt", "a")
for i in range (1,51):
    file.write(f"{i}" + "\n")
file.close()