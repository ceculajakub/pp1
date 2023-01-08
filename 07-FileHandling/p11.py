
def write_lines_films():
    film_titles = ["The Shining\n", "Mr.Robot\n", "Glass Onion\n", "Zodiac\n", "The Office\n"]
    file = open("films.txt", "w")
    file.writelines(film_titles)
    file.close()
write_lines_films()