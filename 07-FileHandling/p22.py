import csv

file = open("students.txt", "r")
content = csv.reader(file)
for row in content:
    if int(row[2]) < 30:
        print(row[0] + " " + row[1] + " " + row[4]) 
file.close()