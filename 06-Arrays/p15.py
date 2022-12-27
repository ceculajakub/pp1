def write_to_txt(tab):
    with open("colors.txt", "w") as f:
        f.write(''.join(tab))

write_to_txt("yellow, green, blue")