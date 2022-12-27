def asteriks(n):
    return n*"*"

def f(tab):
    for i in tab:
        print(f"{i}: {asteriks(i)}")

f([12,6,4,9,3])