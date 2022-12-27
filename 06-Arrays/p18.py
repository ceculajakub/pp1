def bubblesort(tab):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(tab)):
            if tab[i-1] > tab[i]:
                tab[i-1], tab[i] = tab[i], tab[i-1]
                swapped = True
    return tab
print(bubblesort([1,3,2]))