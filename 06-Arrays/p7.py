def f(tab):
    even_num = 0
    odd_num = 0
    for i in tab:
        if i%2 == 0:
            even_num+=1
        else:
            odd_num+=1
    print(f"even numbers: {even_num}, odd numbers; {odd_num}")

f([15, 8, 31, 47, 2, 19])