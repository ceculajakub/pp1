meat = open("MeatAndFish.txt", "r")
bread = open("GrainsAndBread.txt", "r")
result = open("p18_result.txt", "a")
result.write(meat.read())
result.write(bread.read())
meat.close()
bread.close()
result.close()