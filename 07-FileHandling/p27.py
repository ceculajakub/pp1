import re

file = open("grades.txt", "r")
content = file.read()
grades = re.findall("\d+\.\d+", content)
file.close()
average_grades = 0
for grade in grades:
    average_grades += float(grade)
average_grades /= len(grades)
print(average_grades)