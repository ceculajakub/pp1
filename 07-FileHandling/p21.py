file = open("p21_result.py", "a")
for i in range(1, 11):
    file.write(f"{i}, {i**2}, {i**3}\n")
file.close()