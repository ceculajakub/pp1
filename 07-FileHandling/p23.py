import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
average_temp = 0
for i in temperatures:
    average_temp += int(i)
average_temp /= len(temperatures)
print(average_temp)