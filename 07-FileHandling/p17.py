file = open("40lines.txt", "r")
copy = open("copylines.txt", "a")
for line in file:
    copy.write(line)
file.close()
copy.close()
file = open("40lines.txt", "r")
file_content = file.read()
copy = open("copylines.txt", "r")
copy_content = copy.read()
if file_content == copy_content:
    print("same")
file.close()
copy.close()