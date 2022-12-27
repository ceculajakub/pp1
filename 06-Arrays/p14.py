def f(tab):
    max_string = ""
    tmp = 0
    for i in tab:
        if len(i) > tmp:
            tmp = len(i)
            max_string = i
    return max_string
    
print(f(["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]))