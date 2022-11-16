def LettersCounter(sentence, letter):
    counter = 0
    for i in sentence:
        if i == letter:
            counter +=1
    return counter

def zad_17():
    return LettersCounter("You never get a second chance to make a first impression","e")
print(zad_17())