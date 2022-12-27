def f(tab):
    max_val = max(tab)
    min_val = min(tab)
    result = [max_val, min_val]
    return result

result = f([-15, 8, -31, 47, -2, 19])

print(f"Max value = {result[0]}, min value = {result[1]}")