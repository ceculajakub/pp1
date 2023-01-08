import re

file = open("40lines.txt", "r")
content = file.read()
words_arr = re.findall(r"\b\w+\b", content)
for word in words_arr:
    if len(word) >= 6:
        print(word)
file.close()