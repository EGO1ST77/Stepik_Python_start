import random
n = 100
a = [random.randint(-100, 100) for i in range(n)]

for i in range(1, n):
    min_el = a[i]
    j = i
    while j >= 1 and a[j-1] > min_el:
        a[j] = a[j-1]
        j -= 1
    a[j] = min_el

print(f'Sort list: {a}')