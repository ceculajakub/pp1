import random

file = open("p20_result.txt", "a")
for i in range(50):
    file.write(str(random.randint(100,999)) + "\n")
file.close()